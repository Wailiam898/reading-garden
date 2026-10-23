from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
def main():
    checks=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,channel='chrome',args=['--use-fake-device-for-media-stream','--use-fake-ui-for-media-stream'])
        ctx=browser.new_context(viewport={'width':320,'height':740})
        page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        ctx.add_init_script('''Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}});Object.defineProperty(window,'indexedDB',{get(){throw new DOMException('Blocked','SecurityError')}});''')
        page.goto('http://127.0.0.1:8799/');page.locator('[data-act=start]').click()
        page.locator('[data-act=meet]').wait_for(timeout=8000)
        assert 'storage' in page.locator('body').inner_text().lower()
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        checks.append('blocked device storage degrades to playable unsaved mode');assert not errors,errors;ctx.close()
        ctx=browser.new_context(permissions=['microphone']);page=ctx.new_page()
        ctx.add_init_script('''const original=navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices);navigator.mediaDevices.getUserMedia=async opts=>{let stream=await original(opts);window.testStream=stream;return stream;};''')
        page.goto('http://127.0.0.1:8799/');page.locator('[data-act=start]').click();page.locator('[data-act=meet]').wait_for();page.evaluate('G.adult()')
        page.locator('[data-act=record-start]').click();page.wait_for_function('window.testStream && window.testStream.getTracks().some(t=>t.readyState==="live")')
        page.locator('[data-act=home]').first.click();page.wait_for_timeout(500)
        assert page.evaluate('window.testStream.getTracks().every(t=>t.readyState==="ended")'), 'microphone must stop when leaving grown-up recorder'
        checks.append('leaving recorder stops microphone tracks');ctx.close()
        browser.close()
    (ROOT/'test-results/edge-results.json').write_text(json.dumps(checks,indent=2))
if __name__=='__main__':main()
