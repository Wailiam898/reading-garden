const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
test('offline worker installs same-scope shell and handles offline navigation',async()=>{
 const file=path.join(__dirname,'../sw.js');
 assert.ok(fs.existsSync(file),'offline worker must exist');
 const listeners={},items=new Map(),added=[];
 const cache={addAll:async urls=>{added.push(...urls);for(const u of urls)items.set(new URL(u,'https://example.org/reading-garden/').href,{ok:true,marker:u});},match:async r=>items.get(typeof r==='string'?new URL(r,'https://example.org/reading-garden/').href:r.url),put:async()=>{}};
 const box={URL,Response,console,self:{registration:{scope:'https://example.org/reading-garden/'},location:{origin:'https://example.org'},addEventListener:(name,fn)=>listeners[name]=fn,skipWaiting:async()=>{},clients:{claim:async()=>{}}},caches:{open:async()=>cache,match:cache.match,keys:async()=>[],delete:async()=>true},fetch:async()=>{throw new Error('offline')}};
 vm.runInNewContext(fs.readFileSync(file,'utf8'),box);
 let job; listeners.install({waitUntil:p=>job=p});await job;
 assert.ok(added.some(u=>u.endsWith('index.html')),'HTML shell cached');
 assert.ok(added.every(u=>new URL(u,'https://example.org/reading-garden/').pathname.startsWith('/reading-garden/')),'never cache outside app scope');
 let response;listeners.fetch({request:{method:'GET',mode:'navigate',url:'https://example.org/reading-garden/?from=home'},respondWith:p=>response=p});
 assert.ok((await response).ok,'offline navigation returns cached page');
 let intercepted=false;listeners.fetch({request:{method:'GET',mode:'cors',url:'https://tracking.invalid/ad.js'},respondWith:()=>intercepted=true});assert.equal(intercepted,false,'ignore other origins');
});
