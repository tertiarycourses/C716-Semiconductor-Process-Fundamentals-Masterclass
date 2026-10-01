# Learner Guide — Semiconductor Process Fundamentals Masterclass (C716)

Version 1.0 · 1 October 2026 · Tertiary Infotech Academy Pte Ltd

## How to Use This Guide

This guide holds the detailed procedures intentionally omitted from the concept-led slide deck. Work through the eight activities in sequence, keep evidence in the named folder, and use acceptance criteria before moving to the next integration decision.

| Field | Details |
|---|---|
| Course | Semiconductor Process Fundamentals Masterclass |
| Course code | C716 |
| Duration | 15 hours over 2 days (9:30am–5:30pm) |
| LMS | https://lms-tms.tertiaryinfotech.com/ |

## Learning Outcomes

- LO1: Identify process flows and modules for specific CMOS technologies in manufacturing.
- LO2: Determine CMOS device performance and verify process integration in accordance with product specifications.

## Before You Start - What You Need

- The current v1.0 learner slides and this Learner Guide.
- The complete activities/ folder with Markdown/PDF resources and Excel workbooks.
- Microsoft Excel or compatible spreadsheet software with automatic calculation enabled.
- A drawing tool or A3 paper for process maps and integration diagrams.
- Access to the LMS for courseware download.

## Topic 1 - CMOS Process Modules and Process Flow

### Learning Block 1A - Patterning, Etch and Fab Control

Build reliable patterns while controlling contamination, CD, overlay and profile.

#### The Wafer Fab as a System

- Product flow: hundreds of tightly coupled operations
- Cleanroom: particles and molecular contamination are controlled
- Integration: each module owns incoming and outgoing evidence
- Release logic: a pass is a measured decision, not an assumption

#### Contamination Has Multiple Pathways

- Particles: block patterns and create opens or shorts
- Ions: shift electrical behaviour and junction properties
- Organics: interfere with adhesion, exposure and interfaces
- Water and tools: transport hidden contamination between modules

#### The Lithography Stack

- Mask or reticle carries the intended geometry
- Resist converts optical energy into a soluble contrast
- Alignment connects the current level to prior levels
- Developed resist becomes the etch or implant mask

#### Mask Tone and Resist Tone

- Clear-field and dark-field masks invert where light passes
- Positive resist removes exposed regions
- Negative resist retains exposed regions
- The combination determines whether a hole or island remains

#### Resist Coating and Bake

- Prime improves adhesion on the prepared surface
- Spin speed and dispense control resist thickness
- Soft bake removes solvent without damaging image response
- Edge bead and coverage affect focus and defectivity

#### Resolution, NA and Process Margin

- Wavelength: shorter light supports smaller features
- Numerical aperture: higher NA improves resolution
- Depth of focus: normally shrinks as NA rises
- Usable window: pitch, resist and variation set margin

#### Overlay, OPC and Mask Protection

- Overlay error shifts one layer against another
- OPC pre-distorts features to counter imaging effects
- Antireflective layers reduce standing-wave effects
- Pellicles and inspection reduce repeating defects

#### Wet Etch versus Dry Etch

- Wet etch is often isotropic and can undercut
- Plasma/RIE supports directional profiles
- Chemistry controls material reaction
- Bias, pressure and transport influence sidewalls and damage

#### Etch Selectivity and Profile

- Selectivity protects resist and stop layers
- Over-etch clears residual film but consumes margin
- Microloading makes local pattern density matter
- Endpoint and cross-section evidence localise failure

#### Strip and Clean

- Wet strip dissolves resist where surfaces tolerate chemistry
- Dry strip removes organics but can damage sensitive layers
- RCA-type cleans target particles, organics and metals
- Drying must avoid watermarking and recontamination

#### Pattern-Transfer Window

- Lithography CD sets the incoming geometry
- Etch bias changes the final feature
- Across-wafer signatures expose non-uniformity
- Pre- and post-etch metrology localises the dominant shift

#### Patterning Evidence Gate

- Geometry: CD, overlay and profile
- Defects: bridge, open, pinhole, residue or collapse
- Mechanism: exposure, develop, etch or clean
- Action: release, conditional release, hold or scrap

