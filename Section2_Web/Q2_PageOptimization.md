# Question 2: Page Load Optimization

## Three Common Causes & Solutions

### 1. **Large Image Files**
**Problem:** Unoptimized images (10MB+ photos) slow download times.

**Solution:**
- Compress images using tools like TinyPNG or ImageOptim
- Use modern formats (WebP, AVIF) with fallbacks
- Implement lazy loading: `<img loading="lazy">`
- Use responsive images: `<picture>` or `srcset`

---

### 2. **Too Many HTTP Requests**
**Problem:** Loading 50+ separate CSS/JS files increases load time.

**Solution:**
- Bundle and minify CSS/JS files (Webpack, Vite, Parcel)
- Combine multiple small files into one
- Use HTTP/2 multiplexing
- Implement code splitting for large apps

---

### 3. **Blocking JavaScript**
**Problem:** Large JS files in `<head>` block page rendering.

**Solution:**
- Move scripts to bottom of `<body>`
- Use `async` or `defer` attributes:
```html
  <script src="app.js" defer></script>
```
- Remove unused JavaScript (tree shaking)
- Split critical vs non-critical JS

---

## Additional Optimizations
- Enable browser caching (Cache-Control headers)
- Use a CDN for static assets
- Minify HTML/CSS/JS
- Reduce server response time (upgrade hosting, optimize database queries)
- Enable Gzip/Brotli compression
