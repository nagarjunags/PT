# builder.py - Shared layout and component builder for GATE Master Notes

CSS_TEMPLATE = """
    :root {
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-elevated: #e2e8f0;
      --bg-code: #0f172a;
      
      --text-main: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      
      --border-color: #e2e8f0;
      --border-strong: #cbd5e1;
      
      --accent: #2563eb;
      --accent-soft: #eff6ff;
      --accent-dark: #1d4ed8;
      
      --success: #16a34a;
      --success-soft: #f0fdf4;
      --warning: #d97706;
      --warning-soft: #fffbeb;
      --danger: #dc2626;
      --danger-soft: #fef2f2;
      --purple: #7c3aed;
      --purple-soft: #f5f3ff;
      --cyan: #0891b2;
      --cyan-soft: #ecfeff;
      
      --font-body: 'Crimson Pro', Georgia, serif;
      --font-ui: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.08);
    }

    [data-theme="dark"] {
      --bg-page: #0b0f19;
      --bg-card: #111827;
      --bg-card-subtle: #1f2937;
      --bg-elevated: #283344;
      --bg-code: #030712;
      
      --text-main: #f9fafb;
      --text-secondary: #e5e7eb;
      --text-muted: #9ca3af;
      
      --border-color: #1f2937;
      --border-strong: #374151;
      
      --accent: #3b82f6;
      --accent-soft: #172554;
      --accent-dark: #60a5fa;
      
      --success: #22c55e;
      --success-soft: #052e16;
      --warning: #f59e0b;
      --warning-soft: #451a03;
      --danger: #ef4444;
      --danger-soft: #450a0a;
      --purple: #a855f7;
      --purple-soft: #2e1065;
      --cyan: #22d3ee;
      --cyan-soft: #083344;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-body);
      font-size: 1.18rem;
      line-height: 1.8;
      color: var(--text-main);
      background-color: var(--bg-page);
      transition: background-color 0.2s ease, color 0.2s ease;
      -webkit-font-smoothing: antialiased;
    }

    .app-container {
      display: flex;
      min-height: 100vh;
    }

    .sidebar {
      width: 330px;
      flex-shrink: 0;
      background: var(--bg-card);
      border-right: 1px solid var(--border-color);
      height: 100vh;
      position: sticky;
      top: 0;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      z-index: 50;
    }

    .sidebar-header {
      padding: 22px 20px;
      border-bottom: 1px solid var(--border-color);
      background: var(--bg-card);
    }

    .sidebar-header h2 {
      font-family: var(--font-ui);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.01em;
    }

    .sidebar-header p {
      font-family: var(--font-ui);
      font-size: 0.76rem;
      color: var(--text-muted);
      margin-top: 4px;
      line-height: 1.4;
    }

    .sidebar-nav {
      padding: 16px 14px;
      display: flex;
      flex-direction: column;
      gap: 3px;
      flex: 1;
    }

    .nav-group-title {
      font-family: var(--font-ui);
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      color: var(--text-muted);
      padding: 14px 10px 4px 10px;
    }

    .nav-link {
      font-family: var(--font-ui);
      font-size: 0.86rem;
      font-weight: 500;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 8px 12px;
      border-radius: 8px;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .nav-link:hover {
      background: var(--bg-card-subtle);
      color: var(--accent);
      transform: translateX(3px);
    }

    .nav-link.active {
      background: var(--accent-soft);
      color: var(--accent);
      font-weight: 600;
    }

    .nav-link .badge {
      font-size: 0.7rem;
      padding: 2px 6px;
      border-radius: 999px;
      background: var(--bg-card-subtle);
      color: var(--text-muted);
      font-weight: 600;
    }

    .main-wrapper {
      flex: 1;
      max-width: 1080px;
      margin: 0 auto;
      padding: 36px 52px 90px 52px;
    }

    .top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 36px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      flex-wrap: wrap;
    }

    .search-wrapper {
      position: relative;
      flex: 1;
      max-width: 480px;
    }

    .search-input {
      width: 100%;
      font-family: var(--font-ui);
      font-size: 0.9rem;
      padding: 9px 14px 9px 38px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      outline: none;
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
    }

    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      font-size: 0.95rem;
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .theme-btn, .expand-all-btn {
      font-family: var(--font-ui);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }

    .theme-btn:hover, .expand-all-btn:hover {
      background: var(--bg-card-subtle);
      border-color: var(--border-strong);
      color: var(--text-main);
    }

    .hero-header {
      background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-card-subtle) 100%);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 42px 40px;
      margin-bottom: 48px;
      box-shadow: var(--shadow-sm);
    }

    .hero-badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 18px;
    }

    .pill-badge {
      font-family: var(--font-ui);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 11px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      letter-spacing: 0.02em;
    }

    .pill-blue { background: var(--accent-soft); color: var(--accent-dark); border: 1px solid var(--accent); }
    .pill-purple { background: var(--purple-soft); color: var(--purple); border: 1px solid var(--purple); }
    .pill-green { background: var(--success-soft); color: var(--success); border: 1px solid var(--success); }
    .pill-cyan { background: var(--cyan-soft); color: var(--cyan); border: 1px solid var(--cyan); }

    .hero-header h1 {
      font-family: var(--font-ui);
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.25;
      color: var(--text-main);
      margin-bottom: 14px;
    }

    .hero-header p {
      font-size: 1.2rem;
      color: var(--text-secondary);
      max-width: 860px;
      line-height: 1.65;
    }

    .exam-stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 16px;
      margin-top: 28px;
      padding-top: 24px;
      border-top: 1px solid var(--border-color);
    }

    .stat-item { font-family: var(--font-ui); }
    .stat-val { font-size: 1.65rem; font-weight: 800; color: var(--accent); letter-spacing: -0.02em; }
    .stat-lbl { font-size: 0.76rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; font-weight: 700; }

    .chapter-section {
      margin-bottom: 64px;
      scroll-margin-top: 32px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 38px 40px;
      box-shadow: var(--shadow-sm);
    }

    .chapter-number-pill {
      font-family: var(--font-ui);
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--accent);
      background: var(--accent-soft);
      padding: 4px 12px;
      border-radius: 999px;
      display: inline-block;
      margin-bottom: 12px;
    }

    h2.chapter-title {
      font-family: var(--font-ui);
      font-size: 1.85rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
      margin-bottom: 24px;
      line-height: 1.3;
    }

    h3.section-heading {
      font-family: var(--font-ui);
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 32px 0 16px 0;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-color);
    }

    h4.subsection-heading {
      font-family: var(--font-ui);
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-dark);
      margin: 24px 0 10px 0;
    }

    p { margin-bottom: 18px; }
    strong { color: var(--text-main); font-weight: 600; }

    .callout {
      border-radius: 12px;
      padding: 20px 22px;
      margin: 24px 0;
      border-left: 5px solid transparent;
      font-size: 1.08rem;
      line-height: 1.7;
    }

    .gate-trap {
      background: var(--danger-soft);
      border-left-color: var(--danger);
      color: var(--text-main);
    }
    .gate-trap-title {
      font-family: var(--font-ui);
      font-weight: 800;
      color: var(--danger);
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pro-tip {
      background: var(--purple-soft);
      border-left-color: var(--purple);
      color: var(--text-main);
    }
    .pro-tip-title {
      font-family: var(--font-ui);
      font-weight: 800;
      color: var(--purple);
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .theory-box {
      background: var(--accent-soft);
      border-left-color: var(--accent);
      color: var(--text-main);
    }
    .theory-title {
      font-family: var(--font-ui);
      font-weight: 800;
      color: var(--accent-dark);
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .table-container {
      overflow-x: auto;
      margin: 26px 0;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      background: var(--bg-card);
      box-shadow: var(--shadow-sm);
    }

    table.academic-table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-ui);
      font-size: 0.94rem;
      text-align: left;
    }

    table.academic-table th {
      background: var(--bg-card-subtle);
      color: var(--text-main);
      font-weight: 700;
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
    }

    table.academic-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-secondary);
      line-height: 1.6;
    }

    table.academic-table tr:last-child td { border-bottom: none; }
    table.academic-table tr:hover td { background: rgba(37, 99, 235, 0.03); }

    .pyq-box {
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: 14px;
      margin: 32px 0;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .pyq-box:hover {
      border-color: var(--accent);
      box-shadow: var(--shadow-md);
    }

    .pyq-header {
      padding: 16px 22px;
      background: var(--bg-card-subtle);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .pyq-tag-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .pyq-badge-num {
      font-family: var(--font-mono);
      font-weight: 800;
      font-size: 0.9rem;
      background: var(--text-main);
      color: var(--bg-card);
      padding: 3px 9px;
      border-radius: 6px;
    }

    .pyq-badge-year {
      font-family: var(--font-ui);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--accent-dark);
      background: var(--accent-soft);
      padding: 3px 9px;
      border-radius: 6px;
    }

    .pyq-badge-marks {
      font-family: var(--font-ui);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--purple);
      background: var(--purple-soft);
      padding: 3px 9px;
      border-radius: 6px;
    }

    .pyq-badge-type {
      font-family: var(--font-ui);
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--cyan);
      background: var(--cyan-soft);
      padding: 3px 9px;
      border-radius: 6px;
    }

    .pyq-body {
      padding: 24px 26px;
      font-size: 1.15rem;
      line-height: 1.75;
    }

    .pyq-diagram {
      margin: 18px 0;
      text-align: center;
      background: #ffffff;
      padding: 16px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }

    .pyq-diagram img {
      max-width: 100%;
      height: auto;
      max-height: 380px;
      object-fit: contain;
    }

    .pyq-options-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin: 18px 0;
    }

    .pyq-opt {
      font-family: var(--font-ui);
      font-size: 0.96rem;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-color);
      padding: 11px 16px;
      border-radius: 8px;
    }

    .reveal-btn {
      font-family: var(--font-ui);
      font-size: 0.84rem;
      font-weight: 700;
      padding: 7px 16px;
      border-radius: 7px;
      border: 1px solid var(--accent);
      background: var(--accent-soft);
      color: var(--accent);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }

    .reveal-btn:hover {
      background: var(--accent);
      color: #ffffff;
    }

    .solution-drawer {
      display: none;
      padding: 24px 26px;
      background: var(--bg-card-subtle);
      border-top: 1px dashed var(--border-strong);
      animation: fadeIn 0.25s ease;
    }

    .solution-drawer.open {
      display: block;
    }

    .sol-header {
      font-family: var(--font-ui);
      font-size: 1rem;
      font-weight: 800;
      color: var(--success);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sol-steps {
      margin-left: 22px;
      margin-bottom: 16px;
    }

    .sol-steps li {
      margin-bottom: 10px;
    }

    .ans-box {
      font-family: var(--font-ui);
      display: inline-block;
      background: var(--success-soft);
      color: var(--success);
      border: 1px solid var(--success);
      padding: 7px 14px;
      border-radius: 7px;
      font-weight: 800;
      font-size: 1rem;
      margin: 12px 0;
    }

    .lab-card {
      background: var(--bg-card);
      border: 2px solid var(--accent);
      border-radius: 16px;
      padding: 28px;
      margin: 36px 0;
      box-shadow: var(--shadow-md);
    }

    .lab-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-color);
    }

    .lab-title {
      font-family: var(--font-ui);
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .lab-input-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }

    .input-field label {
      display: block;
      font-family: var(--font-ui);
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .input-field input, .input-field select {
      width: 100%;
      font-family: var(--font-mono);
      font-size: 0.95rem;
      padding: 8px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-page);
      color: var(--text-main);
      outline: none;
    }

    .input-field input:focus, .input-field select:focus {
      border-color: var(--accent);
    }

    .lab-output {
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-strong);
      border-radius: 10px;
      padding: 18px 20px;
      font-family: var(--font-mono);
      font-size: 0.95rem;
      line-height: 1.6;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 900px) {
      .app-container { flex-direction: column; }
      .sidebar { width: 100%; height: auto; position: static; }
      .main-wrapper { padding: 24px 20px; }
    }
"""

