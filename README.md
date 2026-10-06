# Hospital-App
# 🏥 PediaCare – Pediatric Hospital Management System

PediaCare is a **Pediatric Hospital Management System** designed to simplify and digitize the management of children's healthcare services. The application focuses on helping pediatricians and hospital staff manage child patient information, appointments, medical records, vaccinations, prescriptions, and growth monitoring through a centralized system.

---

## 📌 Project Overview

Managing pediatric patient information manually can be time-consuming and may make it difficult to maintain complete and organized medical histories.

**PediaCare** provides a centralized digital platform where pediatricians and authorized hospital staff can manage patient information and healthcare activities efficiently.

The system is initially focused on **pediatrics**, with the possibility of expanding to other hospital departments in the future.

---

## 🎯 Objectives

* Digitize pediatric patient records.
* Simplify patient registration and appointment management.
* Maintain complete medical histories for children.
* Track vaccination schedules and vaccination history.
* Monitor children's growth and development.
* Manage prescriptions and treatment information.
* Provide role-based access for hospital staff.
* Reduce dependency on paper-based medical records.
* Create a scalable foundation for a complete Hospital Management System.

---

## ✨ Features

### 👶 Patient Management

* Register new pediatric patients.
* Store child and parent/guardian information.
* Maintain contact and emergency details.
* View and update patient profiles.
* Maintain medical history.

### 👨‍⚕️ Pediatrician Management

* Pediatrician login.
* View assigned patients.
* View patient medical history.
* Record consultation details.
* Add diagnosis and treatment information.
* Create prescriptions.
* Schedule follow-up visits.

### 📅 Appointment Management

* Book appointments.
* View upcoming appointments.
* Manage appointment schedules.
* Update appointment status.
* Reschedule or cancel appointments.

### 💉 Vaccination Management

* Maintain vaccination history.
* Record administered vaccines.
* Track upcoming vaccinations.
* Identify pending vaccinations.
* Maintain vaccination dates and notes.

### 📈 Growth Monitoring

The system can maintain important pediatric growth information such as:

* Height
* Weight
* BMI
* Age
* Growth history
* Periodic measurements

This information can be used to monitor changes in a child's growth over multiple visits.

### 💊 Prescription Management

Pediatricians can record:

* Medicine name
* Dosage
* Frequency
* Duration
* Instructions
* Prescription date

### 📊 Reports

The system can provide organized information such as:

* Patient medical history
* Appointment history
* Vaccination history
* Growth records
* Prescription history
* Consultation records

---

## 👥 User Roles

| Role                     | Responsibilities                                                            |
| ------------------------ | --------------------------------------------------------------------------- |
| 👨‍💼 Admin              | Manage doctors, staff, patients and system data                             |
| 👨‍⚕️ Pediatrician       | Manage consultations, medical records, prescriptions and growth information |
| 🧑‍💼 Receptionist       | Register patients and manage appointments                                   |
| 👨‍👩‍👧 Parent/Guardian | View child's appointments, vaccination information and medical records      |

---

## 🏗️ System Architecture

```text
                    ┌───────────────────────┐
                    │   Parent / Guardian   │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │       Frontend        │
                    │   HTML / CSS / JS     │
                    │      Bootstrap        │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │     Flask Backend     │
                    │                       │
                    │ Authentication        │
                    │ Patient Management    │
                    │ Appointments           │
                    │ Medical Records        │
                    │ Vaccinations           │
                    │ Prescriptions          │
                    │ Growth Monitoring     │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │    MySQL Database     │
                    │                       │
                    │ Patients              │
                    │ Doctors               │
                    │ Appointments          │
                    │ Medical Records       │
                    │ Vaccinations          │
                    │ Prescriptions         │
                    │ Growth Records        │
                    └───────────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Flask

### Database

* MySQL

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
PediaCare/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── patients.html
│   ├── patient_details.html
│   ├── appointments.html
│   ├── vaccinations.html
│   ├── prescriptions.html
│   └── growth.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
├── database/
│   └── schema.sql
│
└── docs/
    └── project-report.pdf
```

> The structure may change as development progresses.

---

## 🗄️ Database Design

The planned database contains several interconnected entities.

```text
Users
  │
  ├────────────── Doctors
  │
  └────────────── Patients
                    │
        ┌───────────┼────────────┐
        │           │            │
        ▼           ▼            ▼
   Appointments  Medical      Vaccinations
                 Records
                    │
                    ▼
              Prescriptions

Patients
   │
   ▼
Growth Records
```

### Main Tables

* `users`
* `doctors`
* `patients`
* `guardians`
* `appointments`
* `medical_records`
* `vaccinations`
* `prescriptions`
* `growth_records`

---

## 🔐 Security

The application is intended to implement:

* User authentication
* Role-based authorization
* Password protection
* Session management
* Input validation
* Database access control

> Since this project deals with healthcare information, security and privacy will be important considerations during development.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PediaCare.git
```

### 2. Navigate to the project

```bash
cd PediaCare
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create a MySQL database and import the database schema:

```bash
mysql -u root -p < database/schema.sql
```

Update the database configuration in the application according to your local MySQL setup.

### 7. Run the application

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

---

## 🔄 Application Workflow

```text
Patient Registration
        ↓
Patient Profile Creation
        ↓
Appointment Booking
        ↓
Pediatrician Consultation
        ↓
Medical Record Updated
        ↓
Diagnosis & Prescription
        ↓
Vaccination / Growth Tracking
        ↓
Follow-up Appointment
        ↓
Patient History Maintained
```

---

## 🔮 Future Enhancements

The project can be expanded with:

* 📱 Mobile application
* 🔔 Vaccination reminders
* 📧 Email notifications
* 📲 SMS notifications
* 📊 Interactive pediatric growth charts
* 🧠 AI-assisted clinical decision support
* 🤖 AI-based symptom assistance
* 🩺 Electronic Health Records
* 💳 Billing and payment management
* 🏥 Pharmacy management
* 🧪 Laboratory report management
* 🛏️ Inpatient/ward management
* 📷 QR-based patient identification
* ☁️ Cloud deployment
* 🔐 Advanced security and audit logging
* 👨‍⚕️ Support for additional hospital departments

---

## ⚠️ Disclaimer

PediaCare is an educational/software development project and is **not intended to replace professional medical advice, diagnosis, or treatment**.

Any medical information entered into a development or demonstration environment should be treated as test data and should not contain real patient information unless appropriate privacy and security measures are implemented.

---

## 📌 Project Status

🚧 **Currently in Development**

The initial version focuses on pediatric patient management, appointments, medical records, vaccinations, prescriptions, and growth monitoring.

More hospital management features will be added as development progresses.

---

## 👨‍💻 Contributors

* **Abdullah E** – Developer

Additional contributors can be added as the project develops.

---

## 📄 License

This project is intended for **educational and academic purposes**.

A formal open-source license can be added when the project is ready for public distribution.

---

⭐ If you find this project useful, consider giving the repository a star!
