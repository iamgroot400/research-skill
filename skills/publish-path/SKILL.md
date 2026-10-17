---
name: publish-path
description: Finds and vets realistic places for a beginner or undergraduate to share and publish first research - preprint servers, undergraduate research journals, workshops, student conferences and symposia - and runs the checks that keep a student out of predatory venues. Covers authorship, mentor sign-off, AI-use disclosure and submission readiness. Use when the user asks "where can I publish", "which journal or conference", "arXiv", "is this journal legitimate", "can an undergrad publish", or before submitting.
---

# Publish path

Policies and deadlines change. **Verify every venue on its official page** and give the link. Mark anything you could not check as unverified. Never invent a venue, impact factor or acceptance rate.

## Venue types to consider

Rank by fit and realism for this paper, not by prestige:

1. **Preprint server** (for example arXiv for physics, math and statistics). Many require a subject-area endorsement for a first-time submitter, and the rules differ by category. Check the current policy and plan time to get endorsed, usually through a mentor. A preprint is public and permanent, so only post once the mentor has read the paper.
2. **Undergraduate research journals.** Peer-reviewed journals designed for student work, often with a faculty-mentor requirement. Check scope and the review process.
3. **Workshops** at established conferences, which often welcome early or small results.
4. **Student conferences and university symposia.** Good first presentations and feedback, even when the output is a poster or abstract, not a full paper.
5. **Field journals.** Possible for a strong, rigorous paper with a mentor's help, but with a slow and demanding review.

## Legitimacy checklist

For each candidate, answer yes/no/unknown with a link. Several "no"s means skip it:

- Is it run by a known society, university or established publisher?
- Is the editorial board real, named, and verifiable on the board members' own pages?
- Is the peer-review process described, and is the timeline realistic (not "accepted in 3 days")?
- Are the fees stated openly before submission, and do they make sense?
- Is it listed in a trusted index or directory (check the directory itself)?
- Did it contact you unprompted with flattering emails? That is a warning sign.
- Do the published papers look like real, reviewed work?

## Readiness checklist

Before submitting anywhere:

- The mentor has read and approved the paper, and agrees to be listed as appropriate.
- Authorship follows contribution. Everyone listed agreed, and nobody who contributed is left out.
- Every number and figure passes **qa-check**; code and data are in a repository or archive others can run.
- References are verified to exist and to say what the text claims.
- The venue's policy on AI-assisted work is read, and the use is disclosed in the form it requires.
- Formatting, length and anonymization rules are met (hand the checklist to **lab-ops**).
- The paper has not been submitted elsewhere in a way that breaks the venue's rules.

## Output

Write `lab/publish-path.md`: a ranked shortlist (3-5 venues) with link, scope fit, deadline, requirements, legitimacy results, and a recommended order of attempts (for example preprint after mentor review, then the best-fit journal or workshop). The student and mentor make the decision. Add real deadlines to `lab/deadlines.md`.
