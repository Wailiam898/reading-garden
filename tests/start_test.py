"""Start must not depend on media/storage promises settling (Safari/in-app browsers)."""
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError
import json, os
ROOT=Path(__file__).resolve().parents[1]
URL=os.environ.get('GAME_URL','https://wailiam898.github.io/reading-garden/')
SCENARIOS={
    'normal': '',
    'media_play_never_settles': "HTMLMediaElement.prototype.play=function(){return new Promise(()=>{});};",
    'audio_resume_never_settles': "window.AudioContext=class {constructor(){this.state='suspended';}resume(){return new Promise(()=>{});} };",
    'indexeddb_never_settles': "Object.defineProperty(window,'indexedDB',{value:{open(){return {};}}});",
    'audio_api_unavailable': "window.AudioContext=undefined;window.webkitAudioContext=undefined;",
}
def main():
    results=[]
    with sync_playwright() as p:
        for engine in os.environ.get('ENGINES','chromium').split(','):
            browser=getattr(p,engine).launch(headless=True,**({'channel':'chrome'} if engine=='chromium' else {}))
            for name,init in SCENARIOS.items():
                context=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True)
                if init:context.add_init_script(init)
                page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
                page.goto(URL);page.locator('[data-act="start"]').tap()
                try:
                    page.locator('[data-act="meet"]').wait_for(timeout=1500)
                    ok=page.evaluate('G.screen')=='home'
                except TimeoutError:ok=False
                results.append({'engine':engine,'scenario':name,'garden_opens_within_1500ms':ok,'errors':errors})
                context.close()
            browser.close()
    (ROOT/'test-results').mkdir(exist_ok=True)
    (ROOT/'test-results/start-results.json').write_text(json.dumps(results,indent=2))
    print(json.dumps(results,indent=2))
    assert all(x['garden_opens_within_1500ms'] and not x['errors'] for x in results),'Start must open the garden even when audio or storage never settles'
if __name__=='__main__':main()
