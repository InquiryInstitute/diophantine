# Enable GitHub Pages - Quick Fix

The 404 error is because GitHub Pages needs to be enabled manually the first time.

## Quick Fix (2 minutes)

1. **Go to Settings**: https://github.com/InquiryInstitute/diophantine/settings/pages

2. **Under "Source"**, select: **"GitHub Actions"** (not "Deploy from a branch")

3. **Click Save**

That's it! The next workflow run will deploy your site.

## Alternative: Enable via GitHub CLI

If you have the right permissions, you can also run:

```bash
gh api repos/InquiryInstitute/diophantine/pages \
  -X POST \
  -f source[type]=branch \
  -f source[branch]=main \
  -f source[path]=/ \
  -f build_type=workflow
```

## After Enabling

Once enabled, the site will be available at:
- **https://inquiryinstitute.github.io/diophantine/**

The workflow will automatically deploy on the next push or workflow run.

## Verify It's Working

1. Go to: https://github.com/InquiryInstitute/diophantine/actions
2. Look for "Deploy GitHub Pages" workflow
3. It should complete successfully after Pages is enabled

---

**Note**: The workflow has been updated to automatically enable Pages if possible, but manual enablement is still the most reliable method.
