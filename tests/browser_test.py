"""Real Chromium acceptance flow; fake microphone is labelled test audio, not a phoneme."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json, os
ROOT=Path(__file__).resolve().parents[1]
def main():
    assert (ROOT/'index.html').exists(), 'Game HTML must exist before acceptance play-through'
    results=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,channel='chrome',args=['--use-fake-device-for-media-stream','--use-fake-ui-for-media-stream'])
        for name, viewport in [('iphone',{'width':390,'height':844}),('ipad',{'width':820,'height':1180})]:
            ctx=browser.new_context(viewport=viewport,is_mobile=True,has_touch=True,device_scale_factor=1,permissions=['microphone'],reduced_motion='reduce')
            page=ctx.new_page();errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
            page.goto(os.environ.get('GAME_URL','http://127.0.0.1:8799/'))
            page.locator('[data-act="start"]').click()
            assert page.locator('[data-act="repeat"]').is_visible()
            page.locator('[data-act="meet"]').wait_for(state='visible')
            assert page.locator('[data-act="meet"]').is_visible()
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'no horizontal overflow'
            (ROOT/'test-results').mkdir(exist_ok=True)
            page.screenshot(path=str(ROOT/f'test-results/{name}-garden.png'),full_page=True)
            # Teach all six starter sounds through the real child UI.
            for idx in range(6):
                page.locator('[data-act="meet"]').click()
                page.locator('[data-act="meet-hear"]').click()
                page.locator('[data-act="trace-tap"]').click()
                page.locator('[data-act="meet-next"]').click()
                if idx==0:
                    page.locator('[data-act="meet-answer"][data-correct="false"]').click()
                    assert page.locator('[data-act="meet-answer"][data-correct="true"]').evaluate('(e)=>e.classList.contains("help")')
                page.locator('[data-act="meet-answer"][data-correct="true"]').click()
                page.locator('[data-act="meet-answer"][data-correct="true"]').click()
                assert page.evaluate('G.state.taught.length')==idx+1
                page.locator('[data-act="home"]').first.click()
            page.locator('[data-act="hunt"]').click()
            page.screenshot(path=str(ROOT/f'test-results/{name}-hunt.png'),full_page=True)
            before=page.evaluate('JSON.stringify(G.state.stats)')
            page.locator('[data-act="answer"][data-correct="true"]').click()
            assert page.evaluate('JSON.stringify(G.state.stats)')==before, 'cannot answer without hearing the sound prompt'
            for idx in range(6):
                page.locator('[data-act="target-sound"]').click()
                if idx==1:
                    page.locator('[data-act="answer"][data-correct="false"]').first.click()
                    assert page.locator('[data-act="answer"][data-correct="true"]').evaluate('(e)=>e.classList.contains("help")')
                page.locator('[data-act="answer"][data-correct="true"]').click()
                page.locator('[data-act="next"]').click()
            assert page.evaluate('G.screen')=='celebrate'
            page.locator('[data-act="home"]').first.click()
            page.locator('[data-act="blend"]').click()
            page.locator('[data-act="word-model"]').click()
            page.locator('[data-act="word-we"]').click()
            for button in page.locator('[data-act="part"]').all():button.click()
            page.locator('[data-act="blend-arrow"]').click()
            page.locator('[data-act="answer"][data-correct="true"]').click()
            assert page.evaluate('G.round.mode')=='independent', 'guided blending must lead to an independent attempt'
            for button in page.locator('[data-act="part"]').all():button.click()
            page.locator('[data-act="blend-arrow"]').click()
            page.locator('[data-act="answer"][data-correct="false"]').first.click()
            page.locator('[data-act="answer"][data-correct="true"]').click()
            assert page.evaluate('G.state.firstWord')
            page.locator('[data-act="first-word"]').click()
            assert page.evaluate('G.screen')=='proud'
            page.locator('[data-act="home"]').first.click()
            # Build a complete round, including guided and independent versions.
            page.locator('[data-act="build"]').click()
            for question in range(4):
                if page.locator('[data-act="word-model"]').count():
                    page.locator('[data-act="word-model"]').click()
                    page.locator('[data-act="word-we"]').click()
                for step in range(12):
                    if page.locator('[data-act="next"]').count():break
                    if page.locator('[data-act="word-you"]').count():
                        page.locator('[data-act="word-you"]').click();continue
                    if step==0:
                        wrong=page.locator('[data-act="tile"][data-correct="false"]')
                        if wrong.count():wrong.first.click()
                    page.locator('[data-act="tile"][data-correct="true"]').click()
                page.locator('[data-act="next"]').click()
            assert page.evaluate('G.screen')=='celebrate'
            page.locator('[data-act="home"]').first.click()
            # Teach both initial heart words through hear/match/make.
            for _ in range(2):
                page.locator('[data-act="hearts"]').click()
                page.locator('[data-act="heart-hear"]').click()
                page.locator('[data-act="heart-match"]').click()
                page.locator('[data-act="heart-answer"][data-correct="true"]').click()
                for part in range(3):
                    if page.evaluate('G.screen')=='celebrate':break
                    page.locator('[data-act="heart-tile"][data-correct="true"]').click()
                page.locator('[data-act="home"]').first.click()
            assert page.evaluate('G.state.hearts.length')==2
            page.locator('[data-act="read"]').click()
            for button in page.locator('[data-act="read-word"]').all():button.click()
            page.locator('[data-act="read-check"]').click()
            page.locator('[data-act="sentence-answer"][data-correct="false"]').click()
            page.locator('[data-act="sentence-answer"][data-correct="true"]').click()
            page.locator('[data-act="home"]').first.click()
            # Near-mastery fixture is explicit test history, not a bypass in the child UI.
            page.evaluate('''() => {let s=G.C.fresh();s.session=2;s.stage=0;s.taught=G.D.sets[0].sounds.slice();s.hearts=['I','the'];for(let id of s.taught){for(let i=0;i<(id==='s'?5:7);i++)G.C.record(s,'sound:'+id,true,false);s.stats['sound:'+id].sessions=id==='s'?[1]:[1,2];}G.replaceState(s);G.home();Math.random=()=>.001;}''')
            assert not page.evaluate('G.C.bookReady(G.D.books[0],G.state)')
            page.locator('[data-act="hunt"]').click()
            assert page.evaluate('G.round.target')=='s'
            page.locator('[data-act="target-sound"]').click()
            page.locator('[data-act="answer"][data-correct="true"]').click()
            assert page.evaluate('G.C.bookReady(G.D.books[0],G.state)')
            page.locator('[data-act="home"]').first.click()
            page.locator('[data-act="library"]').click()
            page.locator('[data-act="book"][data-index="0"]').click()
            page.screenshot(path=str(ROOT/f'test-results/{name}-book.png'),full_page=True)
            for _ in range(4):
                page.locator('[data-act="book-together"]').click()
                page.locator('[data-act="book-next"]').click()
            assert page.evaluate('G.state.books.includes("book0")')
            page.locator('[data-act="first-book"]').click()
            assert page.evaluate('G.screen')=='proud'
            page.locator('[data-act="home"]').first.click()
            page.locator('[data-act="stickers"]').click()
            assert page.locator('.sticker').count()>0
            page.locator('[data-act="home"]').first.click()
            page.locator('[data-act="room"]').click()
            page.locator('[data-act="stamp"]').click()
            assert page.evaluate('G.state.draw.length')==1
            page.locator('[data-act="home"]').first.click()
            # Short tap cannot open grown-up controls; a real hold can.
            page.locator('[data-act="gate"]').click()
            assert page.evaluate('G.screen')!='adult'
            gate=page.locator('[data-act="gate"]').bounding_box()
            page.mouse.move(gate['x']+30,gate['y']+30);page.mouse.down();page.wait_for_timeout(1900);page.mouse.up()
            assert page.evaluate('G.screen')=='adult'
            page.locator('#child-name').fill('Test Reader')
            page.locator('#start-set').select_option('1')
            page.locator('#session-minutes').select_option('5')
            page.locator('[data-act="save-settings"]').click()
            assert page.evaluate('G.state.settings.minutes')==5
            assert page.evaluate('G.state.stage')==1
            assert page.evaluate('G.state.child')=='Test Reader'
            page.locator('#record-sound').select_option('s')
            page.locator('[data-act="record-start"]').click()
            page.wait_for_function('document.querySelector("#record-status").textContent.startsWith("Recording")')
            page.wait_for_timeout(650)
            page.locator('[data-act="record-stop"]').click()
            page.wait_for_function('G.A.has("s")')
            clip_size=page.evaluate('G.A.size("s")')
            assert clip_size>0
            page.locator('[data-act="record-play"]').click()
            page.screenshot(path=str(ROOT/f'test-results/{name}-recording.png'),full_page=True)
            # All visible child controls have 64px targets; record tool uses native select/input too.
            page.locator('[data-act="home"]').first.click()
            assert page.evaluate('Array.from(document.querySelectorAll("button")).every(e=>{let r=e.getBoundingClientRect();return r.width>=63.5&&r.height>=63.5})')
            await_ready='navigator.serviceWorker.ready.then(()=>true)'
            page.evaluate(await_ready)
            page.reload();page.locator('[data-act="start"]').click();page.locator('[data-act="meet"]').wait_for()
            assert page.evaluate('G.state.child')=='Test Reader'
            assert page.evaluate('G.A.has("s")')
            # Cold offline navigation uses the companion worker, not the HTTP cache.
            ctx.set_offline(True)
            page.reload();page.locator('[data-act="start"]').click();page.locator('[data-act="meet"]').wait_for()
            assert page.evaluate('G.state.child')=='Test Reader'
            assert page.evaluate('G.A.size("s")')==clip_size
            ctx.set_offline(False)
            # Shortened clock threshold exercises the real built-in session-end condition.
            page.evaluate('G.state.settings.minutes=.0001')
            page.wait_for_function('G.screen==="end"',timeout=10000)
            page.screenshot(path=str(ROOT/f'test-results/{name}-end.png'),full_page=True)
            assert not errors, errors
            results.append({'device':name,'viewport':viewport,'checks':['first launch','six sound introductions','gentle mistakes','complete hunt round','blend guided then independent','complete build round','heart words','sentence','earned book unlock from prior-session fixture','four-page book','first-book celebration','stickers','drawing','hold gate','settings downstream effects','MediaRecorder save and playback','recording persists after reload','offline reopen','64px child targets','session end'],'recorded_fake_audio_bytes':clip_size,'errors':errors})
            assert not errors, errors
            ctx.close()
        browser.close()
    (ROOT/'test-results/browser-results.json').write_text(json.dumps(results,indent=2))
if __name__=='__main__':main()
