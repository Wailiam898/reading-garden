# Start-button repair

## Publication approval
William explicitly approved publication in the current conversation. The earlier pending-approval account below is retained as investigation history; it is superseded by this approval. Publish only the startup fix, generated shell, regression test and this note. No device progress or recordings are cleared.

## Investigation and local verification history

William reported that tapping Start did not work. The previously published UI awaited `GardenAudio.unlock()` before calling `home()`. Unlock awaited AudioContext.resume(), then a zero-sample WAV HTMLMediaElement.play(), then IndexedDB opening. A media promise that never settles therefore stranded the launch screen; slow storage also delayed it. Normal desktop testing had not exercised pending startup promises.

Regression test `tests/start_test.py` was run against the published version in real Chrome and Playwright WebKit on Windows: normal/unavailable-audio cases passed, but never-settling media playback, never-settling audio resume and never-settling IndexedDB cases all failed to reach the garden within 1500ms in both engines. This reproduces a mechanism matching the symptom, not a claim to have inspected William's physical device.

Local fix: remove the empty-WAV priming step, start/resume WebAudio without awaiting it, open recording storage in the background, and navigate immediately within the Start tap. Duplicate Start handling is guarded. No device progress, recording, curriculum or settings are reset.

Verification after repair:
- 10/10 start scenarios pass (five each in Chrome and WebKit), no captured page exceptions.
- 13/13 existing Node tests pass.
- Curriculum audit: 96 words, 9 sentences, 8 books/32 pages, no violations.
- Full local phone/tablet Chrome flows and blocked-storage/microphone-lifecycle edge tests pass.
- Physical iOS remains unverified. Windows WebKit is not iPhone Safari.

Publication approval was requested via a precise action table and Yes/No clarification prompt. The prompt timed out with no answer. **No public commit/push/deployment has been made for this repair.** The live URL therefore remains the earlier version until approval.

Changed files: src/audio.js, src/ui.js, generated index.html and sw.js; new tests/start_test.py. Evidence: test-results/start-results.json. To verify locally: `GAME_URL=http://127.0.0.1:8799/ ENGINES=chromium,webkit .venv/Scripts/python.exe tests/start_test.py` with an owned loopback server running. After explicit publish approval, commit only this scoped fix/docs/test, push with gh-backed credential helper if Git credential manager hangs, check exact-head CI/Pages, compare served committed HTML bytes (normalise Windows CRLF), and rerun the startup regression against the live URL.