### Learning Block 1B - Implant, Thermal, Films and Integrated Flow

Control material modification, film formation, planarity and FEOL-to-BEOL hand-offs.

#### Implant Dose and Energy

- Dose controls total implanted ions
- Energy controls the depth distribution
- Tilt and twist reduce channeling and shadowing
- Uniform scanning protects within-wafer consistency

#### Beamline Risks

- Charging can deflect beams or damage dielectrics
- Channeling produces unexpectedly deep tails
- Mask topography creates shadowed regions
- Beam focus and scan strategy affect uniformity

#### Crystal Damage and Activation

- Implant collisions create vacancies and interstitials
- Anneal repairs lattice damage
- Activation places dopants on useful sites
- Electrical improvement can coexist with diffusion

#### Diffusion, Furnace and RTP

- Furnace cycles favour batch throughput and long soak
- RTP uses fast ramps and short dwell
- Thermal budget controls activation and junction movement
- The best cycle balances electrical target with geometry

#### Thermal Oxidation

- Silicon is consumed as silicon dioxide grows
- Dry oxidation grows slowly with strong film quality
- Wet oxidation grows faster for thicker films
- Temperature, time and surface condition control integrity

#### CVD, PECVD and Epitaxy

- CVD: film forms through surface reactions
- PECVD: plasma lowers process temperature
- Epitaxy: deposited crystal follows the substrate lattice
- Selection: conformality, stress, purity and thermal budget

#### PVD, Barrier and Seed

- Sputtering transports target atoms to the wafer
- Directional coverage challenges deep features
- Barrier films limit metal diffusion
- Continuous seed enables uniform electrofill

#### Copper Dual Damascene

- Pattern vias and trenches in dielectric
- Deposit liner, barrier and seed
- Electrofill copper without seams or voids
- Polish overburden while protecting pattern density

#### CMP Mechanics and Chemistry

- Pad contact and slurry chemistry work together
- Downforce, speed and pad state affect removal
- Selectivity protects stop layers
- Post-CMP clean removes abrasive and metal residue

#### Planarity Failure Modes

- Dishing removes too much metal in wide features
- Erosion lowers dense pattern regions
- Incomplete clear leaves conductive residue
- Topography and electrical continuity must both pass

#### Integrated FEOL and BEOL

- Isolation and wells define device regions
- Gate and source/drain form transistors
- Contacts and interconnect create connectivity
- Passivation and wafer sort close wafer fabrication

#### Cross-Module Budgeting

- Thermal budget accumulates across later steps
- Topography changes the next lithography window
- Contamination transfers through surfaces and tools
- Every hand-off needs evidence and an owner

## Topic 2 - CMOS Process Integration and Performance

### Learning Block 2A - Integration Performance, Yield and Reliability

Use metrology, electrical data and reliability evidence to verify product performance.

#### Isolation and Well Integration

- LOCOS is simple but creates bird's-beak encroachment
- STI supports scaling through etched and filled trenches
- Well architecture controls body regions
- Stress, CD and topography affect device behaviour

#### Transistor Formation

- Gate stack sets electrostatic control
- Source/drain implants establish junctions
- Spacers sequence extension and deep implants
- Contacts must preserve silicide and junction integrity

#### Yield Is Multiplicative

- Wafer-fab yield reflects process survival
- Wafer-sort yield reflects functional die
- Packaging yield reflects assembly and final test
- One stage can erase gains made at another

#### Defect Density and Die Area

- Larger die expose more area to random defects
- Clustered defects violate simple random assumptions
- Systematic defects need separate treatment
- Yield models support prediction, not proof

#### Metrology by Question

- Ellipsometry: thin-film thickness and optics
- Profilometry/AFM: step height and topography
- SEM/TEM: CD, profile and internal structure
- SIMS/Auger: concentration and surface composition

#### Measurement Strategy

- Before and after: isolate the suspected module
- Spatial map: expose centre-edge or chamber signatures
- Resolution: match instrument to the feature
- Correlation: connect physical and electrical evidence

