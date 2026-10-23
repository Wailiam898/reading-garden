# Bunny's Reading Garden

A warm, tap-first phonics game to play **with a grown-up**. The child does not need to read menus or use a keyboard. Default friend: Pip the bunny; bunny/dinosaur/cat and names can be changed locally. No real child's name is embedded in the published source.

## Play and install

Hosted address: https://wailiam898.github.io/reading-garden/

1. Open the address in **Safari** on an iPhone or iPad, online.
2. Tap **Tap to start** and allow spoken instructions. Turn up the volume.
3. Share → **Add to Home Screen** → Add. Launch the new icon once while online.
4. Hold the top-right **leaf for two seconds** to open grown-up controls.
5. Set the child/mascot name and school starting set. Record pure sounds there. Begin with s a t p i n; say sounds, not letter names, and do not add an “uh”.
6. Confirm “Offline shell: ready”, then try reopening in Airplane Mode. Instructions need a downloaded on-device English voice. Australian English is preferred when installed, then British English, then another local English voice.

If silent, check the device volume and downloaded voices in Accessibility / Spoken Content (or Read & Speak, depending on iOS). Press the speaker to repeat. Without a local English voice, the app explicitly asks a grown-up to read the prompts; it does not switch to a cloud voice. Unrecorded sounds use a whole example-word clue, not a synthesised letter name or claimed pure phoneme.

## What is included

- Eight cumulative stages: s a t p i n; m d g o c k; ck e u r; h b f l; ss ff ll; j v w x y z qu; sh ch th ng (both th pronunciations); CCVC/CVCC.
- Meet/trace, Sound Hunt, Blend It, Build It with sound boxes, listening/rhyme/first-sound/syllable games, sentences, heart-word hear/match/make lessons, and eight four-page mini books.
- Hear → match → make; model → guide → independent practice; gentle correction and extra review of weak/overdue items.
- A garden path, predictable stickers, dress-up/colouring/drawing, first-word/book show-a-grown-up screens, and a gentle 5/7/10-minute session end.
- A hold-gated dashboard, settings, explicit school alignment, MediaRecorder capture saved in IndexedDB and progress in localStorage.
- At least 64px child buttons, portrait phone/tablet layout and Reduce Motion support.

## Honest boundaries

**Single-file / offline trade-off:** `index.html` contains all game logic, CSS and illustrations and can be downloaded by itself. Reliable offline **reopening from a hosted Home Screen app** needs the companion `sw.js` on the same HTTPS origin; the hosted edition also supplies a manifest and app icons. Blob/data service workers do not solve this. The game makes no analytics, advertising, font or third-party API requests. Initial shell installation fetches its own same-origin files; adult research links open only when deliberately tapped.

**Privacy:** names, progress, drawings and recordings are stored locally in this browser. The app does not upload them or sync devices. Browser/OS data clearing, storage eviction and device migration can affect them. This is not permanent backup. The public GitHub host has its own ordinary web-server logging; “no app tracking” does not mean the hosting provider sees no HTTP requests.

**Learning:** the evidence supports instructional principles, not this app's efficacy. The app has not been studied with children. 85–90% success is an aim, not a guarantee. Mastery thresholds, review weights and session lengths are product heuristics. Modelled/helped answers do not count as independent first-try responses; taps/picture answers do **not** prove independent oral reading. There is no speech recognition or automated diagnosis. Listen to her decoding and coordinate with school. More books, pictures and themes can be added after a real-device co-play trial.

**Stories:** to remain decodable, the mascot plays a bunny named **Pat** in every story even if a different display name/animal is chosen. Pictures are emoji/SVG and vary by device. They convey meaning but may need naming by a grown-up. Finger tracing is encouragement, not validated handwriting assessment. No speed score or time pressure is used even in familiar-sound rounds. Rounds are untimed; actual duration depends on co-play and may be shorter/longer than 2–4 minutes.

**Audio:** a whole-word fallback is not a pure phoneme. A parent must record and check pure phonemes and pronunciation. x and qu are consonant combinations /ks/ and /kw/, spanning two sound boxes with one spelling tile; other digraph/double-letter teams occupy one sound box. No phoneme is generated from a lone-letter TTS utterance.

## Development and verification

`src/` contains editable source fragments. `tools/build.py` assembles the downloadable self-contained HTML. No build step is needed to play the published game.

```
python tools/build.py
node --test tests/core.test.cjs tests/audio.test.cjs tests/offline.test.cjs
node tools/audit.cjs
```

The browser tests use Python Playwright with **real headless Chrome**, isolated contexts, phone/tablet viewport emulation and fake microphone audio. Start a loopback server on port 8799, then:

```
python -m http.server 8799 --bind 127.0.0.1
# separate terminal, using a Python environment with Playwright:
python tests/browser_test.py
python tests/edge_test.py
```

`GAME_URL` can point the full browser flow at the published HTTPS site. The tests seed **explicit prior-session history** to exercise earning a book unlock; they do not claim that hours of child learning occurred. Recording verification uses a fake microphone tone and checks nonempty persisted bytes/playback initiation; it does not verify a human phoneme or physical iPhone microphone. Session-end tests shorten the threshold. Screenshots are reviewed separately.

See [design evidence](research/DESIGN-EVIDENCE.md) and [verification report](VERIFICATION.md). Physical iOS Safari audio, microphone permission, Home Screen installation and Airplane Mode must still be checked on the actual devices. Chrome viewport emulation is not an iOS test.
