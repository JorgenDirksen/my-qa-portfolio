# Bug Report: LinkedIn Profile Edit Causes Blank Page on Save

**Application:** LinkedIn (Web version)
**Environment:** 
- macOS Ventura 13.4
- Browser: Safari 16.5
- LinkedIn Profile: Edit mode

**Severity:** High (blocks user from updating profile)
**Priority:** High (core functionality broken)

**Preconditions:**
1. User is logged into LinkedIn.
2. User is on their own profile page.

**Steps to Reproduce:**
1. Click the "Edit" button on the profile introduction section.
2. In the "Skills" section, type a new skill (e.g., "SQL").
3. Click the blue "Save" button.

**Expected Result:**
- The pop-up edit window closes.
- The profile page refreshes normally, displaying the updated skill.
- User can continue browsing.

**Actual Result:**
- The entire browser tab refreshes.
- The page loads as completely **blank/white**.
- The URL remains `[linkedin.com/in/...](https://www.linkedin.com/in/gheorghi-dmitrenco-99a75b1a4/skills/edit/forms/next-action/add-another-skill/)`.
- No error message is displayed.
- The skill is **not saved**.
- User must manually reload the page or navigate away to recover.

**Reproducibility:** 5/5 (happens consistently)

**Notes:**
- Workaround: Adding skills via the "Add profile section" dropdown (not via the main "Edit" button) seems to work.
- This bug disrupts the primary user flow of profile maintenance.
- Tested on 02/04/2026.