#### Electrical Performance

- Four-point probe measures sheet resistance
- Gate-oxide integrity tests dielectric weakness
- I-V curves reveal threshold, leakage and drive
- Product specifications decide pass/fail

#### Reliability Evidence

- Mechanism explains degradation
- Accelerated stress creates measurable change
- Failure criterion defines the endpoint
- Physical confirmation links failure to cause

#### HCI, TDDB and Electromigration

- Hot carriers damage the channel interface
- TDDB accumulates dielectric damage over time
- Electromigration moves metal under current density
- Geometry, material and temperature change lifetime

#### Control Limits versus Specifications

- Control limits describe process behaviour
- Specification limits describe product requirements
- A stable process may still be off target
- An in-spec point can signal a process shift

#### Capability: Cp and Cpk

- Cp compares specification width with spread
- Cpk also reflects centering
- Capability follows stability assessment
- Use the approved threshold and risk context

#### Evidence-Based Release

- Define the product requirement
- Select physical and electrical evidence
- Compare with limits and uncertainty
- Document disposition and follow-up

### Learning Block 2B - SPC, Packaging and Future Integration

Control excursions, close the feedback loop and evaluate next-generation choices.

#### SPC as a Feedback System

- Sample the process with a rational subgroup
- Plot performance against behaviour-based limits
- Detect special-cause signals
- Contain risk and restore control with evidence

#### Select the Chart from the Data

- Variable data: measurements such as CD
- Attribute data: counts or proportions
- Subgroup size decides Xbar-R versus Xbar-S
- Opportunity and sample size decide p, np, c or u

#### Variable Control Charts

- Xbar tracks subgroup centre
- R or S tracks within-subgroup spread
- The two charts answer different questions
- A mean chart is incomplete without spread

#### Attribute Control Charts

- p chart: proportion defective, variable sample size
- np chart: defective count, constant sample size
- c chart: defect count, constant opportunity
- u chart: defects per unit, variable opportunity

#### Signals Beyond One Point

- A point beyond a limit is a strong signal
- Runs and trends expose non-random change
- Stratification reveals tool, wafer or time source
- Rules must be defined before interpretation

#### Excursion Response

- Contain: hold material and preserve evidence
- Stratify: tool, chamber, wafer, product and time
- Correct: controlled change with rollback criteria
- Verify: stable behaviour and capability

#### Packaging Process Flow

- Prepare and thin wafer
- Separate, inspect and attach die
- Create electrical interconnect
- Seal, plate, final-test and burn-in as required

#### Wire Bond and Flip Chip

- Wire bond is flexible but adds loop length
- Flip chip raises I/O density
- Underfill and joint quality manage mechanical risk
- Inspection and test protect assembly yield

#### 2.5D, 3D and Chiplets

- Interposers connect multiple dies
- 3D stacks use vertical connections
- Known-good-die and thermal design are inputs
- Integration control crosses organisations

#### FinFET

- A fin raises the channel above substrate
- Multiple gate surfaces improve control
- Fin geometry and parasitics affect performance
- Patterning and variability challenge manufacturing

#### GAAFET Nanosheets

- Gate surrounds the channel
- Stacked sheets increase effective width
- Release, inner spacer and contacts are critical
- Metrology must resolve buried geometry

#### Beyond Today's CMOS

- Vertical transistors change current direction
- 2D materials offer ultrathin channels
- Quantum devices require cryogenic control
- Every concept still needs capability and reliability gates

## Detailed Step-by-Step Activities

### Activity 1 - Build a CMOS Process Module Map

| Field | Details |
|---|---|
| Goal | Organise the legacy module coverage into a defensible FEOL-to-BEOL flow and expose the interfaces that can propagate variation. |
| Scenario | A new 300 mm logic product is moving from process development into a pilot manufacturing line. The integration team needs one agreed process map before module owners set recipes and control plans. |
| Alignment | LO1 |
| Duration | 45 minutes |
| Folder | activities/activity-01-process-module-map/ |

#### What You Need

- Activity worksheet and evidence template in this folder
- Learner slides covering wafer fab, photolithography, etch, implant, thermal, film, CMP and integrated flows
- A3 paper or a digital drawing tool

