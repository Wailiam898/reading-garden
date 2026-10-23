# Reading Garden — evidence and design decisions

## What the evidence supports
- Explicit, systematic teaching of phonemic awareness and letter–sound relationships, repeated decoding, and attention to vocabulary and comprehension.[1]
- Linking speech sounds to print, blending from left to right, word building, regular/irregular word instruction, and connected-text practice. The WWC rates its sound/letter and decoding recommendations strong; connected text moderate.[2]
- Revisiting knowledge over separate lessons with timely corrective feedback supports retention.[4]
- Play, manageable challenge, agency, adult interaction and process-focused praise inform the social design. Harvard cautions against unnecessary incentives; stickers here are small acknowledgments, not purchases or variable-ratio prizes.[3][6]

## Product choices, not proven prescriptions
The exact sound order is a Letters-and-Sounds-like sequence requested by the parent, not an assertion that every Australian school uses this order. School alignment must be checked with the child's teacher. The 85–90% success aim, mastery thresholds, question counts, sticker frequency and 5–10 minute session limit are adjustable design heuristics. This particular app has not been evaluated for literacy outcomes. Repeated taps or correct picture choices do not prove independent oral reading. A grown-up should listen to her decoding; this is a supplement to teaching and rich shared reading, not an assessment or replacement.

Pictures supply meaning after decoding, rather than encouraging picture/first-letter guessing. Spoken-only listening warm-ups and adult instructions may include vocabulary outside the printed decodable sequence; the decodability audit applies to child reading/spelling content, not ordinary spoken language.

## Audio and technical boundaries
Browser TTS is used for whole words, sentences and instructions, never generated isolated phonemes or letter names. Device-recorded sounds need a grown-up to check purity and volume. A mnemonic whole word is not a substitute for a pure phoneme. Offline speech depends on a locally installed system voice; recording sounds does not by itself guarantee instruction speech while offline.

Reliable offline HTTP(S) reopening requires a same-origin service-worker JavaScript file served over HTTPS (or localhost for testing); it cannot be registered from a data/blob URL. Therefore the downloadable HTML is self-contained but the installable hosted edition also ships a small worker/manifest/icons.[5] Device browser data may be cleared or evicted, so progress/recordings must never be described as permanent or synced.

## Sources

[1] https://www.edresearch.edu.au/summaries-explainers/explainers/introduction-science-reading
[2] https://ies.ed.gov/ncee/wwc/practiceguide/21
[3] https://developingchild.harvard.edu/resources/handouts-tools/brainbuildingthroughplay
[4] https://www.edresearch.edu.au/guides-resources/practice-guides/spacing-and-retrieval-practice-guide-full-publication
[5] https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register
[6] https://developingchild.harvard.edu/resources/briefs/how-to-motivate-children-science-based-approaches-for-parents-caregivers-and-teachers
