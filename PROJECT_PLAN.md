# US Healthcare Backend — Sampurna Roadmap (Django REST Framework)

> Ha document tula reference mhanun aahe. Kधीhi confuse zala tar ithe parat ye.
> Goal: US Healthcare EHR backend, **basic te advanced**, step by step.

---

## 1. Apan kay banavat aahot? (Big picture)

Ek **EHR (Electronic Health Record)** backend. Mhanje hospital cha sagla data —
patients, doctors, appointments, diagnoses, prescriptions, insurance claims,
billing — he sagle **API** dwara manage karaycha. **Frontend nahi**, fakt API.

API mhanje? Doosre apps (mobile app, website, doosri hospital cha system) apan
banavlelya backend shi "baat" kartat HTTP requests dwara. Apan tya requests la
JSON madhe answer deto.

### US Healthcare domain madhe importance terms (he shikne mahattvache):
| Term | Marathi/Simple artha |
|------|----------------------|
| **MRN** | Medical Record Number — pratyek patient cha unique ID |
| **EHR** | Electronic Health Record — patient cha sampurna digital record |
| **ICD-10** | Diagnosis (rog) chе standard codes — jagभर vapartat |
| **Encounter** | Ek hospital visit / bhet (doctor la bhetane) |
| **Claim** | Insurance company kade paise maagnyacha request |
| **Payer** | Insurance company (jo paise deto) |
| **FHIR** | Healthcare data exchange cha jagatik standard format |
| **HIPAA** | US cha kaida — patient data private thevaycha niyam |
| **RBAC** | Role-Based Access Control — kon kay baghu shakto |

---

## 2. Tech Stack (apan kay kay vaaprणार)

| Layer | Tool | Ka? |
|-------|------|-----|
| Language | Python 3.13 | ✅ Already installed |
| Web framework | Django 5.x | Powerful, "batteries included" |
| API framework | Django REST Framework (DRF) | API banavnyasathi best |
| Database | PostgreSQL (Docker madhe) | Production-grade DB |
| Auth | JWT (djangorestframework-simplejwt) | Token-based login |
| API Docs | drf-spectacular (Swagger) | Auto API documentation |
| Async jobs | Celery + Redis | Background kaam (nantar) |
| Container | Docker + docker-compose | DB ani app chalvnyasathi |
| Testing | pytest + DRF test client | Code barobar aahe ka check |

---

## 3. Folder Structure (project kasa disel)

```
USHealthCare Hospital System/
│
├── docker-compose.yml          # PostgreSQL + Redis + app chalvnyasathi
├── Dockerfile                  # App cha image
├── requirements.txt            # Python packages list
├── .env                        # Secrets (passwords, keys) — git madhe nako
├── .gitignore
├── manage.py                   # Django cha main command tool
│
├── config/                     # Project settings (heart of project)
│   ├── settings/
│   │   ├── base.py             # Common settings
│   │   ├── dev.py              # Development settings
│   │   └── prod.py             # Production settings
│   ├── urls.py                 # Sagle URL ithe join hotat
│   ├── celery.py
│   └── wsgi.py
│
├── apps/                       # Sagle modules (Django "apps")
│   ├── users/                  # Login, roles, permissions
│   ├── patients/               # Patient records, MRN
│   ├── providers/              # Doctors, nurses
│   ├── appointments/           # Booking, reschedule, cancel
│   ├── encounters/             # Visit records
│   ├── diagnoses/              # ICD-10 codes
│   ├── medications/            # Prescriptions
│   ├── allergies/
│   ├── labs/                   # Lab orders + results
│   ├── insurance/              # Payers, eligibility
│   ├── claims/                 # Insurance claims
│   ├── billing/                # Invoices, payments
│   ├── documents/              # PDFs, clinical summaries
│   ├── audit_logs/             # Kon ne kay baghla
│   ├── notifications/
│   ├── fhir/                   # FHIR standard endpoints
│   ├── sso/                    # OAuth2 / OpenID login
│   └── integrations/           # External systems (PointClickCare)
│
└── tests/                      # Tests
```

### Pratyek app cha aat kay astа? (Django pattern)
```
patients/
├── models.py        # Database tables (Python class = SQL table)
├── serializers.py   # JSON <-> Python data convert karto
├── views.py         # API logic (request aali ki kay karaycha)
├── urls.py          # Kuthlya URL la konti view
├── services.py      # Business logic (MRN generate vagaire)
├── filters.py       # Search/filter logic
├── admin.py         # Django admin panel madhe dakhavayla
└── tests/           # Ya app che tests
```

**Concept clear kar:** Django madhe data 4 layer madhun jato —
```
Request → URL → View → Serializer → Model → Database
                  ↓
              Service (business logic)
```

---

## 4. Build Phases (12 weeks — basic te advanced)