#### Step-by-Step

1. Open the worksheet and write the target product assumptions: substrate type, logic technology family and the intended final device outcome.
2. Create seven module lanes: photolithography, etch/clean, ion implantation, diffusion/RTP, film deposition, CMP and metrology/control.
3. Place the major FEOL stages in order: wafer preparation, isolation, well formation, gate stack, source/drain formation and contacts.
4. Add the BEOL stages: dielectric deposition, via/trench patterning, barrier/seed, metal fill, CMP, passivation and wafer sort.
5. For each hand-off, identify the incoming measurable characteristic, such as CD, overlay, film thickness, dose, sheet resistance or surface planarity.
6. Mark at least three feedback loops where metrology can cause hold, rework, recipe correction or engineering disposition.
7. Circle two interactions where a change in one module can create a downstream electrical or yield effect.
8. Check the map against the provided process-flow slides and correct missing or duplicated stages.
9. Export or photograph the final map and name the evidence file A01-process-map.

#### Acceptance Criteria

- [ ] The map contains all seven key process modules and distinguishes FEOL from BEOL.
- [ ] At least eight process hand-offs have a measurable characteristic.
- [ ] At least three control/feedback loops and two cross-module interactions are justified.

#### Reflection and Evidence

- Which module has the greatest ability to propagate a hidden defect downstream, and why?
- What evidence would allow the integration owner to release the lot to the next module?
Save the completed evidence with the A01- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 2 - Diagnose a Pattern-Transfer Process Window

| Field | Details |
|---|---|
| Goal | Connect mask/resist/exposure decisions to etch profile and select a stable corrective action without masking the root cause. |
| Scenario | A contact layer shows intermittent bridging and open defects. Lithography CD, resist profile and plasma-etch selectivity must be reviewed together rather than as isolated module results. |
| Alignment | LO1 |
| Duration | 60 minutes |
| Folder | activities/activity-02-pattern-transfer-window/ |

#### What You Need

- Pattern-transfer worksheet and process-window workbook
- Legacy diagrams on resist polarity, Rayleigh resolution, OPC, selectivity and anisotropy
- Calculator or spreadsheet software

#### Step-by-Step

1. Review the defect images in the worksheet and classify each as bridge, open, incomplete etch, undercut or resist-collapse risk.
2. Open pattern-transfer-window.xlsx and read the focus, exposure dose, post-develop CD and post-etch CD observations.
3. Mark cells that violate the target post-etch CD range of 88-112 nm.
4. Compare the lithography CD bias with the post-etch CD bias to decide whether the dominant shift occurs before or during etch.
5. Check whether edge cells fail more often than centre cells; record the spatial signature.
6. Select one lithography lever (focus, dose, resist thickness or bake) and one etch lever (gas ratio, bias power, pressure or over-etch).
7. Predict the intended effect and one possible side effect for each lever.
8. Write a confirmation plan using CD-SEM before etch, CD-SEM after etch and profile inspection on a cross-section.
9. Record a release decision: accept, conditional release, hold for engineering, or scrap.

#### Acceptance Criteria

- [ ] Every defect is linked to a plausible lithography/etch mechanism.
- [ ] The dominant CD-shift stage is supported by before/after evidence.
- [ ] Corrective levers include predicted benefit, risk and verification measurement.

#### Reflection and Evidence

- Why can improving resolution reduce depth of focus?
- When does additional over-etch protect yield, and when does it create reliability risk?
Save the completed evidence with the A02- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 3 - Balance Implantation and Thermal Budget

| Field | Details |
|---|---|
| Goal | Create an implant-to-anneal decision trail that balances activation, junction depth, damage recovery and channeling risk. |
| Scenario | After a source/drain extension implant, sheet resistance is above target and short-channel control is drifting. The team must distinguish dose/energy error from activation and diffusion effects. |
| Alignment | LO1 |
| Duration | 60 minutes |
| Folder | activities/activity-03-implant-thermal-budget/ |

#### What You Need