def build_pyq_card(qnum, year, marks, qtype, statement, options=None, answer_key="", steps=None, trap_note="", diagram_img=""):
    """
    Builds a clean, standard PYQ Card with collapsible solution drawer.
    """
    drawer_id = f"sol_{qnum.lower().replace('.', '_').strip()}"
    
    # Diagram HTML
    diag_html = ""
    if diagram_img:
        if isinstance(diagram_img, list):
            items = "".join([f'<div class="pyq-diagram"><img src="{img}" alt="Diagram for {qnum}" /></div>' for img in diagram_img])
            diag_html = items
        elif str(diagram_img).strip().startswith("<"):
            diag_html = str(diagram_img)
        else:
            diag_html = f'<div class="pyq-diagram"><img src="{diagram_img}" alt="Diagram for {qnum}" /></div>'
        
    # Options HTML
    opts_html = ""
    if options and len(options) > 0:
        opt_items = "".join([f'<div class="pyq-opt"><strong>{opt[0]}</strong> {opt[1]}</div>' for opt in options])
        opts_html = f'<div class="pyq-options-grid">{opt_items}</div>'
        
    # Steps HTML
    steps_list = ""
    if steps:
        step_items = "".join([f'<li>{s}</li>' for s in steps])
        steps_list = f'<ol class="sol-steps">{step_items}</ol>'
        
    trap_html = ""
    if trap_note:
        trap_html = f'<div class="callout gate-trap"><div class="gate-trap-title">⚠️ Examiner Trap Alert</div><p>{trap_note}</p></div>'

    card_html = f"""
    <div class="pyq-box">
      <div class="pyq-header">
        <div class="pyq-tag-group">
          <span class="pyq-badge-num">{qnum}</span>
          <span class="pyq-badge-year">{year}</span>
          <span class="pyq-badge-marks">{marks}</span>
          <span class="pyq-badge-type">{qtype}</span>
        </div>
        <button class="reveal-btn" data-target="{drawer_id}">💡 Show Solution</button>
      </div>
      <div class="pyq-body">
        <p>{statement}</p>
        {diag_html}
        {opts_html}
      </div>
      <div id="{drawer_id}" class="solution-drawer">
        <div class="sol-header">🎯 Complete Step-by-Step Derivation & Concept Mapping</div>
        {steps_list}
        <div class="ans-box">Official ExamGOAL Answer Key: <strong>{answer_key}</strong></div>
        {trap_html}
      </div>
    </div>
    """
    return card_html

