# GTM Experiment Proof

A small, inspectable proof of how I translate a public GTM brief into a **real market experiment** without pretending that public signals equal buyer intent.

This repo was built for the MAXX Intelligence GTM Engineer role. The role emphasizes acquisition systems, enrichment, routing, sequencing, scoring, pipeline/attribution data, experiments, APIs/scripting, and lowering **cost per qualified conversation**.

The artifact is intentionally simple: a real target set, explicit evidence, current operators, deterministic routing, and a pre-declared experiment/kill condition.

## Live field-test offer

Want this applied to a real B2B offer?

See **[FIELD_TEST_OFFER.md](./FIELD_TEST_OFFER.md)**.

The current test is simple: send **one offer + one ICP** and I will manually return the first **5 evidence-backed accounts** with buyer, trigger, source, observed vs inferred reasoning, intervention, and a `READY / RESEARCH / REJECT` state.

No revenue or meeting guarantee is implied; the purpose is to test whether the account-selection and intervention quality is materially better than generic prospect research.

## What question does this answer?

> Given only public evidence, can I turn a broad ICP into a bounded, auditable outbound experiment with clear next actions — without fabricating intent, pain, or ROI?

This repo answers **yes** for the routing/experiment-design layer.

It does **not** claim that the target companies are buying, have the hypothesized pain, or will convert.

## Why recruitment as the wedge?

MAXX publicly describes business workflows around prospecting, follow-up, CRM, proposals, support, recruitment, and getting paid.

Recruitment/staffing firms are useful as a first test wedge because many publicly expose:

- multi-region operations,
- repeated candidate/client handoffs,
- high placement volume,
- multiple service lines,
- distributed teams/offices,
- recurring follow-up and coordination work.

Those signals make them **high-information targets to test**, not automatically qualified leads.

## Repo structure

```text
.
├── README.md
├── targets.csv
├── router.py
├── experiment.md
├── sample_output.txt
└── clara_interview.md
```

### `targets.csv`

Ten real companies with:

- company/domain
- company size and country
- public evidence
- exact source URL
- current operator
- operator LinkedIn
- an observable signal
- an explicitly **unverified** commercial hypothesis

The important distinction:

```text
PUBLIC SIGNAL != INTERNAL PAIN
PUBLIC SIGNAL != BUYING INTENT
PUBLIC SIGNAL != QUALIFIED OPPORTUNITY
```

The public signal only earns the right to ask a better question.

### `router.py`

A deliberately small deterministic router.

It does not use a fake “AI intent score.”

The rules are visible and inspectable:

- **PRIORITY** — mid-market + publicly visible workflow density
- **VALIDATE** — strong workflow-density signal, but smaller company
- **DEFER** — insufficient public workflow-density evidence
- **REJECT** — missing provenance, operator, or hypothesis

Run it with:

```bash
python router.py targets.csv
```

No external dependencies are required.

### `sample_output.txt`

The output from the included dataset.

Current result:

```text
PRIORITY = 7
VALIDATE = 2
DEFER = 1
REJECT = 0
```

That is **not** a conversion forecast.

It simply shows which targets survive the explicit routing rules.

### `experiment.md`

Defines the actual market test:

```text
public signal
→ current operator
→ one historical-behavior question
→ real workflow exposed?
→ consequence?
→ owner?
→ commitment?
→ continue / kill
```

A “qualified conversation” requires all of the following:

1. a concrete current workflow,
2. a repeated friction/failure or costly manual burden,
3. an identifiable owner,
4. willingness to take a meaningful next step.

“Sounds useful” does not count.

## The commercial hypothesis

The hypothesis is **not**:

> “These companies have broken workflows and need MAXX.”

The testable hypothesis is:

> Recruitment firms with visible workflow density are high-information targets for testing whether follow-up, routing, CRM state, proposal/admin work, or candidate/client communication is consequential enough to justify a MAXX companion.

That distinction is the core evidence discipline in this repo.

## Primary metric

```text
cost per qualified conversation
```

Useful decomposition:

```text
source
→ contacted
→ replied
→ problem validated
→ qualified conversation
→ next commitment
→ pipeline
```

Secondary measurements:

- contact → reply rate
- reply → validation rate
- validation → commitment rate
- operator time spent per account
- kill rate

## Kill condition

The experiment should be easy to invalidate.

If fewer than **2 of 10** accounts expose a consequential workflow after real operator conversations, the recruitment wedge should be retired or materially changed.

The purpose of the artifact is not to defend the hypothesis. It is to make the hypothesis cheap to test.

## How to interpret one row

Example logic:

```text
Petroplan
↓
public evidence: 10,000 placements / 55+ countries / 550+ clients
↓
current senior operator identified
↓
visible workflow density
↓
ROUTE: PRIORITY
↓
ask about the last real follow-up/routing/status-tracking event
↓
operator confirms or disproves the hypothesis
↓
seek a concrete next commitment or kill
```

The router does **not** conclude that Petroplan has a problem.

It concludes that Petroplan is worth a high-information validation attempt.

## Evidence state

Strictly:

```text
BUILT            = YES
TESTED           = YES, locally on the included dataset
EXTERNALLY USED  = NOT YET for this MAXX-specific experiment
PAID             = NO
```

The broader operating rule is:

```text
BUILT != TESTED != EXTERNALLY USED != PAID
```

## What this proves

This repo supports the following claims:

- I can translate a broad ICP into an explicit test wedge.
- I can research real companies and current operators.
- I preserve source provenance.
- I distinguish public evidence from internal assumptions.
- I can make routing logic deterministic and inspectable.
- I can define qualification criteria before outreach.
- I can define a kill condition before seeing the result.
- I can connect technical routing logic to a commercial metric.

## What this does NOT prove

This repo does not prove:

- current buying intent,
- internal workflow pain,
- product-market fit,
- revenue,
- pipeline creation,
- CAC reduction,
- conversion lift,
- successful MAXX deployment,
- production-scale enrichment,
- production CRM integration.

Those require external execution and measured outcomes.

## What I would add next in production

Only after real operator feedback:

1. verified email / phone channels,
2. live enrichment and timestamped signals,
3. outreach/call state,
4. reply classification,
5. problem-validation state,
6. next-commitment state,
7. pipeline/CRM writeback,
8. experiment attribution,
9. cost per qualified conversation,
10. outcome labels that could eventually justify learned scoring.

The sequence matters:

```text
manual signal
→ explicit rules
→ outcome data
→ only then smarter automation/scoring
```

## Design principle

The artifact is intentionally boring where “AI magic” would be fake.

Until enough labeled outcome data exists, transparent rules are more useful than a precise-looking score with no calibration.

The goal is not to make a lead list look intelligent.

The goal is to create a system that can be **wrong quickly, visibly, and usefully**.
