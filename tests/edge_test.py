from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
def main():
    checks=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,channel='chrome')
        ctx=browser.new_context(viewport={'width':320,'height':740})
        page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        ctx.add_init_script('''Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}});Object.defineProperty(window,'indexedDB',{get(){throw new DOMException('Blocked','SecurityError')}});''')
        page.goto('http://127.0.0.1:8799/');page.locator('[data-act=start]').click()
        page.locator('[data-act=meet]').wait_for(timeout=8000)
        assert 'storage' in page.locator('body').inner_text().lower()
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
        checks.append('blocked device storage degrades to playable unsaved mode');assert not errors,errors;ctx.close()
        browser.close()
    (ROOT/'test-results/edge-results.json').write_text(json.dumps(checks,indent=2))
if __name__=='__main__':main()
