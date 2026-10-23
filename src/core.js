/* Core curriculum and learning model. No browser dependencies. */
'use strict';
const GardenCore=(()=>{
const sets=[['s','a','t','p','i','n'],['m','d','g','o','c','k'],['ck','e','u','r'],['h','b','f','l'],['ss','ff','ll'],['j','v','w','x','y','z','qu'],['sh','ch','th','thv','ng'],[]].map((sounds,i)=>({sounds,title:['First friends','Meadow friends','Pond friends','Woodland friends','Double-letter friends','Adventure friends','Two-letter teams','Sound explorers'][i]}));
const soundRows=[
['s','s','snake','🐍','start','s'],['a','a','apple','🍎','start','æ'],['t','t','tap','🚰','start','t'],['p','p','pig','🐷','start','p'],['i','i','insect','🐞','start','ɪ'],['n','n','nest','🪺','start','n'],
['m','m','moon','🌙','start','m'],['d','d','dog','🐕','start','d'],['g','g','goat','🐐','start','ɡ'],['o','o','octopus','🐙','start','ɒ'],['c','c','cat','🐈','start','k'],['k','k','kite','🪁','start','k'],
['ck','ck','duck','🦆','end','k'],['e','e','egg','🥚','start','e'],['u','u','umbrella','☂️','start','ʌ'],['r','r','rabbit','🐇','start','ɹ'],['h','h','hat','👒','start','h'],['b','b','bat','🦇','start','b'],['f','f','fish','🐟','start','f'],['l','l','leaf','🍃','start','l'],
['ss','ss','kiss','😘','end','s'],['ff','ff','puff','💨','end','f'],['ll','ll','bell','🔔','end','l'],['j','j','jam','🍓','start','dʒ'],['v','v','van','🚐','start','v'],['w','w','web','🕸️','start','w'],['x','x','box','📦','end','ks'],['y','y','yak','🐂','start','j'],['z','z','zip','🤐','start','z'],['qu','qu','queen','👑','start','kw'],['sh','sh','shell','🐚','start','ʃ'],['ch','ch','chick','🐥','start','tʃ'],['th','th','thumb','👍','start','θ'],['thv','th','this','👉','start','ð'],['ng','ng','ring','💍','end','ŋ']];
const sounds=soundRows.map(([id,g,hook,pic,where,ipa])=>({id,g,hook,pic,where,ipa,set:sets.findIndex(s=>s.sounds.includes(id))}));
const words=[];function add(set,rows){for(const [text,parts,pic] of rows)words.push({text,parts:parts.split(' '),pic,set});}
add(0,[['sat','s a t','🐇🪑'],['pin','p i n','🧷'],['tap','t a p','🚰'],['pat','p a t','🐇🤚'],['nap','n a p','😴'],['pan','p a n','🍳'],['tin','t i n','🥫'],['pip','p i p','🍎🌱'],['sit','s i t','🪑'],['sip','s i p','🥤'],['in','i n','📥'],['it','i t','👉'],['at','a t','📍'],['Pat','p a t','🐇']]);
add(1,[['mat','m a t','🟫'],['cat','c a t','🐈'],['dog','d o g','🐕'],['pig','p i g','🐷'],['pot','p o t','🍲'],['dig','d i g','🪏'],['mop','m o p','🧹'],['cot','c o t','🛏️'],['can','c a n','🥫'],['cap','c a p','🧢'],['map','m a p','🗺️'],['on','o n','🔝'],['nod','n o d','🙂↕️'],['kid','k i d','🧒']]);
add(2,[['duck','d u ck','🦆'],['sock','s o ck','🧦'],['neck','n e ck','🦒'],['pack','p a ck','🎒'],['sun','s u n','☀️'],['run','r u n','🏃'],['cup','c u p','☕'],['rat','r a t','🐀'],['red','r e d','🔴'],['pet','p e t','🐈🤚'],['ten','t e n','👐'],['mud','m u d','🟤'],['up','u p','⬆️']]);
add(3,[['hat','h a t','👒'],['bat','b a t','🦇'],['hen','h e n','🐔'],['bed','b e d','🛏️'],['fan','f a n','🪭'],['leg','l e g','🦵'],['log','l o g','🪵'],['fun','f u n','🥳'],['hop','h o p','🐇⬆️'],['bag','b a g','👜'],['bun','b u n','🥖'],['hug','h u g','🤗']]);
add(4,[['kiss','k i ss','😘'],['hiss','h i ss','🐍💨'],['puff','p u ff','💨'],['cuff','c u ff','👕'],['bell','b e ll','🔔'],['hill','h i ll','⛰️'],['doll','d o ll','🪆'],['fill','f i ll','🫗']]);
add(5,[['jam','j a m','🍓'],['jet','j e t','🛩️'],['van','v a n','🚐'],['vet','v e t','🧑‍⚕️🐕'],['web','w e b','🕸️'],['wet','w e t','💦'],['box','b o x','📦'],['fox','f o x','🦊'],['yak','y a k','🐂'],['yes','y e s','👍'],['zip','z i p','🤐'],['quiz','qu i z','❓']]);
add(6,[['ship','sh i p','🚢'],['shop','sh o p','🏪'],['fish','f i sh','🐟'],['shell','sh e ll','🐚'],['chick','ch i ck','🐥'],['chin','ch i n','🙂👇'],['chop','ch o p','🪓'],['thin','th i n','🪡'],['thud','th u d','📦💥'],['ring','r i ng','💍'],['sing','s i ng','🎤']]);
add(7,[['frog','f r o g','🐸'],['jump','j u m p','🦘'],['hand','h a n d','✋'],['tent','t e n t','⛺'],['pond','p o n d','🏞️'],['nest','n e s t','🪺'],['milk','m i l k','🥛'],['stop','s t o p','🛑'],['drum','d r u m','🥁'],['flag','f l a g','🚩'],['swim','s w i m','🏊'],['clap','c l a p','👏']]);
const hearts=[
{text:'I',set:0,parts:['I'],odd:[0],pic:'🙋',note:'This word says I, like when you point to yourself. We remember this part by heart.'},
{text:'the',set:0,parts:['th','e'],odd:[0,1],pic:'❤️',note:'This word says the. These parts are not the sounds we have learned yet. Remember them by heart.'},
{text:'to',set:1,parts:['t','o'],odd:[1],pic:'➡️',note:'This word says to. The last part is a heart part. It does not use our short vowel sound.'},
{text:'no',set:1,parts:['n','o'],odd:[1],pic:'🙅',note:'This word says no. The last part is a heart part.'},
{text:'go',set:1,parts:['g','o'],odd:[1],pic:'🚦',note:'This word says go. The last part is a heart part.'},
{text:'is',set:1,parts:['i','s'],odd:[1],pic:'❤️',note:'This word says is. The last part is a buzzing heart part.'},
{text:'he',set:2,parts:['h','e'],odd:[0,1],pic:'👦',note:'This word says he. The last part is a heart part. The first sound is one we will learn soon; ask your grown-up.'},
{text:'she',set:2,parts:['sh','e'],odd:[0,1],pic:'👧',note:'This word says she. The first team is a sound we will learn later. The last part is a heart part.'}];
const sentences=[
{set:0,text:'I pat Pat.',pic:'🙋🤚🐇',other:'🙋🥤',heart:['I']},{set:0,text:'Pat sat.',pic:'🐇🪑',other:'🐇😴',heart:[]},
{set:1,text:'The cat sat on the mat.',pic:'🐈🟫',other:'🐕🛏️',heart:['the']},
{set:2,text:'The duck is in mud.',pic:'🦆🟤',other:'🐈🟫',heart:['the','is']},
{set:3,text:'Pat can hop.',pic:'🐇⬆️',other:'🐇🪑',heart:[]},
{set:4,text:'Pat is on the hill.',pic:'🐇⛰️',other:'🐇🛏️',heart:['is','the']},
{set:5,text:'The fox is wet.',pic:'🦊💦',other:'🐕☀️',heart:['the','is']},
{set:6,text:'The chick is in the shop.',pic:'🐥🏪',other:'🐟🚢',heart:['the','is']},
{set:7,text:'The frog can jump.',pic:'🐸⬆️',other:'🐸🪑',heart:['the']}];
const bookRows=[
['Pat',['I pat Pat.','Pat sat.','I tap.','Pat! Pat!'],['🙋🤚🐇','🐇🪑','🙋👆','🐇🤗']],
['The cat',['The cat sat.','Pat sat on the mat.','The dog sat.','Pat can dig.'],['🐈🪑','🐇🟫','🐕🪑','🐇🪏']],
['Mud',['Pat is in mud.','The duck is in mud.','The sun is up.','Pat can run.'],['🐇🟤','🦆🟤','☀️⬆️','🐇🏃']],
['Hop',['Pat can hop.','Pat can pat the hen.','The hen is on the log.','Pat can hug the dog.'],['🐇⬆️','🐇🤚🐔','🐔🪵','🐇🤗🐕']],
['The bell',['Pat is on the hill.','Pat can pat the doll.','The bell is in the bag.','Pat can kiss the doll.'],['🐇⛰️','🐇🤚🪆','🔔👜','🐇😘🪆']],
['The fox',['The fox is wet.','Pat is in the van.','The fox can hop in.','Pat can go.'],['🦊💦','🐇🚐','🦊🚐','🐇🚐➡️']],
['The ship',['Pat is on the ship.','The fish is red.','Pat can sing.','The chick can hop.'],['🐇🚢','🐟🔴','🐇🎤','🐥⬆️']],
['The pond',['Pat is at the pond.','The frog can jump.','Pat can clap.','The frog can swim.'],['🐇🏞️','🐸⬆️','🐇👏','🐸🏊']]];
const books=bookRows.map(([title,texts,pics],set)=>({id:'book'+set,set,title,pages:texts.map((text,i)=>({text,pic:pics[i]}))}));
const DATA={sets,sounds,words,hearts,sentences,books};
const tokenise=text=>text.match(/[A-Za-z]+/g)||[];
const wordFor=w=>words.find(x=>x.text.toLowerCase()===w.toLowerCase());
const soundFor=id=>sounds.find(x=>x.id===id);
function fresh(){return {version:1,child:'little reader',mascot:'Pip',animal:'bunny',taught:[],hearts:[],stats:{},school:0,stage:0,session:0,stickers:[],stars:0,outfit:'',colour:'#eee3ff',draw:[],books:[],firstWord:false,firstBook:false,settings:{sound:true,minutes:10},intro:{}};}
function allowedSounds(set){return sets.slice(0,set+1).flatMap(x=>x.sounds);}
function availableWords(s){return words.filter(w=>w.set<=s.stage&&w.parts.every(p=>s.taught.includes(p)));}
function canRead(text,s){return tokenise(text).every(w=>{let h=hearts.find(x=>x.text.toLowerCase()===w.toLowerCase());if(h)return s.hearts.some(x=>x.toLowerCase()===w.toLowerCase());let d=wordFor(w);return d&&d.set<=s.stage&&d.parts.every(x=>s.taught.includes(x));});}
function nextSound(s){return sounds.find(x=>x.set<=s.stage&&!s.taught.includes(x.id));}
function record(s,key,ok,helped=false){let st=s.stats[key]||(s.stats[key]={right:0,attempts:0,helped:0,sessions:[],last:0,recent:[]});if(helped){st.helped++;}else{st.attempts++;if(ok)st.right++;st.recent.push(ok?1:0);st.recent=st.recent.slice(-12);if(ok&&!st.sessions.includes(s.session))st.sessions.push(s.session);}st.last=Date.now();return st;}
function mastered(s,key){let t=s.stats[key];return !!(t&&t.right>=6&&t.sessions.length>=2&&t.recent.length>=6&&t.recent.reduce((a,b)=>a+b,0)/t.recent.length>=.85);}
function status(s,key){if(mastered(s,key))return 'mastered';let t=s.stats[key];if(t&&t.attempts>=3&&t.recent.reduce((a,b)=>a+b,0)/t.recent.length<.6)return 'tricky';return 'learning';}
function reviewWeight(s,key){let t=s.stats[key];if(!t)return 12;let age=(Date.now()-t.last)/86400000;return 1+Math.min(age,7)+(mastered(s,key)?0:5)+(t.attempts?4*(1-t.right/t.attempts):4);}
function chooseReview(s,items,key){return [...items].sort((a,b)=>reviewWeight(s,key(a))-reviewWeight(s,key(b))||0).reverse()[0];}
function huntPool(s,target){let t=soundFor(target);return s.taught.filter(id=>id===target||(soundFor(id).ipa!==t.ipa&&soundFor(id).g!==t.g));}
function soundSlots(w){return w.parts.flatMap((p,i)=>(p==='x'||p==='qu')?[{part:i,half:0},{part:i,half:1}]:[{part:i,half:0}]);}
function bookReady(b,s){return allowedSounds(b.set).every(id=>mastered(s,'sound:'+id))&&b.pages.every(p=>canRead(p.text,s))&&(b.set!==7||['frog','jump'].every(w=>mastered(s,'word:'+w)));}
function startAt(s,set){s.stage=Math.max(0,Math.min(7,Number(set)||0));s.school=s.stage;for(let id of allowedSounds(s.stage-1))if(!s.taught.includes(id))s.taught.push(id);}
function audit(){let errors=[];for(let w of words){let allowed=allowedSounds(w.set);if(!w.pic)errors.push(w.text+': missing picture');if(w.parts.map(p=>soundFor(p)?.g||'?').join('').toLowerCase()!==w.text.toLowerCase())errors.push(w.text+': spelling mismatch');if(w.parts.some(p=>!allowed.includes(p)))errors.push(w.text+': untaught sound');if(w.set<7&&w.parts.length>3)errors.push(w.text+': cluster before final set');const canonical=w.text.toLowerCase().match(/ck|ss|ff|ll|qu|sh|ch|th|ng|[a-z]/g);if(canonical&&canonical.join('|')!==w.parts.map(p=>soundFor(p)?.g).join('|'))errors.push(w.text+': noncanonical team');}
 const texts=[...sentences.map(p=>({...p,kind:'sentence'})),...books.flatMap(b=>b.pages.map(p=>({...p,set:b.set,kind:b.id}))),...books.map(b=>({text:b.title,set:b.set,pic:'📚',kind:'title'}))];for(let p of texts){if(!p.pic)errors.push(p.kind+': missing picture');for(let w of tokenise(p.text)){let h=hearts.find(h=>h.text.toLowerCase()===w.toLowerCase());if(h){if(h.set>p.set)errors.push(p.kind+' '+w+': early heart');}else {let d=wordFor(w);if(!d||d.set>p.set)errors.push(p.kind+' '+w+': unavailable word');}}}for(let h of hearts)if(!h.pic||h.parts.join('')!==h.text)errors.push(h.text+': heart mapping');return {words:words.length,sentences:sentences.length,books:books.length,pages:books.reduce((n,b)=>n+b.pages.length,0),errors};}
return {DATA,fresh,tokenise,wordFor,soundFor,soundSlots,huntPool,availableWords,canRead,nextSound,record,mastered,status,reviewWeight,chooseReview,bookReady,startAt,allowedSounds,audit};
})();
if(typeof module!=='undefined')module.exports=GardenCore;