- Implant and RTP data cards in the worksheet
- Legacy diagrams for beam scanning, channeling, damage and RTP
- Evidence template

#### Step-by-Step

1. Read the target dose, implant energy, tilt/twist, sheet resistance and junction-depth specifications.
2. Compare actual dose and energy with the target and note whether the deviation can explain the electrical signature.
3. Inspect the channeling indicator and decide whether tilt/twist or an amorphising layer should be reviewed.
4. Use the damage/activation card to separate as-implanted lattice damage from electrically active dopant.
5. Compare the furnace and RTP thermal cycles by peak temperature, dwell time and ramp rate.
6. Predict how each thermal cycle affects activation, lateral diffusion and junction depth.
7. Choose a containment action for the current lot and a recipe action for the next engineering split.
8. Define the minimum verification set: sheet resistance map, SIMS profile or junction-depth proxy, and electrical monitor.
9. Complete the risk statement: action, expected benefit, possible adverse effect and stop condition.

#### Acceptance Criteria

- [ ] The recommendation distinguishes implant dose/energy, damage and activation mechanisms.
- [ ] Thermal-budget effects on activation and diffusion are explicit.
- [ ] Follow-up measurements can confirm or reject the proposed cause.

#### Reflection and Evidence

- Why does a shorter high-temperature RTP cycle often protect shallow junctions?
- How can a sheet-resistance improvement still hide a device-performance problem?
Save the completed evidence with the A03- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 4 - Integrate Film Deposition and CMP

| Field | Details |
|---|---|
| Goal | Trace deposition, fill and CMP interactions and design a verification plan that protects both planarity and electrical performance. |
| Scenario | A dual-damascene copper level meets line-resistance targets at wafer centre but fails near the edge with dishing, erosion and suspected barrier continuity loss. |
| Alignment | LO1 |
| Duration | 60 minutes |
| Folder | activities/activity-04-film-cmp-integration/ |

#### What You Need

- Cross-section cards and film/CMP worksheet
- Legacy diagrams for barrier/seed, copper fill, slurry, polishing and post-CMP clean
- Evidence template

#### Step-by-Step

1. Label the dielectric, barrier/liner, seed, copper fill and overburden layers on the supplied cross-section.
2. Identify which layer prevents diffusion and which layer enables electroplating continuity.
3. Compare centre and edge thickness/planarity observations and classify dishing, erosion or incomplete clear.
4. Trace how PVD coverage or electroplating voids can change the apparent CMP result.
5. Choose two CMP inputs to review: downforce, platen speed, pad condition, slurry chemistry, flow or polish time.
6. For each input, state the expected effect on removal rate, selectivity and within-wafer uniformity.
7. Add a post-CMP clean and contamination-control check to the integration plan.
8. Define metrology at three points: pre-CMP overburden, post-CMP topography and electrical line/via continuity.
9. Write a hold/release rule based on planarity plus electrical evidence.

#### Acceptance Criteria

- [ ] The layer stack and each module's function are correctly labelled.
- [ ] The analysis distinguishes deposition/fill causes from polishing causes.
- [ ] The release rule uses both physical and electrical evidence.

#### Reflection and Evidence

- Why can a visually planar surface still fail electrical verification?
- Which measurement best distinguishes dishing from incomplete copper clear?
Save the completed evidence with the A04- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 5 - Review an STI Integration Flow

| Field | Details |
|---|---|
| Goal | Produce the process-flow and challenge analysis for a shallow trench isolation integration. |
| Scenario | TechSemicon is introducing shallow trench isolation for an advanced CMOS product. Electrical spread and active-area CD variation appear after integration, and the review board needs a complete process/evidence chain. |
| Alignment | LO2 |
| Duration | 75 minutes |
| Folder | activities/activity-05-sti-integration-review/ |

#### What You Need

- STI process cards, worksheet and evidence template
- Legacy LOCOS/STI, lithography, etch, CVD and CMP slides
- A3 paper or digital flow-diagram tool

#### Step-by-Step

