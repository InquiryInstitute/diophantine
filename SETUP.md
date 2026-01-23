# GitHub Repository Setup Instructions

This document provides step-by-step instructions to push this repository to GitHub and enable GitHub Pages.

## Prerequisites

- Git installed and configured
- GitHub account
- Access to create repositories in the `InquiryInstitute` organization (or your own account)

## Step 1: Create the GitHub Repository

1. Go to https://github.com/organizations/InquiryInstitute/repositories/new
   - Or: https://github.com/new (if using personal account)

2. Repository settings:
   - **Repository name**: `diophantine`
   - **Description**: "One Constraint to Bind Them: A Diophantine Lens on a Combinatorial Artifact"
   - **Visibility**: Public (required for GitHub Pages on free tier)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)

3. Click "Create repository"

## Step 2: Add Remote and Push

Run these commands in your terminal (from the diophantine directory):

```bash
cd /Users/danielmcshan/GitHub/diophantine

# Add the remote (replace with your actual GitHub URL)
git remote add origin https://github.com/InquiryInstitute/diophantine.git

# Or if using SSH:
# git remote add origin git@github.com:InquiryInstitute/diophantine.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

### Option A: Using GitHub Actions (Recommended)

The repository already includes a GitHub Actions workflow (`.github/workflows/pages.yml`) that will automatically build and deploy the Jekyll site.

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under "Source", select **GitHub Actions**
4. The workflow will automatically run on the next push

### Option B: Using Jekyll (Legacy)

If you prefer the legacy method:

1. Go to **Settings** → **Pages**
2. Under "Source", select **Deploy from a branch**
3. Select branch: `main`
4. Select folder: `/ (root)`
5. Click **Save**

## Step 4: Verify Deployment

1. After pushing, wait 1-2 minutes for GitHub Actions to complete
2. Go to **Actions** tab to see the workflow status
3. Once complete, your site will be available at:
   - `https://inquiryinstitute.github.io/diophantine/`
   - Or: `https://[your-username].github.io/diophantine/` (if personal account)

## Step 5: Update Base URL (if needed)

If your repository is in a personal account or different organization:

1. Edit `_config.yml`
2. Update the `baseurl` and `url` fields:
   ```yaml
   baseurl: "/diophantine"  # Keep this if repo name is "diophantine"
   url: "https://[your-org-or-username].github.io"
   ```

## Troubleshooting

### Jekyll build fails
- Check the Actions log for errors
- Ensure `Gemfile` is present and correct
- Ruby version may need adjustment in `.github/workflows/pages.yml`

### Pages not updating
- Clear browser cache
- Check that GitHub Actions workflow completed successfully
- Verify `_config.yml` settings

### Math equations not rendering
- Jekyll's default markdown processor may need MathJax
- Consider adding a MathJax script to `_includes/head.html` or using a Jekyll theme that supports math

## Next Steps

- Customize the Jekyll theme in `_config.yml`
- Add more pages or collections
- Update the README with repository-specific information
- Add badges, contributors, etc.

---

For questions, see the [GitHub Pages documentation](https://docs.github.com/en/pages).
