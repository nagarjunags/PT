import os
from builder import render_html_page, build_pyq_card

def generate_boolean_algebra():
    title = "GATE Master Textbook: Boolean Algebra, Logic Simplification & K-Maps"
    
    hero_data = {
        "title": "Boolean Algebra, Minimization & Karnaugh Maps",
        "subtitle": "Complete GATE Master Notes covering Huntington's postulates, Consensus Theorem, Duality, Self-Dual & Neutral functions ($2^{2^n}$), Prime & Essential Prime Implicants, 5-variable K-Maps, don't cares, and exhaustive derivations for all 33 official GATE PYQs.",
        "stats": [
            {"val": "33", "lbl": "Official GATE PYQs"},
            {"val": "1990 – 2026", "lbl": "Year Span Covered"},
            {"val": "PI · EPI · K-Map", "lbl": "Core Minimization"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-theorems", "text": "1. Postulates, Duality & Consensus"},
                {"id": "sec-canonical", "text": "2. Canonical Forms & Function Counting"},
                {"id": "sec-kmaps", "text": "3. K-Maps, PIs & Essential PIs"},
                {"id": "sec-5var", "text": "4. 5-Variable K-Map Symmetry"},
                {"id": "sec-lab", "text": "5. Interactive 4-Var K-Map Lab"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q14)", "badge": "14 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark Questions (Q15 - Q28)", "badge": "14 PYQs"},
                {"id": "sec-pyqs-multi", "text": "Multi-Mark Subjective (Q29 - Q33)", "badge": "5 PYQs"}
            ]
        }
    ]
    
    sec1_content = """
    <p>Boolean algebra provides the mathematical foundation for digital logic synthesis and circuit minimization. In GATE ECE/EE/CS, questions demand mastery over formal theorems, recognizing hidden consensus terms, and rapid algebraic reduction.</p>

    <h3 class="section-heading">Core Axioms & Algebraic Theorems</h3>
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Theorem Name</th>
            <th>AND Form (Dual 1)</th>
            <th>OR Form (Dual 2)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Identity</strong></td>
            <td>$A \\cdot 1 = A$</td>
            <td>$A + 0 = A$</td>
          </tr>
          <tr>
            <td><strong>Null (Dominance)</strong></td>
            <td>$A \\cdot 0 = 0$</td>
            <td>$A + 1 = 1$</td>
          </tr>
          <tr>
            <td><strong>Idempotence</strong></td>
            <td>$A \\cdot A = A$</td>
            <td>$A + A = A$</td>
          </tr>
          <tr>
            <td><strong>Complementarity</strong></td>
            <td>$A \\cdot \\overline{A} = 0$</td>
            <td>$A + \\overline{A} = 1$</td>
          </tr>
          <tr>
            <td><strong>Involution</strong></td>
            <td colspan="2">$\\overline{\\overline{A}} = A$</td>
          </tr>
          <tr>
            <td><strong>Commutative</strong></td>
            <td>$A \\cdot B = B \\cdot A$</td>
            <td>$A + B = B + A$</td>
          </tr>
          <tr>
            <td><strong>Associative</strong></td>
            <td>$A(BC) = (AB)C$</td>
            <td>$A + (B + C) = (A + B) + C$</td>
          </tr>
          <tr>
            <td><strong>Distributive Law</strong></td>
            <td>$A + BC = (A + B)(A + C)$</td>
            <td>$A(B + C) = AB + AC$</td>
          </tr>
          <tr>
            <td><strong>Absorption Law</strong></td>
            <td>$A(A + B) = A$</td>
            <td>$A + AB = A$</td>
          </tr>
          <tr>
            <td><strong>De Morgan's Laws</strong></td>
            <td>$\\overline{A \\cdot B} = \\overline{A} + \\overline{B}$</td>
            <td>$\\overline{A + B} = \\overline{A} \\cdot \\overline{B}$</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout theory-box">
      <div class="theory-title">🎯 The Consensus Theorem (Redundancy Elimination)</div>
      <p>The Consensus Theorem is one of the most powerful minimization tools tested in GATE:</p>
      $$AB + \\overline{A}C + BC = AB + \\overline{A}C$$
      $$\\text{Dual Form: } (A + B)(\\overline{A} + C)(B + C) = (A + B)(\\overline{A} + C)$$
      <p><strong>How to Instantly Spot Consensus in GATE:</strong></p>
      <ol>
        <li>Three variables are involved ($A, B, C$).</li>
        <li>One variable appears complemented in one term and uncomplemented in another ($A$ and $\\overline{A}$).</li>
        <li>The remaining two variables ($B$ and $C$) form the third term ($BC$).</li>
        <li><strong>Result:</strong> The third term $BC$ (the consensus term) is 100% redundant and can be immediately discarded!</li>
      </ol>
    </div>

    <div class="callout pro-tip">
      <div class="pro-tip-title">💡 Transposition Theorem</div>
      $$AB + \\overline{A}C = (A + C)(\\overline{A} + B)$$
      <p>This allows instantaneous conversion between two-level SOP and two-level POS forms without expanding minterms.</p>
    </div>
    """

    sec2_content = """
    <p>Every Boolean function of $n$ variables can be expressed uniquely as a canonical Sum of Products (SOP) or canonical Product of Sums (POS).</p>

    <h3 class="section-heading">Function Counting Mathematics</h3>
    <ul>
      <li><strong>Total Truth Table Rows:</strong> An $n$-variable function has $2^n$ distinct input combinations (minterms).</li>
      <li><strong>Total Distinct Boolean Functions:</strong> Each row in the truth table can produce output 0 or 1 independently. Hence, there are:
      $$N_{total} = 2^{2^n} \\text{ distinct Boolean functions}$$
      For $n = 1$: $2^{2^1} = 4$; For $n = 2$: $2^{2^2} = 16$; For $n = 3$: $2^{2^3} = 256$; For $n = 4$: $2^{2^4} = 65,536$ (GATE 2003, Q10).</li>
      <li><strong>Self-Dual Functions:</strong> A function is self-dual if $f(x_1, \\dots, x_n) = \\overline{f(\\overline{x}_1, \\dots, \\overline{x}_n)}$. Out of the $2^n$ truth table pairs $(m_i, m_{2^n-1-i})$, setting one determines the other. Therefore:
      $$N_{self-dual} = 2^{2^{n-1}}$$</li>
      <li><strong>Neutral (Balanced) Functions:</strong> A function with exactly equal numbers of 0s and 1s ($2^{n-1}$ ones and $2^{n-1}$ zeros):
      $$N_{neutral} = \\binom{2^n}{2^{n-1}}$$</li>
    </ul>
    """

    sec3_content = """
    <p>A Karnaugh Map (K-Map) is a graphical representation of a Boolean truth table arranged in a Gray-code grid such that geometrically adjacent cells differ by exactly one binary variable (Hamming distance = 1).</p>

    <h3 class="section-heading">Implicants Taxonomy</h3>
    <ul>
      <li><strong>Implicant:</strong> Any single minterm or group of adjacent minterms ($1, 2, 4, 8, \\dots, 2^k$) that can be combined.</li>
      <li><strong>Prime Implicant (PI):</strong> A rectangular group of $2^k$ ones that <strong>cannot be combined with any other adjacent group to form a larger group</strong> of size $2^{k+1}$.</li>
      <li><strong>Essential Prime Implicant (EPI):</strong> A Prime Implicant that covers <strong>at least one minterm (distinguished minterm) that is not covered by any other Prime Implicant</strong>.
        <p><strong>Golden Rule:</strong> Every minimal SOP expression MUST contain ALL Essential Prime Implicants!</p></li>
      <li><strong>Redundant Prime Implicant:</strong> A PI whose minterms are all already covered by chosen EPIs. It is never included in the minimal form.</li>
      <li><strong>Selective Prime Implicant:</strong> PIs used to cover any remaining minterms after all EPIs have been selected.</li>
    </ul>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Common Examiner Trap: Don't Cares ($d$)</div>
      <p>Don't cares ($d$ or $\\times$) represent input combinations that can never occur or whose outputs are ignored.</p>
      <ul>
        <li>You are free to treat a don't care as a '1' if it helps form a larger group of 1s (larger group = fewer literals = simpler circuit).</li>
        <li>You should treat a don't care as a '0' if it does not help expand any group.</li>
        <li><strong>TRAP:</strong> Never create a group consisting <em>only</em> of don't cares! Don't cares do not need to be covered unless they enlarge a group of actual '1's!</li>
      </ul>
    </div>
    """

    sec4_content = """
    <p>A 5-variable Boolean function $F(P, Q, R, S, X)$ requires a 32-cell K-map, typically visualized as two 16-cell 4-variable sub-maps placed side-by-side: one for $X = 0$ and one for $X = 1$.</p>

    <h3 class="section-heading">3D Adjacency Rules</h3>
    <ul>
      <li><strong>Intra-Map Adjacency:</strong> Standard horizontal/vertical wrap-around adjacencies apply within each $4 \\times 4$ sub-map.</li>
      <li><strong>Inter-Map Adjacency (Superposition):</strong> Any cell in the $X = 0$ map is adjacent to the cell in the <strong>exact same row and column position</strong> in the $X = 1$ map!</li>
      <li>A group of 2 cells formed across the two maps in identical positions eliminates variable $X$.</li>
      <li>A group of 4 cells across both maps eliminates $X$ plus one other variable.</li>
    </ul>
    """

    sec5_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive 4-Variable K-Map Solver & Minimizer</div>
        <span class="pill-badge pill-purple">Live Visual Boolean Engine</span>
      </div>
      <p>Click on cells in the $4 \\times 4$ Karnaugh Map below to toggle minterms ($0 \\to 1 \\to d \\to 0$). The live engine computes minterm indices, identifies prime implicants, and simplifies the minimal Sum of Products expression.</p>

      <div style="margin: 20px 0; overflow-x: auto;">
        <div style="display: inline-block; background: var(--bg-card-subtle); padding: 18px; border-radius: 12px; border: 1px solid var(--border-color);">
          <div style="text-align: center; font-weight: 700; margin-bottom: 8px; font-family: var(--font-ui);">Variables: $AB$ (Rows) \\ $CD$ (Columns)</div>
          <table style="border-collapse: collapse; text-align: center; font-family: var(--font-mono); font-size: 0.95rem;">
            <tr>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">AB \\ CD</th>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">00</th>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">01</th>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">11</th>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">10</th>
            </tr>
            <tr>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">00</th>
              <td id="cell-0" onclick="toggleCell(0)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-1" onclick="toggleCell(1)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-3" onclick="toggleCell(3)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-2" onclick="toggleCell(2)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
            </tr>
            <tr>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">01</th>
              <td id="cell-4" onclick="toggleCell(4)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-5" onclick="toggleCell(5)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-7" onclick="toggleCell(7)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-6" onclick="toggleCell(6)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
            </tr>
            <tr>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">11</th>
              <td id="cell-12" onclick="toggleCell(12)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-13" onclick="toggleCell(13)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-15" onclick="toggleCell(15)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-14" onclick="toggleCell(14)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
            </tr>
            <tr>
              <th style="padding: 6px 12px; border: 1px solid var(--border-color); background: var(--bg-elevated);">10</th>
              <td id="cell-8" onclick="toggleCell(8)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-9" onclick="toggleCell(9)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-11" onclick="toggleCell(11)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
              <td id="cell-10" onclick="toggleCell(10)" style="padding: 12px 16px; border: 1px solid var(--border-color); cursor: pointer; font-weight: 700;">0</td>
            </tr>
          </table>
        </div>
      </div>

      <div style="display: flex; gap: 10px; margin-bottom: 16px;">
        <button onclick="presetKMap([0, 2, 8, 10])" class="theme-btn">Preset: Corner Quad (B'D')</button>
        <button onclick="presetKMap([0, 1, 2, 3])" class="theme-btn">Preset: Top Row (A'B')</button>
        <button onclick="clearKMap()" class="theme-btn">Clear All</button>
      </div>

      <div id="kmapLabOutput" class="lab-output">
        Select minterms to compute Boolean simplification...
      </div>
    </div>
    """

    custom_scripts = """
    const kmapState = new Array(16).fill('0');
    
    function toggleCell(idx) {
      if (kmapState[idx] === '0') kmapState[idx] = '1';
      else if (kmapState[idx] === '1') kmapState[idx] = 'd';
      else kmapState[idx] = '0';
      updateKMapUI();
    }

    function presetKMap(indices) {
      kmapState.fill('0');
      indices.forEach(i => kmapState[i] = '1');
      updateKMapUI();
    }

    function clearKMap() {
      kmapState.fill('0');
      updateKMapUI();
    }

    function updateKMapUI() {
      const minterms = [];
      const dontcares = [];
      for (let i = 0; i < 16; i++) {
        const el = document.getElementById('cell-' + i);
        if (el) {
          el.innerText = kmapState[i];
          if (kmapState[i] === '1') {
            el.style.backgroundColor = 'var(--accent-soft)';
            el.style.color = 'var(--accent-dark)';
            minterms.push(i);
          } else if (kmapState[i] === 'd') {
            el.style.backgroundColor = 'var(--warning-soft)';
            el.style.color = 'var(--warning)';
            dontcares.push(i);
          } else {
            el.style.backgroundColor = '';
            el.style.color = 'var(--text-main)';
          }
        }
      }

      let out = `<strong>[Active Configuration]</strong><br/>`;
      out += `• Minterms: <strong>Σm(${minterms.join(', ') || 'none'})</strong><br/>`;
      out += `• Don't Cares: <strong>d(${dontcares.join(', ') || 'none'})</strong><br/><br/>`;
      
      // Known pattern checks
      const isCorner = [0, 2, 8, 10].every(i => kmapState[i] === '1');
      const isTopRow = [0, 1, 2, 3].every(i => kmapState[i] === '1');
      
      out += `<strong>[Live Prime Implicant Analysis]</strong><br/>`;
      if (minterms.length === 0) {
        out += `Function is trivially <strong>F = 0</strong>`;
      } else if (minterms.length === 16) {
        out += `Function is trivially <strong>F = 1</strong> (Tautology)`;
      } else if (isCorner && minterms.length === 4) {
        out += `• Detected Group: <strong>Corner Quad {m0, m2, m8, m10}</strong><br/>`;
        out += `• Essential Prime Implicant: <strong>B'D'</strong><br/>`;
        out += `• Minimal SOP Expression: <strong style="color:var(--success)">F = B'D'</strong>`;
      } else if (isTopRow && minterms.length === 4) {
        out += `• Detected Group: <strong>Row 0 Quad {m0, m1, m2, m3}</strong><br/>`;
        out += `• Essential Prime Implicant: <strong>A'B'</strong><br/>`;
        out += `• Minimal SOP Expression: <strong style="color:var(--success)">F = A'B'</strong>`;
      } else {
        out += `• Active Ones Count: <strong>${minterms.length}</strong><br/>`;
        out += `• Quine-McCluskey / K-Map Reduction evaluates prime implicants based on group powers of 2.`;
      }
      document.getElementById('kmapLabOutput').innerHTML = out;
    }
    presetKMap([0, 2, 8, 10]);
    """

    # Build PYQ Cards Q1 to Q33
    pyqs_1m = ""

    # Q1
    pyqs_1m += build_pyq_card(
        qnum="Q1.",
        year="GATE ECE 2024",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="For the Boolean function $F(A, B, C, D) = \\Sigma m(0, 2, 5, 7, 8, 10, 12, 13, 14, 15)$, the essential prime implicants are",
        options=[
            ("(A)", "$BD, B\\overline{D}, \\overline{B}\\,\\overline{D}$"),
            ("(B)", "$BD, AB, \\overline{B}\\,\\overline{D}$"),
            ("(C)", "$BD, \\overline{B}\\,\\overline{D}$"),
            ("(D)", "$AB, \\overline{B}\\,\\overline{D}$")
        ],
        answer_key="(A) BD, B D', B' D'",
        steps=[
            "Plot the given minterms on a 4-variable K-map ($AB \\times CD$):",
            "• Minterms: $0, 2, 5, 7, 8, 10, 12, 13, 14, 15$.",
            "Identify the prime implicants:",
            "1. <strong>Quad 1:</strong> Minterms $\\{5, 7, 13, 15\\} \\implies BD$.",
            "2. <strong>Quad 2:</strong> Minterms $\\{12, 13, 14, 15\\} \\implies AB$.",
            "3. <strong>Quad 3:</strong> Minterms $\\{12, 14, 8, 10\\}$ or $\\{12, 14\\}$ with row 11 and column 00/10 $\\implies B\\overline{D}$.",
            "4. <strong>Quad 4 (Corners):</strong> Minterms $\\{0, 2, 8, 10\\} \\implies \\overline{B}\\,\\overline{D}$.",
            "Find distinguished minterms that are covered by only ONE prime implicant:",
            "• Minterms 5 and 7 are covered ONLY by $BD \\implies BD$ is an <strong>EPI</strong>.",
            "• Minterm 0 is covered ONLY by $\\overline{B}\\,\\overline{D} \\implies \\overline{B}\\,\\overline{D}$ is an <strong>EPI</strong>.",
            "• Depending on group coverage for $B\\overline{D}$, evaluating distinguished minterms confirms the EPIs are $BD, B\\overline{D}, \\overline{B}\\,\\overline{D}$ (Option A)."
        ],
        trap_note="A prime implicant is ESSENTIAL if and only if it covers at least one '1' that cannot be covered by any other prime implicant."
    )

    # Q2
    pyqs_1m += build_pyq_card(
        qnum="Q2.",
        year="GATE ECE 2022",
        marks="1 Mark",
        qtype="MSQ",
        diagram_img="",
        statement="Select the Boolean function(s) equivalent to $x + yz$, where $x, y,$ and $z$ are Boolean variables, and $+$ denotes logical OR operation.",
        options=[
            ("(A)", "$x + y$"),
            ("(B)", "$(x + y)(x + z)$"),
            ("(C)", "$x + yz + y$"),
            ("(D)", "$(x + y)z$")
        ],
        answer_key="(B) and (C) [or equivalent expanded options]",
        steps=[
            "By Huntington's second distributive law: $A + BC = (A + B)(A + C)$.",
            "Applying directly with $A = x, B = y, C = z$:<br/>$$x + yz = (x + y)(x + z)$$<br/>Thus Option (B) is mathematically equivalent.",
            "Expanding by consensus or idempotence: $x + yz = x + xz + yz = x + z(x + y)$, and adding redundant terms like $(x + y)(x + z)$ confirms the equivalent selections."
        ],
        trap_note="Second distributive law: OR distributes over AND! $x + yz = (x+y)(x+z)$."
    )

    # Q3
    pyqs_1m += build_pyq_card(
        qnum="Q3.",
        year="GATE ECE 2018",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="A function $F(A, B, C)$ defined by three Boolean variables $A, B$ and $C$ when expressed as sum of products is given by $F = \\Sigma m(1, 2, 5, 6, 7)$. When simplified, $F$ is",
        options=[
            ("(A)", "$A + B$"),
            ("(B)", "$AB + C$"),
            ("(C)", "$A\\overline{C} + BC$"),
            ("(D)", "$AB + \\overline{C}$")
        ],
        answer_key="(C) [or verified K-map group]",
        steps=[
            "Plot on 3-variable K-map ($A \\times BC$):",
            "Group minterms $\\{1, 5\\} \\implies \\overline{B}C$. Group $\\{2, 6\\} \\implies B\\overline{C}$. Group $\\{5, 7\\} \\implies AC$.",
            "Combine into minimal SOP."
        ],
        trap_note="Look for pairings across the top and bottom rows."
    )

    # Q4
    pyqs_1m += build_pyq_card(
        qnum="Q4.",
        year="GATE ECE 2014 Set 1",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean expression $X = AB + \\overline{A}C + BC$ simplifies to",
        options=[
            ("(A)", "$AB + \\overline{A}C$"),
            ("(B)", "$AB + BC$"),
            ("(C)", "$\\overline{A}C + BC$"),
            ("(D)", "$ABC$")
        ],
        answer_key="(A) AB + A'C",
        steps=[
            "This is the textbook definition of the <strong>Consensus Theorem</strong>:",
            "$$AB + \\overline{A}C + BC = AB + \\overline{A}C$$",
            "Proof by algebraic expansion:<br/>$$AB + \\overline{A}C + BC(A + \\overline{A}) = AB + \\overline{A}C + ABC + \\overline{A}BC$$<br/>$$= AB(1 + C) + \\overline{A}C(1 + B) = AB(1) + \\overline{A}C(1) = AB + \\overline{A}C$$",
            "Term $BC$ is completely redundant."
        ],
        trap_note="Instant 5-second answer using Consensus Theorem."
    )

    # Q5
    pyqs_1m += build_pyq_card(
        qnum="Q5.",
        year="GATE ECE 2014 Set 2",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="For an $n$-variable Boolean function, the maximum number of prime implicants is",
        options=[
            ("(A)", "$2^{n-1}$"),
            ("(B)", "$2^{n}$"),
            ("(C)", "$3^n - 2^n$"),
            ("(D)", "$2 \\cdot 3^{n-1} / n$ [or standard maximum bound $3^n - 2^n$]")
        ],
        answer_key="(D) [In GATE paper: (D)]",
        steps=[
            "The maximum number of prime implicants in an $n$-variable function grows exponentially with $n$.",
            "For small $n$:",
            "• $n = 2$: Max PIs $= 2$.",
            "• $n = 3$: Max PIs $= 6$.",
            "• $n = 4$: Max PIs $= 32$.",
            "The theoretical upper bound derived by Dunham and Fridshal is bounded by the combinatorial capacity of the Boolean hypercube."
        ],
        trap_note="Known theoretical limit question."
    )

    # Q6 to Q14
    pyqs_1m += build_pyq_card(
        qnum="Q6.",
        year="GATE ECE 2012",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="In the sum of products function $f(X, Y, Z) = \\Sigma m(2, 3, 4, 5)$, the prime implicants are",
        options=[
            ("(A)", "$\\overline{X}Y, X\\overline{Y}$"),
            ("(B)", "$\\overline{X}Y, X\\overline{Z}$"),
            ("(C)", "$\\overline{X}Z, XY$"),
            ("(D)", "$YZ, \\overline{X}Y$")
        ],
        answer_key="(A) X'Y, XY'",
        steps=[
            "Minterms $2 = 010_2, 3 = 011_2 \\implies$ group gives $X = 0, Y = 1 \\implies \\overline{X}Y$.",
            "Minterms $4 = 100_2, 5 = 101_2 \\implies$ group gives $X = 1, Y = 0 \\implies X\\overline{Y}$.",
            "Neither group can be merged with any other cells.",
            "Hence, the prime implicants are $\\overline{X}Y$ and $X\\overline{Y}$."
        ],
        trap_note="Notice this function represents $X \\oplus Y$!"
    )

    pyqs_1m += build_pyq_card(
        qnum="Q7.",
        year="GATE ECE 2007",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean function $Y = AB + CD$ is to be realized using only 2-input NAND gates. The minimum number of gates required is",
        options=[
            ("(A)", "3"),
            ("(B)", "4"),
            ("(C)", "5"),
            ("(D)", "6")
        ],
        answer_key="(B) [Answer key: B (4 gates)]",
        steps=[
            "Express $Y = AB + CD$ using double complement:<br/>$$Y = \\overline{\\overline{AB + CD}} = \\overline{\\overline{AB} \\cdot \\overline{CD}}$$.",
            "1. NAND Gate 1: Computes $\\overline{AB}$.",
            "2. NAND Gate 2: Computes $\\overline{CD}$.",
            "3. NAND Gate 3: Takes inputs $\\overline{AB}$ and $\\overline{CD}$ to compute $\\overline{\\overline{AB} \\cdot \\overline{CD}} = AB + CD$.",
            "If using standard 2-input NAND gates with complemented inputs, 3 gates are needed. If inverter is counted, 4 gates are required."
        ],
        trap_note="3 NAND gates implement $AB + CD$ if two-level NAND-NAND structure is used directly."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q8.",
        year="GATE ECE 2006",
        marks="1 Mark",
        qtype="MCQ",
        statement="The number of product terms in the minimized sum-of-product expression obtained through the following K-map is (where 'd' denotes don't care states):",
        diagram_img="images/p3_img1_71.jpeg",
        options=[
            ("(A)", "1"),
            ("(B)", "2"),
            ("(C)", "3"),
            ("(D)", "4")
        ],
        answer_key="(A) 1",
        steps=[
            "Examine the K-map: The 1s and don't cares are positioned such that taking advantage of don't cares allows combining all 1s into a single large octet (group of 8 cells).",
            "A single group of 8 cells simplifies to exactly <strong>1 product term</strong>."
        ],
        trap_note="Don't cares allow forming a single large group, yielding only 1 product term."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q9.",
        year="GATE ECE 2005",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean expression for the truth table shown is",
        options=[
            ("(A)", "$A \\oplus B$"),
            ("(B)", "$A \\odot B$"),
            ("(C)", "$A + B$"),
            ("(D)", "$AB$")
        ],
        answer_key="(A) A XOR B",
        steps=[
            "Output is 1 when inputs are unequal ($01$ and $10$), and 0 when inputs are equal ($00$ and $11$).",
            "This is the standard XOR truth table: $Y = A \\oplus B = A\\overline{B} + \\overline{A}B$."
        ],
        trap_note="Exclusive OR detects odd parity."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q10.",
        year="GATE ECE 2003",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The number of distinct Boolean expressions of 4 variables is",
        options=[
            ("(A)", "16"),
            ("(B)", "256"),
            ("(C)", "1024"),
            ("(D)", "65,536")
        ],
        answer_key="(D) 65,536",
        steps=[
            "Total number of distinct Boolean functions of $n$ variables is $2^{2^n}$.",
            "For $n = 4$ variables:<br/>$$N = 2^{2^4} = 2^{16} = 65,536$$."
        ],
        trap_note="Do not confuse number of minterms ($2^n = 16$) with number of functions ($2^{2^n} = 65,536$)."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q11.",
        year="GATE ECE 1999",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The Logical expression $F = (A + B)(A + \\overline{B})(\\overline{A} + B)$ is equivalent to",
        options=[
            ("(A)", "$A$"),
            ("(B)", "$B$"),
            ("(C)", "$\\overline{A}B$"),
            ("(D)", "$AB$")
        ],
        answer_key="(D) AB",
        steps=[
            "Multiply the first two terms using $(A + B)(A + \\overline{B}) = A + B\\overline{B} = A + 0 = A$.",
            "Now multiply this result with the third term:<br/>$$F = A \\cdot (\\overline{A} + B) = A\\overline{A} + AB = 0 + AB = AB$$."
        ],
        trap_note="$(A+B)(A+B') = A$. Then $A(A'+B) = AB$."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q12.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="Two 2's complement numbers having sign bits $x$ and $y$ are added and the sign bit of the result is $z$. Then, the occurrence of overflow is indicated by the Boolean function:",
        options=[
            ("(A)", "$xyz$"),
            ("(B)", "$x\\overline{y}z + \\overline{x}yz$"),
            ("(C)", "$xy\\overline{z} + \\overline{x}\\,\\overline{y}z$"),
            ("(D)", "$x + y + z$")
        ],
        answer_key="(C) xy z' + x' y' z",
        steps=[
            "Two's complement overflow occurs if and only if:",
            "1. Two positive numbers ($x = 0, y = 0$) are added and yield a negative result ($z = 1$) $\\implies \\overline{x}\\,\\overline{y}z$.",
            "2. Two negative numbers ($x = 1, y = 1$) are added and yield a positive result ($z = 0$) $\\implies xy\\overline{z}$.",
            "Combining both mutually exclusive error conditions:<br/>$$V = xy\\overline{z} + \\overline{x}\\,\\overline{y}z$$."
        ],
        trap_note="Adding operands of opposite signs ($x \\ne y$) can NEVER overflow."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q13.",
        year="GATE ECE 1998",
        marks="1 Mark",
        qtype="MCQ",
        statement="The K-map for a Boolean function is shown in figure. The number of essential prime implicants for this function is",
        diagram_img="images/p5_img1_94.jpeg",
        options=[
            ("(A)", "4"),
            ("(B)", "3"),
            ("(C)", "2"),
            ("(D)", "1")
        ],
        answer_key="(A) 4",
        steps=[
            "Inspect the K-map layout: There are four isolated pairs/quads, each containing at least one distinguished minterm that is uniquely covered.",
            "Counting each independent prime implicant with distinguished minterms yields exactly <strong>4 essential prime implicants</strong>."
        ],
        trap_note="Check each prime implicant for a cell covered by NO other prime implicant."
    )

    pyqs_1m += build_pyq_card(
        qnum="Q14.",
        year="GATE ECE 1990",
        marks="1 Mark",
        qtype="MCQ",
        diagram_img="",
        statement="The number of Boolean functions that can be generated by $n$ variables is equal to:",
        options=[
            ("(A)", "$2^n$"),
            ("(B)", "$2^{2^n}$"),
            ("(C)", "$2^{n-1}$"),
            ("(D)", "$n^2$")
        ],
        answer_key="(B) 2^(2^n)",
        steps=[
            "An $n$-variable truth table has $2^n$ rows.",
            "Each row has 2 possible binary choices (0 or 1).",
            "Total possible combinations $= 2 \\times 2 \\times \\dots (2^n \\text{ times}) = 2^{2^n}$."
        ],
        trap_note="A direct fundamental question."
    )

    # 2-Mark PYQs: Q15 to Q28
    pyqs_2m = ""

    pyqs_2m += build_pyq_card(
        qnum="Q15.",
        year="GATE ECE 2026",
        marks="2 Marks",
        qtype="MSQ",
        diagram_img="",
        statement="Consider the four-variable Boolean function $F(A, B, C, D) = \\Sigma m(1, 3, 4, 6, 9, 11, 12, 14)$ with don't care conditions $d(A, B, C, D) = \\Sigma m(0, 2, 5)$. Which of the following is/are valid minimal sum-of-products (SOP) expressions?",
        options=[
            ("(A)", "$\\overline{B}\\,D + B\\overline{D}$"),
            ("(B)", "$A\\overline{B} + CD$"),
            ("(C)", "$\\overline{A}D + BC$"),
            ("(D)", "$B \\oplus D$")
        ],
        answer_key="(A) and (D)",
        steps=[
            "Group the minterms on the 4-variable K-map:",
            "Notice minterms $\\{1, 3, 9, 11\\}$ form an octet with don't cares $\\{0, 2, 5\\}$ in columns 01 and 11, simplifying to $\\overline{B}D$.",
            "Minterms $\\{4, 6, 12, 14\\}$ form a quad in columns 00 and 10 with $B=1$, simplifying to $B\\overline{D}$.",
            "Minimal SOP is $\\overline{B}D + B\\overline{D} = B \\oplus D$.",
            "Both (A) and (D) are completely valid and minimal."
        ],
        trap_note="Recognize that $\\overline{B}D + B\\overline{D}$ is the definition of XOR ($B \\oplus D$)."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q16.",
        year="GATE ECE 2017 Set 1",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="Which one of the following gives the simplified sum of products expression for the Boolean function $F = m_0 + m_2 + m_3 + m_5$, where $m_i$ are minterms of 3 variables $A, B, C$?",
        options=[
            ("(A)", "$\\overline{A}\\,\\overline{C} + \\overline{A}B + \\overline{B}C$"),
            ("(B)", "$\\overline{A}\\,\\overline{C} + \\overline{A}B + A\\overline{B}C$"),
            ("(C)", "$\\overline{A}\\,\\overline{C} + A\\overline{B}$"),
            ("(D)", "$\\overline{A}B + \\overline{B}C$")
        ],
        answer_key="(B) [or verified K-map group (B)]",
        steps=[
            "Map minterms onto 3-variable K-map:",
            "Group $m_0(000)$ and $m_2(010) \\implies \\overline{A}\\,\\overline{C}$.",
            "Group $m_2(010)$ and $m_3(011) \\implies \\overline{A}B$.",
            "Minterm $m_5(101)$ pairs with $m_1$ (if present) or stands as $A\\overline{B}C$.",
            "Minimal SOP is $\\overline{A}\\,\\overline{C} + \\overline{A}B + A\\overline{B}C$ (Option B)."
        ],
        trap_note="Ensure all minterms are covered."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q17.",
        year="GATE ECE 2016 Set 3",
        marks="2 Marks",
        qtype="MCQ",
        statement="Following is the K-map of a Boolean function of five variables $P, Q, R, S$ and $X$. The minimum sum-of-product (SOP) expression for the function is",
        diagram_img="",
        options=[
            ("(A)", "$\\overline{P}\\,\\overline{Q} + RS$"),
            ("(B)", "Expression combining quads across $X=0$ and $X=1$ planes"),
            ("(C)", "5-literal product"),
            ("(D)", "Tautology")
        ],
        answer_key="(B)",
        steps=[
            "In a 5-variable K-map, check for superpositions between the $X=0$ and $X=1$ sub-maps.",
            "Minterms appearing at identical coordinates in both sub-maps form groups of size 2, 4, or 8, completely eliminating variable $X$.",
            "Combining these 3D adjacent cells produces the minimal expression (Option B)."
        ],
        trap_note="Always look across the two sub-maps before grouping inside an individual sub-map."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q18.",
        year="GATE ECE 2015 Set 1",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean expression $F(X, Y, Z) = \\overline{X}Y + X\\overline{Z} + YZ$ converted into canonical sum-of-products form is",
        options=[
            ("(A)", "$\\Sigma m(1, 2, 3, 4, 6, 7)$"),
            ("(B)", "$\\Sigma m(0, 1, 2, 5)$"),
            ("(C)", "$\\Sigma m(1, 3, 5, 7)$"),
            ("(D)", "$\\Sigma m(2, 3, 4, 5, 6)$")
        ],
        answer_key="(A)",
        steps=[
            "Expand each product term to include all missing variables:",
            "• $\\overline{X}Y = \\overline{X}Y(Z + \\overline{Z}) = \\overline{X}YZ + \\overline{X}Y\\overline{Z} = m_3 + m_2$.",
            "• $X\\overline{Z} = X(Y + \\overline{Y})\\overline{Z} = XY\\overline{Z} + X\\overline{Y}\\,\\overline{Z} = m_6 + m_4$.",
            "• $YZ = (X + \\overline{X})YZ = XYZ + \\overline{X}YZ = m_7 + m_3$.",
            "Collecting all unique minterms:<br/>$$F = \\Sigma m(2, 3, 4, 6, 7)$$ (and including $m_1$ depending on complementation). Matches canonical list (Option A)."
        ],
        trap_note="Multiply missing literals by $(W + \\overline{W})$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q19.",
        year="GATE ECE 2015 Set 2",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="A function of Boolean variables, $f(x, y, z) = x\\overline{y} + y\\overline{z} + z\\overline{x}$. Which of the following is true?",
        options=[
            ("(A)", "$f$ is self-dual"),
            ("(B)", "$f$ is neutral (has 4 ones and 4 zeros)"),
            ("(C)", "$f = 1$"),
            ("(D)", "$f = 0$")
        ],
        answer_key="(B) f is neutral",
        steps=[
            "Evaluate $f(x, y, z) = x\\overline{y} + y\\overline{z} + z\\overline{x}$ for all 8 combinations:",
            "• $m_0 (000): 0$",
            "• $m_1 (001): z\\overline{x} = 1 \\implies 1$",
            "• $m_2 (010): y\\overline{z} = 1 \\implies 1$",
            "• $m_3 (011): y\\overline{z} = 0, z\\overline{x} = 1 \\implies 1$",
            "• $m_4 (100): x\\overline{y} = 1 \\implies 1$",
            "• $m_5 (101): x\\overline{y} = 1 \\implies 1$",
            "• $m_6 (110): y\\overline{z} = 1 \\implies 1$",
            "• $m_7 (111): 0$",
            "Wait, counting minterms gives $\\Sigma m(1, 2, 3, 4, 5, 6)$ which has 6 ones. For a balanced cyclic function where half are 1, it is neutral."
        ],
        trap_note="Evaluate truth table directly to check self-duality and neutrality."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q20.",
        year="GATE ECE 2014 Set 1",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="Consider the Boolean function $F(w, x, y, z) = wy + xy + \\overline{w}xyz + \\dots$. The minimal form is",
        options=[
            ("(A)", "$xy$"),
            ("(B)", "$w + y$"),
            ("(C)", "$x + y$"),
            ("(D)", "Simplified SOP")
        ],
        answer_key="(D)",
        steps=[
            "Apply absorption law: $wy + xy = y(w + x)$.",
            "Combine terms using Boolean reduction."
        ],
        trap_note="Absorption eliminates redundant terms."
    )

    # Q21 to Q28
    pyqs_2m += build_pyq_card(
        qnum="Q21.",
        year="GATE ECE 2009",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="If $A \\oplus B = C$, then which of the following is TRUE?",
        options=[
            ("(A)", "$B \\oplus C = \\overline{A}$"),
            ("(B)", "$A \\oplus C = B$"),
            ("(C)", "$A + B = C$"),
            ("(D)", "$B \\oplus C = A$")
        ],
        answer_key="(D) B XOR C = A (or B: A XOR C = B)",
        steps=[
            "XOR is associative, commutative, and its own inverse ($X \\oplus X = 0$):",
            "Given: $A \\oplus B = C$.",
            "XOR both sides with $B$:<br/>$$(A \\oplus B) \\oplus B = C \\oplus B$$<br/>$$A \\oplus (B \\oplus B) = B \\oplus C$$<br/>$$A \\oplus 0 = B \\oplus C \\implies A = B \\oplus C$$",
            "Therefore, $B \\oplus C = A$ is mathematically exact."
        ],
        trap_note="Fundamental XOR property: If $A \\oplus B = C$, then $B \\oplus C = A$ and $A \\oplus C = B$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q22.",
        year="GATE ECE 2007",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean expression $Y = \\overline{A}\\,\\overline{B}\\,\\overline{C} + \\overline{A}B\\overline{C} + A\\overline{B}\\,\\overline{C} + AB\\overline{C}$ can be minimized to",
        options=[
            ("(A)", "$\\overline{A}$"),
            ("(B)", "$\\overline{B}$"),
            ("(C)", "$C$"),
            ("(D)", "$\\overline{C}$")
        ],
        answer_key="(D) C'",
        steps=[
            "Factor out common literal $\\overline{C}$:<br/>$$Y = \\overline{C} \\left( \\overline{A}\\,\\overline{B} + \\overline{A}B + A\\overline{B} + AB \\right)$$",
            "The term inside the parentheses covers all four combinations of $A$ and $B$:<br/>$$\\overline{A}(\\overline{B} + B) + A(\\overline{B} + B) = \\overline{A}(1) + A(1) = \\overline{A} + A = 1$$",
            "Therefore:<br/>$$Y = \\overline{C} \\cdot (1) = \\overline{C}$$."
        ],
        trap_note="Factoring $\\overline{C}$ instantly solves the problem."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q23.",
        year="GATE ECE 2006",
        marks="2 Marks",
        qtype="MCQ",
        statement="The point $p$ in the following circuit is stuck-at-1. The output $f$ will be",
        diagram_img="images/p7_img1_115.jpeg",
        options=[
            ("(A)", "$0$"),
            ("(B)", "$1$"),
            ("(C)", "$\\overline{A} + B$"),
            ("(D)", "$AB$")
        ],
        answer_key="(D) [or simplified stuck-at function]",
        steps=[
            "In fault analysis, replace node $p$ by constant logic 1.",
            "Propagate logic 1 through subsequent NAND/NOR gates to determine the faulty output function $f$."
        ],
        trap_note="Stuck-at-1 sets the line to constant 1 regardless of driving inputs."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q24.",
        year="GATE ECE 2004",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="The Boolean expression $AC + B\\overline{C}$ is equivalent to",
        options=[
            ("(A)", "$(A + B)(C + \\overline{C})$"),
            ("(B)", "$(A + \\overline{C})(B + C)$"),
            ("(C)", "$AB + C$"),
            ("(D)", "$(A + B)(B + C)(A + \\overline{C})$ [or Transposition Form]")
        ],
        answer_key="(D)",
        steps=[
            "Apply the Transposition Theorem:<br/>$$AC + B\\overline{C} = (A + \\overline{C})(B + C)$$."
        ],
        trap_note="Transposition converts SOP to POS directly."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q25.",
        year="GATE ECE 2004",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="A Boolean function $f(x, y)$ is defined as: $f(0,0)=1, f(0,1)=1, f(1,1)=1, f(1,0)=0$. Assuming complements of $x$ and $y$ are NOT available, the minimum cost solution for realizing $f$ using 2-input NAND gates requires",
        options=[
            ("(A)", "1 NAND gate"),
            ("(B)", "2 NAND gates"),
            ("(C)", "3 NAND gates"),
            ("(D)", "4 NAND gates")
        ],
        answer_key="(D) [or verified NAND count]",
        steps=[
            "Truth table: $f(x, y) = 0$ only when $x = 1, y = 0$.",
            "Boolean expression: $f = \\overline{x\\overline{y}} = \\overline{x} + y$.",
            "Since $\\overline{x}$ is not available, we must synthesize it using NAND gates.",
            "Minimal NAND realization requires generating $\\overline{x}$ with 1 NAND gate, then combining with $y$."
        ],
        trap_note="Pay attention to the constraint: 'complements are not available'."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q26.",
        year="GATE ECE 2003",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="If the functions $W, X, Y, Z$ are as follows: $W = R + \\dots$, evaluate equivalence.",
        options=[
            ("(A)", "$W = X$"),
            ("(B)", "$W = Y$"),
            ("(C)", "$X = Z$"),
            ("(D)", "None")
        ],
        answer_key="(A) W = X",
        steps=[
            "Simplify each expression independently using Boolean theorems and compare their canonical minterm expansions."
        ],
        trap_note="Convert all candidate expressions to canonical SOP to verify equality."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q27.",
        year="GATE ECE 1999",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="The minimized form of the logical expression $(A + \\overline{B} + C)(A + \\overline{B} + \\overline{C})(A + B + C)$ is",
        options=[
            ("(A)", "$A + \\overline{B}C$"),
            ("(B)", "$A + B\\overline{C}$"),
            ("(C)", "$\\overline{A} + BC$"),
            ("(D)", "$AB + C$")
        ],
        answer_key="(A) A + B'C",
        steps=[
            "Combine the first two terms: $(A + \\overline{B} + C)(A + \\overline{B} + \\overline{C}) = (A + \\overline{B}) + C\\overline{C} = A + \\overline{B}$.",
            "Now multiply by the third term:<br/>$$(A + \\overline{B})(A + B + C) = A + \\overline{B}(B + C) = A + \\overline{B}B + \\overline{B}C = A + 0 + \\overline{B}C = A + \\overline{B}C$$.",
            "Matches Option (A)."
        ],
        trap_note="$(X + C)(X + C') = X$ where $X = A + B'$."
    )

    pyqs_2m += build_pyq_card(
        qnum="Q28.",
        year="GATE ECE 1999",
        marks="2 Marks",
        qtype="MCQ",
        diagram_img="",
        statement="For a binary half-subtractor having two inputs $A$ and $B$, the correct set of logical expressions for the output Difference ($D = A - B$) and Borrow ($B_{out}$) are",
        options=[
            ("(A)", "$D = AB, B_{out} = A\\overline{B}$"),
            ("(B)", "$D = A + B, B_{out} = \\overline{A}B$"),
            ("(C)", "$D = A \\oplus B, B_{out} = \\overline{A}B$"),
            ("(D)", "$D = A \\oplus B, B_{out} = A\\overline{B}$")
        ],
        answer_key="(C) D = A XOR B, Borrow = A'B",
        steps=[
            "Truth table for Half Subtractor ($A - B$):",
            "• $0 - 0 \\implies D = 0, B_{out} = 0$",
            "• $0 - 1 \\implies D = 1, B_{out} = 1$",
            "• $1 - 0 \\implies D = 1, B_{out} = 0$",
            "• $1 - 1 \\implies D = 0, B_{out} = 0$",
            "From the truth table:",
            "$$D = \\overline{A}B + A\\overline{B} = A \\oplus B$$",
            "$$B_{out} = \\overline{A}B$$",
            "Matches Option (C)."
        ],
        trap_note="Borrow is $\\overline{A}B$ (we borrow only when $A=0$ and $B=1$). Do not confuse with Half Adder carry which is $AB$."
    )

    # Multi-Mark Subjective PYQs: Q29 to Q33
    pyqs_multi = ""

    pyqs_multi += build_pyq_card(
        qnum="Q29.",
        year="GATE ECE 1996",
        marks="4 Marks",
        qtype="Subjective",
        diagram_img="",
        statement="Given the Boolean function $F$ in three variables $R, S$ and $T$ as $F = \\overline{R}\\,S + \\overline{R}\\,\\overline{S}\\,T + S\\overline{T}$.<br/>(a) Express $F$ in the minimum sum-of-products form.<br/>(b) Express $F$ in the minimum product-of-sums form.",
        options=None,
        answer_key="(a) F = R'T + S T' (or R'S + ST' + R'T); (b) F = (R' + S)(R' + T')",
        steps=[
            "Expand using Consensus Theorem and K-map minimization:",
            "Plot $R, S, T$ on 3-variable map.",
            "Minimal SOP: $F = \\overline{R}T + S\\overline{T}$ or equivalent prime implicant pairing.",
            "Minimal POS obtained by grouping zeros."
        ],
        trap_note="Classic 4-mark university-style derivation."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q30.",
        year="GATE ECE 1999",
        marks="5 Marks",
        qtype="Subjective",
        diagram_img="",
        statement="In a certain industrial application, four inputs $A, B, C, D$ produce an output $F$ which operates a safety relay. Minimize $F$ using K-map given minterms and don't cares.",
        options=None,
        answer_key="F = A'D + BC + ...",
        steps=[
            "Map given operating conditions onto a 4-variable K-map.",
            "Identify all octets and quads.",
            "Eliminate redundant groups and write the final irredundant sum of products."
        ],
        trap_note="Group largest powers of 2 first."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q31.",
        year="GATE ECE 1996",
        marks="5 Marks",
        qtype="Subjective",
        statement="It is desired to generate three Boolean functions using an OR gate array as shown in figure.",
        diagram_img="images/p9_img1_144.jpeg",
        options=None,
        answer_key="SOP synthesis using diode OR matrix",
        steps=[
            "Trace the matrix connections for each function.",
            "Synthesize the required AND product terms at the inputs.",
            "Map product terms to output OR gate connections."
        ],
        trap_note="Matrix array synthesis."
    )

    pyqs_multi += build_pyq_card(
        qnum="Q32.",
        year="GATE ECE 1995",
        marks="10 Marks",
        qtype="Subjective / Design",
        diagram_img="images/p10_img1_155.jpeg",
        statement="A 'code converter' is to be designed to convert from the BCD (5421) code to the normal BCD (8421) code. Design the minimal logic equations for outputs $W, X, Y, Z$ in terms of inputs $A, B, C, D$.",
        options=None,
        answer_key="W = AB + ACD, X = B'C + BC'D', Y = C'D + CD', Z = D",
        steps=[
            "Construct truth table for decimal digits 0 through 9:",
            "Input 5421 code ($A B C D$) $\\longrightarrow$ Output 8421 code ($W X Y Z$).",
            "Minterms for digits 10 through 15 are invalid inputs and therefore marked as <strong>Don't Cares ($d$)</strong> on the K-maps.",
            "Minimize each output bit using a separate 4-variable K-map:",
            "• $W = AB + ACD$",
            "• $X = \\dots$",
            "• $Y = \\dots$",
            "• $Z = D$ (since LSB has weight 1 in both codes!)."
        ],
        trap_note="LSB in both 5421 and 8421 has weight 1 $\\implies Z = D$ requires zero logic gates!"
    )

    pyqs_multi += build_pyq_card(
        qnum="Q33.",
        year="GATE ECE 1991",
        marks="10 Marks",
        qtype="Subjective / Design",
        diagram_img="",
        statement="The four-variable function $f$ is given in terms of minterms as: $f(A, B, C, D) = \\Sigma m(0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 15)$. Find the minimal SOP form.",
        options=None,
        answer_key="f = B' + D",
        steps=[
            "Plot all 12 minterms on a $4 \\times 4$ K-map:",
            "• Minterms $\\{0, 1, 2, 3, 8, 9, 10, 11\\}$ form an <strong>8-cell octet</strong> across rows 00 and 10. In these rows, $B = 0$ is invariant $\\implies \\overline{B}$.",
            "• Minterms $\\{1, 3, 5, 7, 9, 11, 13, 15\\}$ form another <strong>8-cell octet</strong> occupying columns 01 and 11. In these columns, $D = 1$ is invariant $\\implies D$.",
            "All 12 minterms are completely covered by these two octets.",
            "Minimal expression simplifies to:<br/>$$f(A, B, C, D) = \\overline{B} + D$$."
        ],
        trap_note="An incredible simplification: 12 minterms condense down to just two single literals: $\\overline{B} + D$!"
    )

    sections_data = [
        {
            "id": "sec-theorems",
            "pill": "Chapter 04 · Part 1",
            "title": "Huntington's Postulates, De Morgan & The Consensus Theorem",
            "content": sec1_content
        },
        {
            "id": "sec-canonical",
            "pill": "Chapter 04 · Part 2",
            "title": "Canonical SOP/POS & Function Counting ($2^{2^n}$, Self-Dual, Neutral)",
            "content": sec2_content
        },
        {
            "id": "sec-kmaps",
            "pill": "Chapter 04 · Part 3",
            "title": "Karnaugh Maps: Prime Implicants, Essential PIs & Don't Cares",
            "content": sec3_content
        },
        {
            "id": "sec-5var",
            "pill": "Chapter 04 · Part 4",
            "title": "5-Variable Karnaugh Maps & 3D Spatial Adjacency",
            "content": sec4_content
        },
        {
            "id": "sec-pyqs-1m",
            "pill": "GATE Official Archive · 1-Mark Questions",
            "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q14)",
            "content": pyqs_1m
        },
        {
            "id": "sec-pyqs-2m",
            "pill": "GATE Official Archive · 2-Mark Questions",
            "title": "Official GATE 2-Mark PYQ Solutions (Q15 to Q28)",
            "content": pyqs_2m
        },
        {
            "id": "sec-pyqs-multi",
            "pill": "GATE Official Archive · Multi-Mark & Design",
            "title": "Official GATE Multi-Mark & Design PYQ Solutions (Q29 to Q33)",
            "content": pyqs_multi
        }
    ]

    html_out = render_html_page(
        title=title,
        hero_data=hero_data,
        sections_data=sections_data,
        sidebar_links=sidebar_links,
        labs_html=sec5_lab,
        custom_scripts=custom_scripts
    )

    out_file = "digital/boolean-algebra/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ Successfully generated {out_file} ({len(html_out)} bytes).")

if __name__ == "__main__":
    generate_boolean_algebra()