def render_html_page(title, hero_data, sections_data, sidebar_links, labs_html="", custom_scripts=""):
    """
    Renders a complete, pristine GATE master notes textbook HTML page.
    """
    # Build sidebar HTML
    nav_items_html = ""
    for group in sidebar_links:
        nav_items_html += f'<div class="nav-group-title">{group["title"]}</div>\n'
        for link in group["links"]:
            badge_html = f'<span class="badge">{link["badge"]}</span>' if "badge" in link else ''
            nav_items_html += f'<a href="#{link["id"]}" class="nav-link"><span>{link["text"]}</span>{badge_html}</a>\n'

    # Build Hero HTML
    stats_html = "".join([f'<div class="stat-item"><div class="stat-val">{s["val"]}</div><div class="stat-lbl">{s["lbl"]}</div></div>' for s in hero_data.get("stats", [])])
    hero_html = f"""
    <div class="hero-header">
      <div class="hero-badge-row">
        <span class="pill-badge pill-blue">GATE ECE / EE Master Class</span>
        <span class="pill-badge pill-purple">Official ExamGOAL Archive</span>
        <span class="pill-badge pill-green">Textbook-Grade Derivations</span>
        <span class="pill-badge pill-cyan">Interactive Simulator</span>
      </div>
      <h1>{hero_data["title"]}</h1>
      <p>{hero_data["subtitle"]}</p>
      <div class="exam-stats-grid">
        {stats_html}
      </div>
    </div>
    """

    # Build Sections HTML
    body_sections_html = ""
    for sec in sections_data:
        pill = f'<div class="chapter-number-pill">{sec["pill"]}</div>' if "pill" in sec else ''
        body_sections_html += f"""
        <section id="{sec['id']}" class="chapter-section">
          {pill}
          <h2 class="chapter-title">{sec['title']}</h2>
          <div class="section-content">
            {sec['content']}
          </div>
        </section>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>

  <!-- Google Fonts: Inter (UI), Crimson Pro (Textbook Body), JetBrains Mono (Code/Math) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">

  <!-- KaTeX for pristine mathematical typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <style>
{CSS_TEMPLATE}
  </style>
</head>
<body>
  <div class="app-container">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>📚 GATE Master Series</h2>
        <p>Digital Electronics & Logic Design</p>
      </div>
      <nav class="sidebar-nav">
        {nav_items_html}
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="main-wrapper">
      <!-- Top Action Bar -->
      <div class="top-bar">
        <div class="search-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="chapterSearch" class="search-input" placeholder="Search theory, theorems, or PYQs..." />
        </div>
        <div class="top-actions">
          <button id="themeToggle" class="theme-btn" title="Toggle Light/Dark Theme">🌓 Theme</button>
          <button id="expandAllBtn" class="expand-all-btn" title="Expand/Collapse all PYQ solutions">📖 Expand All</button>
        </div>
      </div>

      <!-- Hero Header -->
      {hero_html}

      <!-- Chapter Sections & PYQ Walkthroughs -->
      {body_sections_html}

      <!-- Interactive Calculator / Labs -->
      {labs_html}
    </main>
  </div>

  <script>
    // Theme toggle
    const themeBtn = document.getElementById('themeToggle');
    const currentTheme = localStorage.getItem('gate_theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    themeBtn.addEventListener('click', () => {{
      const t = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', t);
      localStorage.setItem('gate_theme', t);
    }});

    // Expand/Collapse all solutions
    const expandBtn = document.getElementById('expandAllBtn');
    let allExpanded = false;
    expandBtn.addEventListener('click', () => {{
      allExpanded = !allExpanded;
      document.querySelectorAll('.solution-drawer').forEach(d => {{
        if (allExpanded) d.classList.add('open');
        else d.classList.remove('open');
      }});
      expandBtn.innerHTML = allExpanded ? '📕 Collapse All' : '📖 Expand All';
    }});

    // Solution toggling
    document.querySelectorAll('.reveal-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const targetId = btn.getAttribute('data-target');
        const drawer = document.getElementById(targetId);
        if (drawer) {{
          drawer.classList.toggle('open');
          btn.innerHTML = drawer.classList.contains('open') ? '🙈 Hide Solution' : '💡 Show Solution';
        }}
      }});
    }});

    // Realtime Search
    const searchInput = document.getElementById('chapterSearch');
    if (searchInput) {{
      searchInput.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        document.querySelectorAll('.pyq-box, .chapter-section').forEach(el => {{
          if (!q) {{
            el.style.display = '';
            return;
          }}
          const text = el.innerText.toLowerCase();
          if (text.includes(q)) {{
            el.style.display = '';
          }} else if (el.classList.contains('pyq-box')) {{
            el.style.display = 'none';
          }}
        }});
      }});
    }}

    // KaTeX auto render
    document.addEventListener("DOMContentLoaded", function() {{
      if (typeof renderMathInElement !== 'undefined') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}}
          ],
          throwOnError: false
        }});
      }}
    }});

    {custom_scripts}
  </script>
</body>
</html>
"""
    return full_html