### 🟢 PHASE 1 — Foundation (Week 1)
**Goal:** Project chalu hoil, "Hello API" disel, PostgreSQL connect hoil.
- [ ] Virtual environment + packages install
- [ ] Django project + config/ structure banavne
- [ ] docker-compose ne PostgreSQL chalvne
- [ ] DRF setup + pahili test API
- [ ] Swagger docs chalu karne (/api/docs/)
- [ ] API versioning (/api/v1/) + consistent error format

### 🟢 PHASE 2 — Authentication + RBAC (Week 2)
**Goal:** Users register/login karu shaktil, roles asthil.
- [ ] Custom User model (email ne login)
- [ ] Roles: Admin, Doctor, Nurse, Patient, Integration User
- [ ] JWT login/refresh (/auth/login, /auth/refresh)
- [ ] Register API (/auth/register)
- [ ] Permission classes (kon kay karu shakto)
- [ ] **Domain:** Healthcare madhe role kiti important — Nurse la prescription nahi deta yet, Doctor la yeto

### 🟡 PHASE 3 — Patients (Week 3)
**Goal:** Patient cha record CRUD + MRN.
- [ ] Patient model (demographics, contact, emergency contact)
- [ ] **MRN auto-generate** (unique medical record number)
- [ ] CRUD APIs (Create, Read, Update, Delete)
- [ ] Search APIs (naav, MRN, DOB ne shodhne)
- [ ] Pagination, filtering, sorting

### 🟡 PHASE 4 — Appointments (Week 4)
**Goal:** Appointment book/reschedule/cancel/complete.
- [ ] Appointment model (patient + provider + time)
- [ ] Status workflow: scheduled → completed / cancelled
- [ ] Double-booking prevention (validation)
- [ ] Provider availability check

### 🟡 PHASE 5 — Encounters + Diagnoses (Week 5)
- [ ] Encounter model (ek visit cha record)
- [ ] ICD-10 code catalog
- [ ] Patient la diagnosis attach karne
- [ ] Encounter shi diagnosis/medication/labs jodne

### 🟡 PHASE 6 — Medications + Labs (Week 6)
- [ ] Prescription management
- [ ] Medication history
- [ ] Allergy tracking (medication shi conflict check)
- [ ] Lab orders + results

### 🟠 PHASE 7 — Insurance (Week 7)
- [ ] Payer (insurance company) details
- [ ] Member ID, policy info
- [ ] Eligibility tracking

### 🟠 PHASE 8 — Claims + Billing (Week 8)
- [ ] Claim model + workflow (create → submit → paid/rejected)
- [ ] Invoice generation
- [ ] Payment tracking, balances
- [ ] **Domain:** Claim lifecycle US healthcare cha core aahe

### 🟠 PHASE 9 — Documents (Week 9)
- [ ] Document push API
- [ ] PDF generation (clinical summary, discharge summary)
- [ ] S3-style file storage

### 🔴 PHASE 10 — OAuth2 + SSO (Week 10)
- [ ] OAuth2 Authorization Code flow
- [ ] OpenID Connect
- [ ] /oauth/login, /oauth/callback

### 🔴 PHASE 11 — FHIR (Week 11)
- [ ] FHIR Patient, Encounter, Observation endpoints
- [ ] MedicationRequest, Condition resources
- [ ] **Domain:** FHIR mule doosrya hospitals shi data exchange hoto

### 🔴 PHASE 12 — Polish + Deploy (Week 12)
- [ ] Audit logs (HIPAA requirement)
- [ ] Celery + Redis (background jobs)
- [ ] Full Swagger documentation
- [ ] Testing (unit + API + integration)
- [ ] Docker production setup + Nginx + Gunicorn

🟢 = Easy/Foundation | 🟡 = Core | 🟠 = Business logic | 🔴 = Advanced

---

## 5. Pratyek phase madhe apan kasa kaam karu

1. **Domain samjavin** — ha module healthcare madhe ka lagto
2. **Model lihu** — database table design
3. **Serializer + View + URL** — API banavu
4. **Swagger madhe test** — browser madhun API chalvun baghu
5. **Pudhcha module**

Ekach veli sagla code nahi — chota chota, samjun samjun.

---

## 6. Important sवायी (habits — professional developer banaaychа aahe)

- ✅ Pratyek module nantar **test** kar (Swagger/Postman)
- ✅ **Git** vaapr — pratyek phase nantar commit
- ✅ Secrets (.env) kधीhi git madhe taku nako
- ✅ Comments lihi — 3 mahin nantar tula tujha code samajla pahije
- ✅ Error aala tar **ghabru nako** — error message vaach, to tula sangtoy kay chuk aahe

---

## NEXT STEP
Ha plan vaach. Mag apan **Phase 1 (Foundation)** suru karu —
virtual environment, Django install, PostgreSQL Docker setup, ani pahili API.
