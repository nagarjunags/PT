# Dynamic HTML Hierarchy Explorer

A lightweight, zero-dependency dashboard that allows you to directly open `index.html` in your browser and dynamically browse standalone HTML files arranged across any nested folder structure.

---

## 🚀 How to Use

You can open `index.html` directly from your browser (e.g. double-click it or open `file:///.../index.html`).

There are two flexible ways it discovers your folders and files:

### Method 1: Instant In-Browser Selection (Zero Setup)
1. Open `index.html` in any browser.
2. Click **"Select Folder"** (or just **drag and drop** your folder directly into the browser window).
3. The page immediately reads all nested subdirectories, builds the tree hierarchy, and displays your HTML files.

### Method 2: Instant Auto-Load with `tree.js` (No Folder Selection Needed)
If you want `index.html` to load all your files automatically on open:
- Run the provided scan script:
  ```bash
  python3 scan.py
  ```
  *(Or if you prefer Node.js: `node scan.js`)*
- This generates `tree.js`. When you open `index.html`, it automatically detects `tree.js` and loads the full hierarchy immediately!

#### 💡 Live Watcher Mode
If you are actively adding or modifying HTML files and folders, you can run the watcher:
```bash
python3 scan.py --watch
# or
node scan.js --watch
```
Whenever a file is added, moved, or deleted, `tree.js` updates automatically in real-time.

---

## 📁 Example Folder Structure

You can create any directory depth you want:

```text
PT/
├── index.html              <-- Main explorer (open this in your browser)
├── tree.js                 <-- Auto-catalog of files
├── scan.py / scan.js       <-- Lightweight helper scripts
│
├── analytics/
│   └── dashboard.html      <-- Standalone HTML file
├── components/
│   ├── buttons.html
│   └── nested/
│       └── modal-demo.html <-- Deeply nested HTML file
└── documents/
    └── guide.html
```

---

## ✨ Features

- **Nested Tree Hierarchy**: Supports unlimited folder nesting levels with expand/collapse chevron toggles and file count badges.
- **Search & Filter**: Real-time search that highlights matches and auto-expands parent folders.
- **Device Viewport Switcher**: Preview your standalone HTML files in **Desktop (100%)**, **Tablet (768px)**, or **Mobile (375px)** device sizes.
- **Direct Preview & New Tab**: Embedded sandbox iframe with a reload button and one-click "Open in New Tab" link.
- **Dark & Light Mode**: Modern UI with dark/light theme toggle.
- **Drag & Drop**: Drag any folder into the browser window anytime to inspect its contents.
- **Completely Offline**: Zero external CDN dependencies, self-contained SVG icons, and works without an internet connection.