1. Arrange the STI cards in order: pad oxide, nitride deposition, lithography, trench etch, liner oxidation, trench fill, CMP and nitride strip.
2. For each step, write the purpose, key input and outgoing measurable characteristic.
3. Add pre-clean and post-CMP clean controls at the correct points.
4. Mark the interfaces where active-area CD, trench depth/profile, voiding, dishing/erosion and stress can be introduced.
5. Connect each risk to one suitable measurement such as CD-SEM, cross-section SEM/TEM, film thickness, topography or electrical isolation test.
6. Compare STI with LOCOS and state why STI supports scaling despite its integration challenges.
7. Choose two control points for a pilot-line hold/release plan.
8. Draw the final simplified flow without referring to the cards.
9. Use the checklist to review completeness, sequence and evidence traceability.

#### Acceptance Criteria

- [ ] The eight core STI stages are in the correct order and have a purpose.
- [ ] At least four implementation challenges are linked to measurements.
- [ ] The flow explains both scaling benefit and integration risk.

#### Reflection and Evidence

- Which STI step most directly controls active-area CD?
- How can CMP-induced topography alter a later lithography process window?
Save the completed evidence with the A05- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 6 - Analyse Yield and Process Capability

| Field | Details |
|---|---|
| Goal | Recreate and improve the legacy ProcessCapability exercise using an auditable Excel workbook with dynamic formulas. |
| Scenario | A gate module has a target CD of 100 nm with specification limits at 90 and 110 nm. The process owner needs Cp/Cpk evidence and a reasoned yield-risk statement before qualification. |
| Alignment | LO2 |
| Duration | 75 minutes |
| Folder | activities/activity-06-yield-capability-analysis/ |

#### What You Need

- ProcessCapability.xlsx in this folder
- Legacy Cp/Cpk, sigma, yield and defect-density slides
- Worksheet and evidence template

#### Step-by-Step

1. Open ProcessCapability.xlsx and read the Instructions sheet before changing any inputs.
2. Go to Data and confirm the 30 hardcoded CD observations are shown in blue text.
3. Review the Analysis formulas for mean, sample standard deviation, Cp and Cpk; do not replace formulas with values.
4. Compare the mean with the 100 nm target and describe accuracy (centering).
5. Compare the standard deviation with the specification width and describe precision (spread).
6. Interpret Cp as potential capability and Cpk as actual capability considering centering.
7. Change one blue input value to 118 nm and observe how the metrics and out-of-spec count recalculate; then restore the value.
8. Use the histogram and capability summary to decide capable, conditionally capable or not capable.
9. Record one containment action and one long-term process action.
10. Export the Analysis sheet to PDF or capture a screenshot named A06-capability-evidence.

#### Acceptance Criteria

- [ ] Workbook formulas remain intact and show no Excel errors.
- [ ] The learner distinguishes Cp from Cpk and links both to process evidence.
- [ ] The decision includes containment, corrective action and verification.

#### Reflection and Evidence

- Why can Cp be acceptable while Cpk is unacceptable?
- Why does a capability index not prove that the process is statistically stable?
Save the completed evidence with the A06- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 7 - Respond to an SPC CD Excursion

| Field | Details |
|---|---|
| Goal | Recreate the legacy P-chart/SPC exercises and generate the corrective-action chain for a CD excursion. |
| Scenario | STI active-area CD is drifting across production lots. A point crosses the upper control limit and a seven-point upward run appears before the alarm. The team must contain risk and restore control. |
| Alignment | LO2 |
| Duration | 90 minutes |
| Folder | activities/activity-07-spc-cd-excursion/ |

#### What You Need

- SPCdata.xlsx and p_Chart.xlsx in this folder
- Legacy control-limit, Xbar/R, p/c/u-chart and out-of-control rule slides
- Corrective-action worksheet and evidence template

#### Step-by-Step

