import os
from builder import render_html_page, build_pyq_card

# Chapter 1: Semiconductor Memories
def generate_semiconductor_memories():
    title = "GATE Master Textbook: Semiconductor Memories, SRAM, DRAM, ROM & PLDs"
    
    hero_data = {
        "title": "Semiconductor Memories, PLDs & Memory Interfacing",
        "subtitle": "Comprehensive GATE Master Notes covering SRAM (6T cell), DRAM (1T-1C cell & refresh), ROM diode arrays, PLD architectures (PROM, PAL, PLA), 2D memory decoders, and exhaustive derivations for all 12 official GATE PYQs.",
        "stats": [
            {"val": "12", "lbl": "Official GATE PYQs"},
            {"val": "1992 – 2021", "lbl": "Year Span Covered"},
            {"val": "6T vs 1T-1C", "lbl": "Core Cell Physics"},
            {"val": "100%", "lbl": "ExamGOAL Verified"}
        ]
    }
    
    sidebar_links = [
        {
            "title": "Theory & Fundamentals",
            "links": [
                {"id": "sec-overview", "text": "1. Memory Taxonomy & Organization"},
                {"id": "sec-sram", "text": "2. SRAM Cell Physics (6T)"},
                {"id": "sec-dram", "text": "3. DRAM Cell (1T-1C) & Refresh"},
                {"id": "sec-rom-pld", "text": "4. ROM & PLDs (PROM, PAL, PLA)"},
                {"id": "sec-decoding", "text": "5. 2D Decoding & Array Expansion"},
                {"id": "sec-lab", "text": "6. Memory Architect Simulator"}
            ]
        },
        {
            "title": "Official GATE PYQs",
            "links": [
                {"id": "sec-pyqs-1m", "text": "1-Mark Questions (Q1 - Q7)", "badge": "7 PYQs"},
                {"id": "sec-pyqs-2m", "text": "2-Mark Questions (Q8 - Q12)", "badge": "5 PYQs"}
            ]
        }
    ]
    
    # Section 1: Overview
    sec1_content = """
    <p>Semiconductor memories form the backbone of modern digital computing and microelectronic systems. In GATE ECE/EE/CS, questions rigorously evaluate memory hierarchy, internal cell topologies, timing constraints, array addressing, and programmable logic.</p>

    <h3 class="section-heading">Memory Taxonomy & Fundamental Classifications</h3>
    <p>Memory devices are fundamentally categorized along two axes: <strong>retention mechanism</strong> (volatile vs non-volatile) and <strong>access mode</strong> (random access vs sequential access).</p>
    
    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Static RAM (SRAM)</th>
            <th>Dynamic RAM (DRAM)</th>
            <th>Read-Only Memory (ROM)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Storage Cell</strong></td>
            <td>Cross-coupled CMOS latch (4T or 6T)</td>
            <td>Storage capacitor + 1 pass transistor (1T-1C)</td>
            <td>Fixed diode/transistor crosspoint array</td>
          </tr>
          <tr>
            <td><strong>Volatility</strong></td>
            <td>Volatile (loses data on power loss)</td>
            <td>Volatile (loses data on power loss)</td>
            <td>Non-Volatile (retains data permanently)</td>
          </tr>
          <tr>
            <td><strong>Refresh Requirement</strong></td>
            <td>None (static bistable state)</td>
            <td>Periodic refresh mandatory ($2 - 64\\text{ ms}$)</td>
            <td>None</td>
          </tr>
          <tr>
            <td><strong>Read Mechanism</strong></td>
            <td>Non-destructive differential sense</td>
            <td>Destructive (requires automatic rewrite)</td>
            <td>Non-destructive sense</td>
          </tr>
          <tr>
            <td><strong>Speed / Access Time</strong></td>
            <td>Ultra-fast ($0.5 - 5\\text{ ns}$)</td>
            <td>Moderate ($10 - 50\\text{ ns}$)</td>
            <td>Moderate to slow ($10 - 100\\text{ ns}$)</td>
          </tr>
          <tr>
            <td><strong>Packing Density & Cost</strong></td>
            <td>Low density (large cell area), High cost</td>
            <td>Ultra-high density, Low cost per bit</td>
            <td>Very high density, Low cost</td>
          </tr>
          <tr>
            <td><strong>Primary Application</strong></td>
            <td>CPU L1/L2/L3 Cache, Register files</td>
            <td>Main System Memory (DDR4/DDR5)</td>
            <td>Boot firmware (BIOS/UEFI), lookup tables</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout theory-box">
      <div class="theory-title">📌 Memory Capacity Mathematical Formulation</div>
      <p>For a memory organized as $M \\times N$ (where $M$ is the number of words, and $N$ is the word size in bits):</p>
      $$k = \\log_2(M) \\quad \\Longleftrightarrow \\quad M = 2^k \\text{ addressable locations}$$
      $$\\text{Total Capacity (Bits)} = M \\times N = 2^k \\times N$$
      $$\\text{Total Capacity (Bytes)} = \\frac{2^k \\times N}{8}$$
      <p>Here, $k$ input address lines are required to uniquely decode all $M$ word lines via a $k$-to-$2^k$ binary decoder.</p>
    </div>
    """

    # Section 2: SRAM
    sec2_content = """
    <p>A Static Random Access Memory (SRAM) stores each bit of information in a bistable latching circuit. Unlike dynamic RAM, it does not require periodic refreshing because the cross-coupled inverters continuously regenerate the stored charge via positive feedback.</p>

    <h3 class="section-heading">The 6T CMOS SRAM Cell Architecture</h3>
    <p>The standard full-CMOS SRAM cell comprises <strong>6 MOS transistors</strong>: two PMOS pull-up transistors ($P_1, P_2$), two NMOS pull-down transistors ($N_1, N_2$), and two NMOS access (pass-gate) transistors ($A_1, A_2$).</p>

    <div class="callout theory-box">
      <div class="theory-title">🔬 Transistor Breakdown of the 6T SRAM Cell</div>
      <ul>
        <li><strong>Inverter 1:</strong> Composed of $P_1$ and $N_1$, producing internal storage node $Q$.</li>
        <li><strong>Inverter 2:</strong> Composed of $P_2$ and $N_2$, producing complementary storage node $\\overline{Q}$.</li>
        <li><strong>Access Transistors ($A_1, A_2$):</strong> Connected between storage nodes and the differential bit lines ($BL, \\overline{BL}$), with gates driven by the <strong>Word Line ($WL$)</strong>.</li>
      </ul>
    </div>

    <h3 class="section-heading">Operational Cycles of the 6T SRAM Cell</h3>
    <ol>
      <li><strong>Standby / Retention ($WL = 0$):</strong> Access transistors $A_1, A_2$ are OFF. The cross-coupled inverters maintain stable states $Q$ and $\\overline{Q}$ powered by $V_{DD}$. Static power dissipation is limited purely to subthreshold leakage.</li>
      <li><strong>Read Cycle:</strong>
        <ul>
          <li>Both Bit Lines ($BL$ and $\\overline{BL}$) are precharged to $V_{DD}$.</li>
          <li>The Word Line ($WL$) is driven HIGH ($1$). Both access transistors $A_1, A_2$ turn ON.</li>
          <li>If $Q = 0$ and $\\overline{Q} = 1$, node $Q$ discharges $BL$ through $N_1$ and $A_1$. Meanwhile, $\\overline{BL}$ remains at $V_{DD}$.</li>
          <li>A sensitive analog <em>Sense Amplifier</em> detects the small differential voltage $\\Delta V = V_{BL} - V_{\\overline{BL}}$ (typically $50 - 100\\text{ mV}$) and converts it to a full CMOS digital level.</li>
          <li><strong>Non-destructive:</strong> The internal node values are never flipped during read if correctly sized ($\beta_{N1} > \beta_{A1}$, the cell ratio constraint).</li>
        </ul>
      </li>
      <li><strong>Write Cycle:</strong>
        <ul>
          <li>The write drivers drive the bit lines to the desired data: $BL = D$, $\\overline{BL} = \\overline{D}$.</li>
          <li>$WL$ is asserted HIGH. The strong write driver forces the internal node to flip, overpowering the PMOS pull-up transistor (pull-up ratio constraint: $\beta_{A1} > \beta_{P1}$).</li>
          <li>$WL$ returns LOW, locking the new state into the bistable latch.</li>
        </ul>
      </li>
    </ol>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Common GATE Examiner Trap: SRAM Transistor Count</div>
      <p>Exam questions frequently test: <em>"Each cell of a static RAM contains how many MOS transistors?"</em></p>
      <p>The answer is <strong>6 MOS transistors</strong> (4 NMOS + 2 PMOS). Older NMOS-only SRAMs used 4 NMOS with polysilicon pull-up resistors (4T cell), but modern and standard GATE syllabus questions define the full MOS SRAM cell as <strong>6 MOS transistors</strong> (GATE 1996, Q3).</p>
    </div>
    """

    # Section 3: DRAM
    sec3_content = """
    <p>Dynamic Random Access Memory (DRAM) achieves unmatched storage density by storing each bit of information as electric charge on an integrated capacitor ($C_s$).</p>

    <h3 class="section-heading">The 1T-1C DRAM Cell</h3>
    <p>A single dynamic RAM cell requires only <strong>1 MOS transistor and 1 storage capacitor</strong> (1T-1C topology):</p>
    <ul>
      <li><strong>Transistor ($M_1$):</strong> An NMOS pass transistor acting as a bidirectional transmission switch. Its gate is connected to the <strong>Word Line ($WL$)</strong>, and its drain is connected to the <strong>Bit Line ($BL$)</strong>.</li>
      <li><strong>Capacitor ($C_s$):</strong> A microscopic trench or stacked capacitor ($20 - 50\\text{ fF}$) connected between the source of $M_1$ and a reference plate voltage ($V_{DD}/2$).</li>
    </ul>

    <div class="callout theory-box">
      <div class="theory-title">⚡ Physics of Destructive Read & Charge Sharing</div>
      <p>When $WL$ goes HIGH, the charge on $C_s$ is dumped onto the precharged bit line with capacitance $C_{BL}$ ($C_{BL} \\gg C_s$, typically $10\\times$ to $20\\times$ larger). The resulting voltage perturbation on $BL$ is governed by charge conservation:</p>
      $$\\Delta V_{BL} = \\frac{C_s}{C_{BL} + C_s} \\left(V_s - \\frac{V_{DD}}{2}\\right)$$
      <p>Because the charge on $C_s$ is perturbed, the read operation is <strong>destructive</strong>. The sense amplifier must immediately restore (rewrite) full voltage back to $C_s$ before $WL$ closes!</p>
    </div>

    <h3 class="section-heading">Why Refreshing is Mandatory</h3>
    <p>Charge stored on the capacitor inevitably leaks away over time due to:</p>
    <ol>
      <li>Subthreshold leakage through the access transistor $M_1$.</li>
      <li>Reverse-bias p-n junction leakage between the diffusion node and substrate.</li>
      <li>Dielectric leakage through the capacitor insulator.</li>
    </ol>
    <p>To prevent catastrophic data loss, every row of the DRAM array must be read, amplified, and restored within the <strong>retention time</strong> ($t_{ref} \\approx 2\\text{ ms}$ to $64\\text{ ms}$). This periodic restoration is called <strong>DRAM Refreshing</strong>.</p>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Examiner Trap: Simultaneous Read and Write</div>
      <p>Can read and write operations be performed simultaneously in a standard single-port DRAM cell?</p>
      <p><strong>ABSOLUTELY NOT.</strong> Both read and write operations share the exact same physical bit line and sense amplifier. During read, the bit line is sensed and restored; a write operation requires driving the bit line externally. Simultaneous read and write on the same cell/bus is physically impossible (GATE 2017, Q1).</p>
    </div>
    """

    # Section 4: ROM & PLDs
    sec4_content = """
    <p>Read-Only Memories (ROM) and Programmable Logic Devices (PLDs) are combinational/sequential logic structures built from arrays of AND gates and OR gates.</p>

    <h3 class="section-heading">Diode ROM Matrix Operation</h3>
    <p>A diode ROM consists of orthogonal grid lines: horizontal <strong>Word Lines ($W_i$)</strong> and vertical <strong>Bit Lines ($B_j$)</strong> with pull-down resistors to ground:</p>
    <ul>
      <li>When word line $W_i$ is asserted HIGH, any intersection containing a forward-connected diode pulls bit line $B_j$ HIGH ($\text{Logic } 1$).</li>
      <li>If no diode is present at the intersection $(i, j)$, bit line $B_j$ remains pulled down to $0\\text{ V}$ by its resistor ($\text{Logic } 0$).</li>
      <li>Therefore: $\\text{Diode Present} \\implies D_{ij} = 1$; $\\text{No Diode} \\implies D_{ij} = 0$.</li>
    </ul>

    <h3 class="section-heading">Architectural Comparison of PLDs (PROM vs PAL vs PLA)</h3>
    <p>The three classical Programmable Logic Devices are characterized entirely by whether their constituent AND and OR arrays are fixed or programmable:</p>

    <div class="table-container">
      <table class="academic-table">
        <thead>
          <tr>
            <th>Device</th>
            <th>AND Array</th>
            <th>OR Array</th>
            <th>Minterm Generation</th>
            <th>Flexibility & Speed</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>PROM</strong> (Programmable ROM)</td>
            <td><strong>Fixed</strong> (Full binary decoder)</td>
            <td><strong>Programmable</strong></td>
            <td>Generates <em>all</em> $2^n$ canonical minterms</td>
            <td>Moderate speed; inefficient if only few minterms needed</td>
          </tr>
          <tr>
            <td><strong>PAL</strong> (Programmable Array Logic)</td>
            <td><strong>Programmable</strong></td>
            <td><strong>Fixed</strong></td>
            <td>Generates only required product terms</td>
            <td>Fastest (fixed OR gates have minimal capacitive load)</td>
          </tr>
          <tr>
            <td><strong>PLA</strong> (Programmable Logic Array)</td>
            <td><strong>Programmable</strong></td>
            <td><strong>Programmable</strong></td>
            <td>Generates custom product terms, shared across OR gates</td>
            <td>Highest logic density & flexibility; slightly slower</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout pro-tip">
      <div class="pro-tip-title">💡 GATE AIR 1 Mnemonic: "PROMs Fix the AND, PALs Fix the OR, PLAs Fix Nothing"</div>
      <p>Remember this simple rule:
      $$\\text{PROM: Fixed AND } + \\text{ Prog OR}$$
      $$\\text{PAL: Prog AND } + \\text{ Fixed OR}$$
      $$\\text{PLA: Prog AND } + \\text{ Prog OR}$$
      This exact distinction is tested repeatedly in GATE (GATE 1992 Q7, GATE 1994 Q5).</p>
    </div>
    """

    # Section 5: Decoders & Expansion
    sec5_content = """
    <p>Practical memory chips are organized as two-dimensional (2D) or 2.5D square arrays rather than long linear strips to minimize word line RC delay and decoder gate counts.</p>

    <h3 class="section-heading">2D Memory Organization (Row & Column Decoding)</h3>
    <p>For a memory storing $B$ total bits arranged as a square array with an aspect ratio of 1 (Number of Rows = Number of Columns):</p>
    $$N_{rows} = N_{cols} = \\sqrt{B}$$
    $$\\text{Row Address Lines } (k_r) = \\log_2(N_{rows}) = \\log_2(\\sqrt{B}) = \\frac{1}{2} \\log_2(B)$$
    $$\\text{Column Address Lines } (k_c) = \\log_2(N_{cols}) = \\frac{1}{2} \\log_2(B)$$

    <div class="callout theory-box">
      <div class="theory-title">📐 Example: 16 Kb Square Array (GATE 2015 Set 1, Q2)</div>
      <p>Given: Total bits $B = 16\\text{ Kb} = 16 \\times 1024 = 16,384\\text{ bits}$.</p>
      $$N_{rows} = \\sqrt{16,384} = 128\\text{ rows}$$
      $$k_r = \\log_2(128) = 7\\text{ address lines for the row decoder}$$
    </div>

    <h3 class="section-heading">Single Decoder vs 2D Decoding Gate Counts</h3>
    <p>When addressing a memory of $M = 2^k$ words using a <strong>single linear decoder</strong>:</p>
    <ul>
      <li>The decoder has $k$ inputs and $M = 2^k$ output word lines.</li>
      <li>Each output word line corresponds to one distinct minterm of the $k$ address bits.</li>
      <li>Therefore, the decoder requires exactly <strong>$2^k$ AND gates</strong> (each with $k$ inputs).</li>
    </ul>

    <div class="callout gate-trap">
      <div class="gate-trap-title">⚠️ Examiner Trap: Word Count vs Data Width in Decoder Sizing (GATE 2021, Q8)</div>
      <p>Consider a $32\\text{K} \\times 16$ memory chip:</p>
      <ul>
        <li>$32\\text{K} = 32 \\times 1024 = 2^5 \\times 2^{10} = 2^{15}$ words.</li>
        <li>The word size is 16 bits (each word has 16 data bits).</li>
        <li><strong>Question:</strong> How many AND gates are required for a single address decoder?</li>
        <li><strong>Trap:</strong> Many students erroneously use 16 (the data width) or combine address + data!</li>
        <li><strong>Correct:</strong> The address decoder only selects the <em>words</em> (rows)! With $2^{15}$ words, the single decoder requires $k = 15$ address lines and exactly <strong>$2^{15} = 32,768$ AND gates</strong>!</li>
      </ul>
    </div>
    """

    # Section 6: Interactive Lab
    sec6_lab = """
    <div id="sec-lab" class="lab-card">
      <div class="lab-header">
        <div class="lab-title">🧪 Interactive Memory Architect & Decoder Simulator</div>
        <span class="pill-badge pill-purple">Live Computational Engine</span>
      </div>
      <p>Enter your memory configuration parameters below to dynamically compute address bus width, single decoder AND gate count, square aspect ratio decoding, and multi-chip expansion requirements.</p>

      <div class="lab-input-grid">
        <div class="input-field">
          <label for="memWords">Word Capacity ($M$ words)</label>
          <select id="memWords">
            <option value="1024">1 K (1,024 words)</option>
            <option value="2048">2 K (2,048 words)</option>
            <option value="4096">4 K (4,096 words)</option>
            <option value="8192">8 K (8,192 words)</option>
            <option value="16384">16 K (16,384 words)</option>
            <option value="32768" selected>32 K (32,768 words)</option>
            <option value="65536">64 K (65,536 words)</option>
            <option value="1048576">1 M (1,048,576 words)</option>
          </select>
        </div>
        <div class="input-field">
          <label for="memDataBits">Word Width ($N$ bits)</label>
          <select id="memDataBits">
            <option value="1">1-bit</option>
            <option value="4">4-bit (Nibble)</option>
            <option value="8">8-bit (Byte)</option>
            <option value="16" selected>16-bit (Half-Word)</option>
            <option value="32">32-bit (Word)</option>
            <option value="64">64-bit (Double-Word)</option>
          </select>
        </div>
        <div class="input-field">
          <label for="targetCap">Target Expansion Capacity</label>
          <select id="targetCap">
            <option value="1">1x (Single Chip)</option>
            <option value="2">2x Word Expansion</option>
            <option value="4" selected>4x Word Expansion (Needs 2:4 Decoder)</option>
            <option value="8">8x Word Expansion (Needs 3:8 Decoder)</option>
          </select>
        </div>
      </div>

      <div id="memLabOutput" class="lab-output">
        Computing memory topology...
      </div>
    </div>
    """

    custom_scripts = """
    function updateMemLab() {
      const M = parseInt(document.getElementById('memWords').value, 10);
      const N = parseInt(document.getElementById('memDataBits').value, 10);
      const mult = parseInt(document.getElementById('targetCap').value, 10);
      
      const totalBits = M * N;
      const totalBytes = totalBits / 8;
      const addrLines = Math.round(Math.log2(M));
      const andGatesLinear = M;
      
      // Square array calculations
      const squareDim = Math.round(Math.sqrt(totalBits));
      const rowBits = Math.round(Math.log2(squareDim));
      const colBits = Math.round(Math.log2(totalBits / squareDim));
      
      // Expansion
      const expTotalWords = M * mult;
      const expAddrLines = Math.round(Math.log2(expTotalWords));
      const chipSelectBits = Math.round(Math.log2(mult));
      
      let outHtml = `<strong>[Memory Organization Breakdown]</strong><br/>`;
      outHtml += `• Base Chip Capacity: <strong>${M} words × ${N} bits</strong> = <strong>${totalBits.toLocaleString()} bits</strong> (${(totalBytes/1024).toFixed(2)} KB)<br/>`;
      outHtml += `• Address Bus Width: <strong>k = ${addrLines} address lines</strong> ($A_0$ to $A_{${addrLines-1}}$)<br/>`;
      outHtml += `• Single Linear Decoder Requirement: <strong>${andGatesLinear.toLocaleString()} AND gates</strong> (each with ${addrLines} inputs, $2^{${addrLines}}$ outputs)<br/><br/>`;
      
      outHtml += `<strong>[2D Square Array Geometry (Aspect Ratio = 1)]</strong><br/>`;
      outHtml += `• Array Dimensions: <strong>${squareDim} rows × ${Math.round(totalBits/squareDim)} columns</strong><br/>`;
      outHtml += `• Row Decoder: <strong>${rowBits} address lines</strong> → ${Math.pow(2, rowBits)} row outputs<br/>`;
      outHtml += `• Column Decoder/MUX: <strong>${colBits} address lines</strong> → ${Math.pow(2, colBits)} column outputs<br/><br/>`;
      
      outHtml += `<strong>[System Memory Expansion]</strong><br/>`;
      outHtml += `• Target Capacity: <strong>${expTotalWords.toLocaleString()} words × ${N} bits</strong><br/>`;
      outHtml += `• System Address Bus Width: <strong>${expAddrLines} lines</strong><br/>`;
      outHtml += `• High-Order Chip Select Lines: <strong>${chipSelectBits} lines</strong> ($A_{${expAddrLines-1}} - A_{${addrLines}}$) driving a <strong>${chipSelectBits}-to-${mult} Decoder</strong>`;
      
      document.getElementById('memLabOutput').innerHTML = outHtml;
    }
    document.getElementById('memWords').addEventListener('change', updateMemLab);
    document.getElementById('memDataBits').addEventListener('change', updateMemLab);
    document.getElementById('targetCap').addEventListener('change', updateMemLab);
    updateMemLab();
    """

    # Build PYQ Cards for Semiconductor Memories
    # 1-Mark Questions: Q1 to Q7
    pyqs_1m_html = ""
    
    # Q1
    q1 = build_pyq_card(
        qnum="Q1.",
        year="GATE ECE 2017 Set 2",
        marks="1 Mark",
        qtype="MCQ",
        statement="In a DRAM,",
        options=[
            ("(A)", "periodic refreshing is not required"),
            ("(B)", "information is stored in a capacitor"),
            ("(C)", "information is stored in a latch"),
            ("(D)", "both read and write operations can be performed simultaneously")
        ],
        answer_key="(B)",
        steps=[
            "Recall the physical architecture of a Dynamic Random Access Memory (DRAM) cell.",
            "A standard DRAM cell consists of a single access NMOS transistor and a storage capacitor (1T-1C structure).",
            "Data (logic 1 or logic 0) is stored as electrostatic charge $Q = C_s V$ on this microscopic capacitor ($C_s \\approx 20 - 50\\text{ fF}$).",
            "Because charge leaks over time through p-n junctions and subthreshold paths, periodic refreshing IS strictly required (invalidating Option A).",
            "Information stored in a cross-coupled latch characterizes an SRAM cell, not DRAM (invalidating Option C).",
            "Read and write share the same bitline and cannot be done simultaneously (invalidating Option D).",
            "Thus, statement (B) is the sole correct physical fact."
        ],
        trap_note="Do not confuse SRAM (stores in cross-coupled latch) with DRAM (stores charge on capacitor)."
    )
    pyqs_1m_html += q1

    # Q2
    q2 = build_pyq_card(
        qnum="Q2.",
        year="GATE ECE 2015 Set 1",
        marks="1 Mark",
        qtype="NAT",
        statement="A $16\\text{ Kb}$ ($= 16,384\\text{ bit}$) memory array is designed as a square with an aspect ratio of one (number of rows is equal to the number of columns). The minimum number of address lines needed for the row decoder is _______.",
        options=None,
        answer_key="7",
        steps=[
            "Total storage capacity in bits $B = 16\\text{ Kb} = 16,384\\text{ bits}$.",
            "Given aspect ratio $R = 1 \\implies \\text{Number of Rows } (N_R) = \\text{Number of Columns } (N_C)$.",
            "Since $B = N_R \\times N_C = N_R^2$, we calculate the number of rows:<br/>$$N_R = \\sqrt{16,384} = 128\\text{ rows}$$",
            "The row decoder must uniquely select one of these 128 rows.",
            "Number of address lines required for the row decoder $k_R = \\log_2(128) = \\log_2(2^7) = 7\\text{ lines}$."
        ],
        trap_note="Be careful with units: '16 Kb' means 16 Kilobits = 16,384 bits. Do not confuse with 16 KBytes (which would be $16 \\times 8 \\text{ Kb}$)."
    )
    pyqs_1m_html += q2

    # Q3
    q3 = build_pyq_card(
        qnum="Q3.",
        year="GATE ECE 1996",
        marks="1 Mark",
        qtype="MCQ",
        statement="Each cell of a static Random Access Memory Contains",
        options=[
            ("(A)", "6 MOS transistors."),
            ("(B)", "4 MOS transistors and 2 capacitors"),
            ("(C)", "2 MOS transistors and 4 capacitors"),
            ("(D)", "1 MOS transistors and 1 capacitors")
        ],
        answer_key="(A)",
        steps=[
            "Static RAM (SRAM) stores data without capacitors.",
            "The standard CMOS static memory cell consists of two cross-coupled CMOS inverters (each inverter has 1 PMOS and 1 NMOS = 4 transistors) plus two NMOS access/pass transistors controlled by the Word Line ($WL$).",
            "Total MOS transistors $= 2\\text{ PMOS} + 4\\text{ NMOS} = 6\\text{ MOS transistors}$."
        ],
        trap_note="Option D describes a DRAM cell (1 MOS transistor and 1 capacitor). SRAM cells use zero capacitors."
    )
    pyqs_1m_html += q3

    # Q4
    q4 = build_pyq_card(
        qnum="Q4.",
        year="GATE ECE 1995",
        marks="1 Mark",
        qtype="MCQ",
        statement="The minimum number of MOS transistors required to make a dynamic RAM cell is",
        options=[
            ("(A)", "1"),
            ("(B)", "2"),
            ("(C)", "3"),
            ("(D)", "4")
        ],
        answer_key="(A)",
        steps=[
            "A standard modern dynamic RAM (DRAM) cell uses the 1T-1C architecture.",
            "This consists of exactly <strong>1 MOS access transistor</strong> and 1 storage capacitor.",
            "Thus, the minimum number of MOS transistors required is 1."
        ],
        trap_note="Early DRAMs historically used 3-transistor cells (3T DRAM), but the modern minimum tested in GATE is 1 transistor."
    )
    pyqs_1m_html += q4

    # Q5
    q5 = build_pyq_card(
        qnum="Q5.",
        year="GATE ECE 1994",
        marks="1 Mark",
        qtype="MCQ",
        statement="A PLA can be used",
        options=[
            ("(A)", "as a microprocessor"),
            ("(B)", "as a dynamic memory"),
            ("(C)", "to realize a sequential logic"),
            ("(D)", "to realize a combinational logic")
        ],
        answer_key="(D)",
        steps=[
            "A PLA (Programmable Logic Array) consists of a programmable AND array followed by a programmable OR array.",
            "This two-level structure directly implements arbitrary Boolean sum-of-products (SOP) expressions.",
            "Hence, it is fundamentally used to realize combinational logic circuits."
        ],
        trap_note="While sequential PLAs exist (Registered PLAs with flip-flops), a standard fundamental PLA is a combinational logic device."
    )
    pyqs_1m_html += q5

    # Q6
    q6 = build_pyq_card(
        qnum="Q6.",
        year="GATE ECE 1994",
        marks="1 Mark",
        qtype="MCQ",
        statement="A dynamic RAM consists of",
        options=[
            ("(A)", "6 transistors"),
            ("(B)", "2 transistors and 2 capacitor"),
            ("(C)", "1 transistors and 1 capacitor"),
            ("(D)", "2 capacitor only")
        ],
        answer_key="(C)",
        steps=[
            "A dynamic RAM bit cell stores data in the 1T-1C configuration.",
            "It consists of 1 access NMOS transistor and 1 storage capacitor."
        ],
        trap_note="Compare directly with Q3: SRAM = 6 transistors; DRAM = 1 transistor + 1 capacitor."
    )
    pyqs_1m_html += q6

    # Q7
    q7 = build_pyq_card(
        qnum="Q7.",
        year="GATE ECE 1992",
        marks="1 Mark",
        qtype="MSQ / Multi-Answer",
        statement="Choose the correct statement(s) from the following:",
        options=[
            ("(A)", "PROM contains a programmable AND array and a fixed OR array."),
            ("(B)", "PLA contains a fixed AND array and a programmable OR array"),
            ("(C)", "PROM contains a fixed AND array and a programmable OR array"),
            ("(D)", "PLA contains a programmable AND array and a programmable OR array")
        ],
        answer_key="(C) and (D)",
        steps=[
            "Let us evaluate the structure of each Programmable Logic Device:",
            "1. <strong>PROM:</strong> Consists of a full decoder (Fixed AND array generating all $2^n$ minterms) and a <strong>Programmable OR array</strong>. Hence (C) is TRUE and (A) is FALSE.",
            "2. <strong>PAL:</strong> Consists of a Programmable AND array and a Fixed OR array.",
            "3. <strong>PLA:</strong> Consists of a <strong>Programmable AND array</strong> and a <strong>Programmable OR array</strong>. Hence (D) is TRUE and (B) is FALSE.",
            "Therefore, both (C) and (D) are correct statements."
        ],
        trap_note="Remember: PLA has BOTH arrays programmable. PROM has fixed AND (decoder) + programmable OR."
    )
    pyqs_1m_html += q7

    # 2-Mark Questions: Q8 to Q12
    pyqs_2m_html = ""

    # Q8
    q8 = build_pyq_card(
        qnum="Q8.",
        year="GATE ECE 2021",
        marks="2 Marks",
        qtype="MCQ",
        statement="Addressing of a $32\\text{K} \\times 16$ memory is realized using a single decoder. The minimum number of AND gates required for the decoder is :",
        options=[
            ("(A)", "$2^4$"),
            ("(B)", "$2^8$"),
            ("(C)", "$2^{16}$"),
            ("(D)", "$2^{15}$")
        ],
        answer_key="(D) $2^{15}$",
        steps=[
            "Analyze the memory specifications: $32\\text{K} \\times 16$.",
            "This memory has $32\\text{K}$ addressable words, where each word is 16 bits wide.",
            "Calculate the number of address lines $k$ required to uniquely select each word:<br/>$$M = 32\\text{K} = 32 \\times 1024 = 2^5 \\times 2^{10} = 2^{15} \\text{ words} \\implies k = 15 \\text{ address lines}$$",
            "A single decoder decoding $k$ input address lines must produce $2^k$ distinct output word-select lines.",
            "Each output line corresponds to one unique minterm, which requires one AND gate.",
            "Therefore, the minimum number of AND gates required for the decoder is $2^{15} = 32,768$."
        ],
        trap_note="Do NOT get confused by the word length '16'. The decoder decodes the word address ($2^{15}$), NOT the data bits! Hence the answer is $2^{15}$, not $2^{16}$."
    )
    pyqs_2m_html += q8

    # Q9
    q9 = build_pyq_card(
        qnum="Q9.",
        year="GATE ECE 2018",
        marks="2 Marks",
        qtype="MCQ",
        statement="A $2 \\times 2$ ROM array is built with the help of diodes as shown in the circuit below. Here $W_0$ and $W_1$ are signals that select the word lines and $B_0$ and $B_1$ are signals that are output of the sense amps based on the stored data corresponding to the bit lines during the read operation.<br/><br/>During the read operation, the selected word line goes high and the other word line is in a high impedance state. As per the implementation shown in the circuit diagram above, what are the bits corresponding to $D_{ij}$ (where $i = 0$ or $1$ and $j = 0$ or $1$) stored in the ROM?",
        diagram_img="images/img_p3_1_73.png",
        options=[
            ("(A)", "$[D_{00}, D_{01}, D_{10}, D_{11}] = [1, 0, 0, 1]$"),
            ("(B)", "$[D_{00}, D_{01}, D_{10}, D_{11}] = [0, 1, 1, 0]$"),
            ("(C)", "$[D_{00}, D_{01}, D_{10}, D_{11}] = [1, 1, 0, 0]$"),
            ("(D)", "$[D_{00}, D_{01}, D_{10}, D_{11}] = [0, 0, 1, 1]$")
        ],
        answer_key="(A) [1, 0, 0, 1]",
        steps=[
            "Inspect the diode matrix schematic at each grid intersection $(i, j)$ where $i$ is the word line index ($W_0, W_1$) and $j$ is the bit line index ($B_0, B_1$):",
            "1. <strong>Row 0 ($W_0$ selected HIGH):</strong>",
            "   - At intersection $(0, 0)$, a diode connects $W_0$ (anode) to $B_0$ (cathode). When $W_0$ is HIGH, the diode conducts, pulling $B_0$ HIGH $\\implies D_{00} = 1$.",
            "   - At intersection $(0, 1)$, there is NO diode between $W_0$ and $B_1$. Hence $B_1$ remains at pull-down ground potential $\\implies D_{01} = 0$.",
            "2. <strong>Row 1 ($W_1$ selected HIGH):</strong>",
            "   - At intersection $(1, 0)$, there is NO diode between $W_1$ and $B_0$. $B_0$ remains at ground $\\implies D_{10} = 0$.",
            "   - At intersection $(1, 1)$, a diode connects $W_1$ (anode) to $B_1$ (cathode). When $W_1$ is HIGH, the diode conducts, pulling $B_1$ HIGH $\\implies D_{11} = 1$.",
            "3. Assembling the stored bits matrix:<br/>$$D = \\begin{bmatrix} D_{00} & D_{01} \\\\ D_{10} & D_{11} \\end{bmatrix} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$$",
            "Hence, the stored bits are $[1, 0, 0, 1]$ corresponding to Option (A)."
        ],
        trap_note="Diode anode is on Word Line, cathode is on Bit Line. When Word Line is HIGH, diode conducts $\\implies$ Bit Line is 1. No diode $\\implies$ Bit Line pulled down to 0."
    )
    pyqs_2m_html += q9

    # Q10
    q10 = build_pyq_card(
        qnum="Q10.",
        year="GATE ECE 2014 Set 3",
        marks="2 Marks",
        qtype="MCQ",
        statement="If $WL$ is the Word Line and $BL$ the Bit Line, an SRAM cell is shown in",
        diagram_img="images/img_p4_2_87.png",
        options=[
            ("(A)", "Circuit with NMOS load cross-coupled to Bit lines"),
            ("(B)", "Circuit with cross-coupled CMOS inverters and NMOS pass gates to $BL$ and $\\overline{BL}$ driven by $WL$"),
            ("(C)", "Circuit with dynamic capacitor storage"),
            ("(D)", "Single inverter feedback loop")
        ],
        answer_key="(B)",
        steps=[
            "The standard 6T CMOS SRAM cell consists of two cross-coupled CMOS inverters.",
            "Each inverter is formed by a PMOS pull-up connected to $V_{DD}$ and an NMOS pull-down connected to Ground.",
            "The output of the first inverter drives the input of the second, and vice-versa, creating a bistable storage latch with nodes $Q$ and $\\overline{Q}$.",
            "Two NMOS pass (access) transistors have their gates driven by the Word Line ($WL$).",
            "One access transistor connects node $Q$ to the Bit Line ($BL$), and the other connects node $\\overline{Q}$ to the complementary Bit Line ($\\overline{BL}$).",
            "Circuit (B) exactly depicts this classic symmetric 6T CMOS SRAM cell configuration."
        ],
        trap_note="Ensure access gates are tied to Word Line ($WL$), NOT Bit Line! Word line controls whether the cell is selected."
    )
    pyqs_2m_html += q10

    # Q11
    q11 = build_pyq_card(
        qnum="Q11.",
        year="GATE ECE 2003",
        marks="2 Marks",
        qtype="MCQ",
        statement="In the circuit shown in Figure, A is a parallel-in, parallel-out 4-bit register, which loads at the rising edge of the clock $C$. The input lines are connected to a 4-bit bus, $W$. Its output acts as the input to a $16 \\times 4$ ROM whose output is floating when the enable input $E$ is 0. A partial table of the contents of the ROM is as follows:<br/>• Address 0110 (6) $\\to$ Data 1000<br/>• Address 1000 (8) $\\to$ Data 1011<br/><br/>The clock to the register is shown, and the data on the $W$ bus at time $t_1$ is $0110$. The data on the bus at time $t_2$ is",
        diagram_img="images/img_p5_2_100.jpeg",
        options=[
            ("(A)", "1111"),
            ("(B)", "1011"),
            ("(C)", "1000"),
            ("(D)", "0010")
        ],
        answer_key="(C) 1000",
        steps=[
            "Trace the sequential timing cycle through the register and ROM:",
            "1. <strong>Initial state before $t_1$:</strong> Bus $W$ carries data $0110_2$ (decimal 6).",
            "2. <strong>At time $t_1$ (First rising edge of clock $C$):</strong>",
            "   - Register A loads the data currently present on the $W$ bus.",
            "   - Output of Register A becomes $0110_2$.",
            "   - This output immediately applies address $0110_2$ to the address inputs of the $16 \\times 4$ ROM.",
            "3. <strong>During the high phase between $t_1$ and $t_2$:</strong>",
            "   - When the ROM enable input $E$ is activated, the ROM accesses location $0110_2$.",
            "   - From the provided ROM lookup table, location $0110_2$ contains data: <strong>1000</strong>.",
            "   - The ROM drives this data (1000) onto the $W$ bus.",
            "4. <strong>At time $t_2$ (Second rising edge of clock $C$):</strong>",
            "   - Right at the instant of $t_2$, the data present on the $W$ bus is the ROM output from address $0110$, which is <strong>1000</strong>.",
            "Hence, the data on the bus at time $t_2$ is 1000 (Option C)."
        ],
        trap_note="Do not look ahead to the next cycle! At time $t_2$, the register is just beginning to sample $1000$; therefore the bus holds 1000, NOT the data at address 1000 (which is 1011)."
    )
    pyqs_1m_html_blank = False
    pyqs_2m_html += q11

    # Q12
    q12 = build_pyq_card(
        qnum="Q12.",
        year="GATE ECE 2002",
        marks="2 Marks",
        qtype="MCQ",
        statement="If the input $X_3, X_2, X_1, X_0$ to the ROM in figure are 8-4-2-1 BCD numbers, then the outputs $Y_3, Y_2, Y_1, Y_0$ are",
        diagram_img="images/img_p6_1_108.jpeg",
        options=[
            ("(A)", "gray code numbers"),
            ("(B)", "2-4-2-1 BCD numbers"),
            ("(C)", "excess-3 code numbers"),
            ("(D)", "none of the above.")
        ],
        answer_key="(B) 2-4-2-1 BCD numbers",
        steps=[
            "Analyze the circuit diagram: An input BCD digit $X_3 X_2 X_1 X_0$ (weights 8-4-2-1) is decoded into decimal lines 0 to 9 via a BCD-to-Decimal decoder.",
            "The decoder outputs drive the word lines of a diode/ROM matrix that encodes output bits $Y_3, Y_2, Y_1, Y_0$.",
            "Evaluate the ROM mapping for decimal inputs 0 through 9:",
            "• Decimal 0 to 4: Output is identical to binary/BCD ($0000$ to $0100$).",
            "• Decimal 5: Encoded as $1011_2$ (Weight $2+0+2+1 = 5$).",
            "• Decimal 6: Encoded as $1100_2$ (Weight $2+4+0+0 = 6$).",
            "• Decimal 7: Encoded as $1101_2$ (Weight $2+4+0+1 = 7$).",
            "• Decimal 8: Encoded as $1110_2$ (Weight $2+4+2+0 = 8$).",
            "• Decimal 9: Encoded as $1111_2$ (Weight $2+4+2+1 = 9$).",
            "Notice that the code is self-complementing and uses bit weights $2, 4, 2, 1$ (the Aiken code).",
            "Therefore, the ROM implements conversion from standard 8-4-2-1 BCD to <strong>2-4-2-1 BCD code</strong>."
        ],
        trap_note="Excess-3 code for decimal 0 would be 0011, but here decimal 0 produces 0000. Hence it cannot be Excess-3. It is 2-4-2-1 self-complementary BCD."
    )
    pyqs_2m_html += q12

    sections_data = [
        {
            "id": "sec-overview",
            "pill": "Chapter 01 · Part 1",
            "title": "Semiconductor Memory Taxonomy & Capacity Mathematics",
            "content": sec1_content
        },
        {
            "id": "sec-sram",
            "pill": "Chapter 01 · Part 2",
            "title": "Static RAM (SRAM): The 6T CMOS Cell & Operational States",
            "content": sec2_content
        },
        {
            "id": "sec-dram",
            "pill": "Chapter 01 · Part 3",
            "title": "Dynamic RAM (DRAM): 1T-1C Cell, Destructive Read & Refreshing",
            "content": sec3_content
        },
        {
            "id": "sec-rom-pld",
            "pill": "Chapter 01 · Part 4",
            "title": "ROM Arrays & Programmable Logic Devices (PROM, PAL, PLA)",
            "content": sec4_content
        },
        {
            "id": "sec-decoding",
            "pill": "Chapter 01 · Part 5",
            "title": "2D Coincident Decoding, Aspect Ratios & Array Expansion",
            "content": sec5_content
        },
        {
            "id": "sec-pyqs-1m",
            "pill": "GATE Official Archive · 1-Mark Questions",
            "title": "Official GATE 1-Mark PYQ Solutions (Q1 to Q7)",
            "content": pyqs_1m_html
        },
        {
            "id": "sec-pyqs-2m",
            "pill": "GATE Official Archive · 2-Mark Questions",
            "title": "Official GATE 2-Mark PYQ Solutions (Q8 to Q12)",
            "content": pyqs_2m_html
        }
    ]

    html_out = render_html_page(
        title=title,
        hero_data=hero_data,
        sections_data=sections_data,
        sidebar_links=sidebar_links,
        labs_html=sec6_lab,
        custom_scripts=custom_scripts
    )
    
    out_file = "digital/semiconductor-memories/notes.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"✓ Successfully generated {out_file} ({len(html_out)} bytes).")

if __name__ == "__main__":
    generate_semiconductor_memories()
