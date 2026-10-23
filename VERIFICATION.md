# Verification — Reading Garden

## Result and scope

Built `index.html` as a self-contained game with inline CSS/JS/SVG/emoji. The hosted installation includes a same-origin service worker, manifest and icons for reliable offline reopening. Code is published at https://github.com/Wailiam898/reading-garden ; game at https://wailiam898.github.io/reading-garden/ .

No real child's name, microphone recordings, learning history or drawings are shipped in the source. Test data is confined to isolated browser contexts. Hosting is public; device data is not uploaded by the app.

## Content audit

`node tools/audit.cjs` checks the **built HTML's** curriculum matches source and validates every printed word's explicit grapheme segmentation, cumulative set availability, canonical digraph/double-letter parsing and picture presence. It checks every sentence/book/title token against the cumulative regular-word dictionary or the separately introduced heart-word list.

- **96 regular-word entries** (includes the decodable character name Pat separately from the action pat).
- **9 decodable sentences**.
- **8 books, 4 pages each: 32 pages**.
- **8 explicit heart words**: I, the, to, no, go, is, he, she.
- **No violations reported** in the final audit.

Phonetic design checks also cover voiced/unvoiced th, avoiding same-sound distractors (c/k/ck, s/ss, f/ff, l/ll), treating x/qu as two phoneme boxes, and keeping consonant-cluster words in the final stage. This is a structural audit, not an independent expert linguistic review or proof that every emoji is unambiguous. Spoken-only listening vocabulary, instructions, menus and adult text are outside the decodability constraint.

## Automated verification

**13 Node tests pass**: curriculum, individual teaching gates, separate-session mastery, helped-answer exclusion, mistakes/accuracy, genuine book gates, school-start behaviour, sound alternatives, phoneme-box counts, final cluster-book gate, local-voice selection, phoneme fallback safety, audio cancellation and offline worker behaviour (several assertions per test).

Headless **Google Chrome**, Playwright, isolated iPhone-size **390×844** and iPad-size **820×1180** contexts with touch/mobile flags and Reduce Motion:

- First launch and spoken-play controls.
- All six starter-sound introductions through hear/trace/match/make, including deliberate wrong choices and gentle highlighting.
- Complete six-question Sound Hunt with mistakes; hearing the sound is required before answering.
- Guided blending followed by an independent turn; first-word show-a-grown-up screen.
- Complete four-question Build It round with guided/independent turns and incorrect tiles.
- Both starter heart-word lessons and sentence-picture matching with an error.
- A book **earned from explicitly seeded near-mastery history in an earlier session**, then a four-page read-through and first-book celebration. This is a fixture for gate testing, not a claim that child learning was observed.
- Sticker book, drawing stamp, short-tap rejection and successful press-and-hold grown-up entry.
- Settings changed and downstream name/set/session values verified, not merely that controls exist.
- **Actual MediaRecorder API** with Chrome's fake microphone: nonempty recording, playback invocation, IndexedDB persistence after reload.
- Offline cold page reopening and persistence of names/progress/recordings through the service-worker shell.
- Child button dimensions ≥64px and no horizontal page overflow.
- Session-end condition exercised with a shortened test threshold, not a ten-minute child trial.
- **No captured JavaScript exceptions or console errors** in either full flow.

Additional edge tests: blocked localStorage/IndexedDB leaves playable unsaved mode at **320px** width; leaving grown-up recording stops microphone tracks.

Screenshots of phone/tablet home, Sound Hunt, book, recording dashboard and session end were generated. Phone home/book/recorder and tablet Sound Hunt were visually reviewed: no clipped text, overlaps or serious layout faults. Garden path overflow is intentional horizontal scrolling.

Raw local evidence (not public child data): `test-results/browser-results.json`, `edge-results.json`, `curriculum-audit.json`, `word-list.csv`, and screenshots.

## Important limits and next check

- **No physical iPhone/iPad was available.** iOS Safari audio unlocking, actual voice availability, microphone permissions/codecs, Home Screen installation and Airplane Mode must be tested on the real devices. Emulated sizes do not verify iOS.
- The recorded test audio is synthetic fake-microphone audio, **not a human pure phoneme**. A parent must record and listen to real sounds. Playback was invoked programmatically; no human auditory quality assessment is claimed.
- On-device voice preference is Australian English when available, then British, then another downloaded English voice. The test machine used a local US English voice; an Australian voice was not installed there. Unit tests verify Australian preference without claiming real Australian speech was heard.
- Without a downloaded local voice, a grown-up must read the prompts. Without recordings, whole-word hooks are a temporary co-play fallback, not pure-sound instruction.
- The exact mastery thresholds, target success rate, sticker schedule and session/round durations are heuristics. No efficacy, reading-age gain or guaranteed child engagement is claimed. Round duration is untimed and depends on co-play.
- Single-file download is self-contained for game content; durable hosted offline reopening requires `sw.js`. This unavoidable browser constraint is explained rather than hidden behind a nonfunctional blob-worker trick.
- Progress is device/browser-specific and subject to clearing/eviction. There is no cloud sync or permanent backup.

**Recommended acceptance trial:** install from Safari on the actual iPhone, record s/a/t, play one listening/phonics round with her, then reopen in Airplane Mode. Note any confusing pictures, voice or tracing instructions before extending content.