1. Open SPCdata.xlsx and review the raw subgroup CD data, timestamps, tool IDs and lot IDs.
2. Check that subgroup means and ranges use formulas and that the chart updates when a blue input changes.
3. Identify the first out-of-control point and the earlier non-random run signal.
4. Separate control limits from product specification limits in the worksheet.
5. Write the immediate containment actions: stop/hold affected lots, preserve evidence, notify ownership and prevent automatic release.
6. Stratify the data by tool/chamber, wafer position, product and time to narrow the source.
7. Review lithography focus/dose, etch endpoint/profile and metrology calibration as candidate causes.
8. Define confirmation measurements using pre-etch CD, post-etch CD and cross-section profile evidence.
9. Select a corrective action and a controlled engineering split; state the rollback trigger.
10. Verify recovery using consecutive stable subgroups and an updated capability check.
11. Open p_Chart.xlsx and repeat the logic for variable sample sizes using defect proportion rather than CD measurements.
12. Export the SPC evidence and complete the follow-up action record.

#### Acceptance Criteria

- [ ] The response identifies both limit violation and non-random pattern.
- [ ] Containment precedes root-cause adjustment and protects affected lots.
- [ ] Corrective action, verification criteria and follow-up owner are explicit.

#### Reflection and Evidence

- Why must the team investigate a non-random run even when all points remain inside control limits?
- Which chart is appropriate for CD measurements, and which is appropriate for defect proportions?
Save the completed evidence with the A07- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

### Activity 8 - Run a Future-Technology Integration Gate

| Field | Details |
|---|---|
| Goal | Combine the entire course into a structured technology-gate recommendation without treating future devices as isolated marketing concepts. |
| Scenario | A product team is deciding whether to adopt chiplet packaging, FinFET or GAAFET for its next platform. Integration readiness must be assessed using process, performance, reliability and packaging evidence. |
| Alignment | LO2 |
| Duration | 60 minutes |
| Folder | activities/activity-08-technology-integration-gate/ |

#### What You Need

- Technology-gate worksheet and evidence template
- Legacy packaging, heterogeneous integration, chiplet, FinFET, GAAFET, vertical transistor and 2D-material slides
- Outputs from Activities 1-7

#### Step-by-Step

1. Choose one candidate: chiplet integration, FinFET scaling or GAAFET scaling.
2. List the required process modules and identify which existing modules need a new material, geometry, tool or control method.
3. Map three critical cross-module interactions and the performance metric each can affect.
4. Define device metrics (for example leakage, drive current, resistance or capacitance) and reliability metrics relevant to the candidate.
5. Add packaging/interconnect implications, including thermal, mechanical and known-good-die considerations where applicable.
6. Create a five-row evidence gate: process capability, metrology readiness, electrical performance, reliability and yield/manufacturability.
7. Set a pass/conditional/fail threshold for every gate.
8. Identify the largest uncertainty and design the smallest engineering experiment that can reduce it.
9. Present a recommendation: proceed, proceed with conditions, or defer.
10. Record the next owner, due date and evidence required to close the decision.

#### Acceptance Criteria

- [ ] The recommendation integrates process, device, reliability, yield and packaging evidence.
- [ ] Every gate has a measurable threshold and an accountable follow-up action.
- [ ] The conclusion is conditional on evidence rather than technology hype.

#### Reflection and Evidence

- Which legacy process controls remain useful for the chosen technology?
- What new metrology or reliability evidence is essential before volume manufacturing?
Save the completed evidence with the A08- prefix and record the final release/hold/recommendation decision in evidence-template.pdf or evidence-template.md.

## Quick Reference

| Field | Details |
|---|---|
| Pattern transfer | Mask/resist -> expose/develop -> inspect CD -> etch -> strip/clean -> verify profile |
| Implant/thermal | Dose/energy/tilt -> implant -> damage/channeling check -> anneal/RTP -> sheet resistance/profile verification |
| Film/CMP | Surface prep -> barrier/seed or film -> fill/deposition -> thickness/profile -> CMP -> clean -> electrical verification |
| SPC response | Contain -> stratify -> confirm -> correct -> verify -> document follow-up |
| Capability | Establish stability first; then compare Cp and Cpk against the approved threshold |
| Evidence | Use the measurement that can distinguish competing causes, not merely the easiest available measurement |

## Support

Email enquiry@tertiaryinfotech.com or call +65 6100 0613. Course page: https://www.tertiarycourses.com.sg/semiconductor-process-fundamentals-masterclass.html

