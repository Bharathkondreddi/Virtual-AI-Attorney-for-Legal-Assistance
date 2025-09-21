# Email Service Setup Guide

## Option 1: Formspree (Recommended - Free and Easy)

1. Go to https://formspree.io
2. Sign up with your email
3. Create a new form
4. Set the target email to: bk2982689@gmail.com
5. Copy the form endpoint (looks like: https://formspree.io/f/xpzgvnag)
6. Replace the URL in the code

## Option 2: EmailJS (Alternative)

1. Go to https://emailjs.com
2. Sign up and create a service
3. Connect your Gmail account
4. Create an email template
5. Get your service ID, template ID, and public key

## Option 3: Simple Email Forwarding

For immediate testing, you can:
1. Create a simple HTML form that posts to a webhook
2. Use services like Zapier or IFTTT to forward emails
3. Set up a simple serverless function (Vercel, Netlify)

## Current Implementation

The forms currently use a fallback system:
- Try to send via webhook service
- If that fails, show mailto links and WhatsApp
- Provide direct contact information

## To Activate Email Sending:

1. Choose Option 1 (Formspree) - it's the easiest
2. Create account and form at formspree.io
3. Update the formspree_url in both home.py and about.py
4. Deploy the changes

## Testing:

1. Fill out the form on your deployed app
2. Check your Gmail inbox at bk2982689@gmail.com
3. Verify the email contains all form data