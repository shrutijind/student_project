# student_project
# EduLeave — Student Leave & Attendance Management System

🚀 **Live Demo:** [https://eduleave-508b4c29de03.herokuapp.com/](https://eduleave-508b4c29de03.herokuapp.com/)
deve

![Responsiveness Screenshots](docs/desktop.png)





## Introduction

**EduLeave** is a Django web application developed by **[Shruti Jindal]** designed to streamline the request, approval, and management process of leave for staff and educators within educational institutions. An employee can submit leave requests, select dates, view dynamic leave duration calculations, and track the status of their submissions. Managers or administrators can review incoming requests, approve or reject them, and maintain full oversight of team availability. It replaces disorganized email chains and paper forms with a centralized, accountable, full CRUD system.

I chose this project idea because tracking leave manually often leads to miscommunications, delayed approvals, and confusion over leave balances. Rebuilding this process as an account-based Django application provides a practical solution to an everyday administrative challenge, while offering a natural, real-world context to implement full CRUD operations, role-based access control, and a robust permissions model.

This is a Full-Stack Capstone Project for the Code Institute AI Augmented Full-Stack Bootcamp.

---

## UX — The 5 Planes

### 1. Strategy

* **Purpose:** Provide educational staff and administrators with a centralized, transparent platform to request and manage leave, eliminating ad-hoc paper forms or disjointed email threads.
* **Primary User Needs:**
  * **Employees/Teachers:** Need a simple, low-friction way to request leave, calculate durations automatically, view real-time request statuses, and cancel pending requests if plans change.
  * **Managers/Administrators:** Need a clear dashboard to review pending leave requests, check coverage, approve or reject submissions, and manage staff leave records.
  * **Both:** Require confidence that only authorized users can view, manage, or approve specific leave requests.
* **Project Goals:**
  * Build a functional, real-world administrative tool addressing an actual organizational workflow.
  * Demonstrate full CRUD capabilities, custom role-based permissions (Employee vs. Manager/Admin), and dynamic form validation.
  * Deliver an accessible, fully responsive web application suitable for desktop and mobile devices.

---

### 2. Scope

* **Features:**
  * **Leave Request Management:** Create, view, update, and cancel leave requests (with dates, leave types, and optional notes).
  * **Dynamic Calculations:** Instant JavaScript calculation of leave duration upon selecting start and end dates.
  * **Role-Aware Navigation:** Context-sensitive navigation bars tailored for Guests, Employees, and Managers.
  * **Feedback & Notifications:** On-page flash messages and auto-dismissing Bootstrap alert notifications for user actions.
  * **Custom Error Handling:** Customized 403, 404, and 500 error pages styled consistently with the application's theme.

---

### 3. Structure

* **Information Architecture:**
  * **Navigation:** `Home` is visible to all visitors. Unauthenticated users see options to `Log In` or `Sign Up`. Authenticated users see their name, assigned role, a link to their `Dashboard` or `Leave Requests`, and a `Log Out` button. Staff members are provided with additional `Admin` links.
  * **Dashboard / Requests Page:** Displays an overview of active and past leave requests categorized by status (*Pending*, *Approved*, *Rejected*).
  * **Leave Request Form:** A clean interface allowing users to pick start/end dates, choose a leave type, and view calculated leave durations before submitting.
* **User Flow:**
  * **Guest:** Browses the homepage landing view → Registers or logs in to access the system.
  * **Employee:** Accesses personal dashboard → Submits new leave request with dynamic date validation → Tracks request status → Cancels pending requests if needed.
  * **Manager/Admin:** Reviews pending staff requests on an administrative dashboard → Approves or rejects submissions with feedback notes → Views site-wide leave schedules.

---
## Design & Planning

### User Stories

#### Student Management
* As a **Teacher / Admin**, I can **add a new student profile** so that I can keep track of enrolled students in the institution.
* As a **Teacher / Admin**, I can **view all students listed alphabetically** so that I can quickly search and manage individual profiles.
* As a **Teacher / Admin**, I can **toggle student attendance status (Present / Absent)** so that real-time attendance records stay up to date.
* As a **Teacher / Admin**, I can **delete a student profile** so that obsolete records and associated user login accounts are cleaned up automatically.

#### Leave Management
* As a **Student**, I can **submit a leave request** with start dates, end dates, and reasons so that my absence can be reviewed.
* As a **Teacher / Admin**, I can **approve or reject student leave requests** so that student status records remain accurate.

#### Authentication
* As a **User**, I can **register and log into my account** so that I can access features reserved for authenticated users.

---

### Wireframes

* **Dashboard View Wireframe:**  
  ![Dashboard Wireframe](docs/deskwire.png)

* **Mobile Responsive View Wireframe:**  
  ![Mobile Wireframe](docs/tabmob.png)

---

### Agile Methodology

This project was built using an **Agile methodology** tracked via GitHub Projects and a Kanban board.

* **Iterations:** Divided into 1-week Sprints focusing on Setup, Authentication, Core CRUD, and Refinement/Styling.
* **User Stories & Tasks:** Broken down into granular sub-tasks tagged with labels (`must-have`, `should-have`, `could-have`, `bug`)
* **Acceptance Criteria:** Every user story included clear Given/When/Then acceptance conditions before being marked as done.

![Kanban Board Screenshot](docs/userstory.png)

---

### Typography

* **Primary Font:** Inter / Roboto (Sans-serif) — chosen for clear readability across dense tables and data-driven dashboards.
* **Secondary Font:** System UI / BlinkMacSystemFont — used for secondary UI elements, badges, and status labels.

---

### Colour Scheme

The application uses an intuitive, modern color scheme designed for administrative clarity:

## 🎨 Color Scheme

| Color | Hex | Usage |
|---|---|---|
| **Primary Blue** | `#0d6efd` | Navigation and primary actions |
| **Dark Charcoal** | `#212529` | Headings and text |
| **Light Neutral** | `#f8f9fa` | Section backgrounds |
| **White** | `#ffffff` | Cards and content |

![EduLeave Color Scheme](docs/colorscheme.png)!


### DataBase Diagram

The application uses PostgreSQL in production and SQLite in development.
 ![EduLeave ](docs/diag.png)!




## Features

### Navigation
* **Navbar:** Clean navigation bar displaying the app brand, quick links to Directory, Leave Requests, and conditional Auth controls (Login/Logout/Register).

### Footer
* **Footer:** Displays copyright details, system status, and links to institutional resources.

### Home-page
* **Student Directory & Attendance Dashboard:** Displays a clean table listing students alphabetically using case-insensitive sorting (`Lower('name')`).
* **Status Badges:** Visual indicators showing present/absent states.

### CRUD Functionality
* **Create:** Teachers can add new students; students can submit leave requests.
* **Read:** View student directory and leave request statuses in structured tables.
* **Update:** Toggle attendance status with immediate database updates.
* **Delete:** Deleting a student executes a custom `delete()` model method that automatically cascades and removes their associated `User` account.

### Authentication & Authorisation
* Built with Django's default authentication system for secure sign-in, sign-out, session handling, and route protection via decorators/mixins.

---

## Technologies Used

* **HTML5 / CSS3 / JavaScript:** Frontend structure, responsive layout, and interactive components.
* **Python 3.12+:** Core business logic.
* **Django 5.x:** Web framework handling routing, ORM, security, and views.
* **Bootstrap 5:** Styling framework for responsive grids, tables, and buttons.
* **PostgreSQL (via ElephantSQL / CI Database):** Production relational database.
* **Gunicorn:** WSGI HTTP Server for UNIX deployment.
* **Git & GitHub:** Version control and source code management.
* **Heroku:** Cloud platform for deployment.

---

## Testing

### Google's Lighthouse Performance

![Lighthouse Desktop Screenshot](docs/deskperformance.png)
![Lighthouse Mobile Screenshot](docs/mobileperformance.png)

| Platform | Performance | Accessibility | Best Practices | SEO |
| :--- | :--- | :--- | :--- | :--- |
| **Desktop** | 95+ | 96 | 100 | 91 |
| **Mobile** | 83 | 89 | 100 | 91 |

---

### Browser Compatibility

The application was tested across multiple modern browsers to verify UI consistency and full functional stability:
* **Google Chrome:** Fully functional.
* **Mozilla Firefox:** Fully functional.
* **Apple Safari:** Fully functional.
* **Microsoft Edge:** Fully functional.

---

### Responsiveness

Tested across multiple viewport sizes using Chrome DevTools:
* **Mobile Small :** Table converts to horizontal scrollable grid; action buttons collapse cleanly.
![Responsiveness Screenshots](docs/mobile.png)
* **Tablet :** Full layout rendering without visual truncation.
![Responsiveness Screenshots](docs/tab.png)
* **Desktop :** Full multi-column view with optimal spacing.

![Responsiveness Screenshots](docs/desktop.png)

---

### Code Validation

* **W3C HTML Validator:** Validated all templates without critical errors.
![Validation Screenshots](docs/htmlval.png)

* **W3C CSS Validator (Jigsaw):** Passed without errors.
![Validation Screenshots](docs/css.png)

* **JavaScript Validator (ESLint / JSHint):** Passed without warnings.
![Validation Screenshots](docs/jssj.png)

* **Python Validation (PEP 8 / Flake8):** All models, views, and custom methods adhere strictly to PEP 8 standards.

![Validation Screenshots(admin.py)](docs/adminpy.png)

![Validation Screenshots(forms.py)](docs/formspy.png)

![Validation Screenshots(apps.py)](docs/appspy.png)

![Validation Screenshots(views.py)](docs/pep8val.png)

![Validation Screenshots(test.py)](docs/test.png)

![Validation Screenshots(url.py)](docs/url.png)

![Validation Screenshots(model.py)](docs/modelpy.png)

---

### Manual Testing User Stories

| User Story | Test | Pass | Result Visible / Action | Screenshot |
| :--- | :--- | :---: | :--- | :--- |
| **Add Student** | Submit student form | ✓ | New student named manohar appears sorted alphabetically in list | ![Test Screenshot](docs/after.png) |
| **Toggle Status** | Click Attendance button | ✓ | Status badge toggles between Present & Absent |![Test Screenshot](docs/toggle.png) |
| **Delete Student** | Click Delete button | ✓ | Student and linked User account removed | ![Test Screenshot](docs/delete.png) |

---
### Manual Testing Features

| **User Authentication** | Submit Login Form | ✓ | Submitting valid credentials redirects user to Dashboard with a success toast message | ![Feature Test](docs/auth.png) |

| **Duration Calculation** | Change Date Inputs | ✓ | Selecting valid start/end dates dynamically calculates total days without page refresh | ![Feature Test](docs/nodays.png) |

### Bugs

| Bug Description | Resolution | Status |
| :--- | :--- | :---: |
| Deleting a Student left an orphaned User record in `auth_user`. | Overrode `delete()` method on `Student` model to clean up `self.user` before deletion. | **Fixed** |
| Capitalized names ('Apen') appeared before lowercase names ('gulshan') in ordering. | Updated `ordering` in `class Meta` to use `django.db.models.functions.Lower('name')`. | **Fixed** |

---
## Deployment

This website was deployed to **Heroku** from a **GitHub** repository. The following steps were taken to complete the deployment:

### Creating the GitHub Repository
1. Logged into my GitHub account and navigated to the project template repository.
2. Clicked on **Use this template** and selected **Create a new repository** from the drop-down menu.
3. Entered a unique repository name, set the repository visibility to Public, and clicked **Create repository**.
4. Cloned the repository to my local development environment in VS Code to build and format the project assets.

---

### Provisioning the Database
1.Created a PostgreSQL database using the **Code Institute PostgreSQL Database Maker**.
2.Entered my email address to receive my database credentials.
3.Copied the generated `DATABASE_URL` string sent to my email.
4. I added the database URL to my local `env.py` environment variables file to connect the local Django development environment to the live database:
   ```python
   os.environ["DATABASE_URL"]

   ### Heroku Deployment

This application was deployed to **Heroku** directly from the repository's `main` branch using the following steps:

1. **App and Database Creation:**
   * Created a new application on the Heroku Dashboard.
   * Provisioned a PostgreSQL database using the **Heroku Postgres** add-on (`heroku-postgresql`) via the **Resources** tab (or CLI).

2. **Configuration Variables (Config Vars):**
   * Navigated to **Settings → Config Vars** on the Heroku Dashboard and configured the environment variables:
     * `SECRET_KEY`: A unique, secure Django secret key for production (distinct from the local development key).
     * `DATABASE_URL`: Automatically attached and populated upon provisioning the Postgres add-on.

3. **Code Deployment:**
   * Pushed the codebase to Heroku:
     ```bash
     git push heroku main
     ```
   * This triggered the build process, automatically ran `collectstatic`, and executed database migrations via the project's `Procfile` before launching the application:
     ```text
     release: python manage.py migrate --noinput
     web: gunicorn config.wsgi
     ```

> **Important Deployment Note:** Pushing code to GitHub (`git push`) does not automatically deploy changes to Heroku. Running `git push heroku main` is a required separate step whenever the repository is updated and changes need to be reflected on the live site.
> 
> Static files (CSS/JS) are served in production using **WhiteNoise**, configured in `config/settings.py`.
     ```

> **Note on Deployment Workflow:** Pushing code to GitHub (`git push origin main`) does not automatically deploy to Heroku. Running `git push heroku main` is a distinct step required whenever updates need to be reflected on the live site. Static assets (CSS/JS) are served in production using **WhiteNoise**, configured directly inside `config/settings.py`.


---

## AI Usage

Generative AI (Gemini) was utilized as an adaptive development assistant throughout this project:
* **Refactoring Models:** Assisted in implementing the custom `.delete()` cascade override on the `Student` model to automatically clean up `User` objects.
* **Query Optimization:** Implemented case-insensitive database sorting via `django.db.models.functions.Lower` inside `class Meta`.
* **Documentation:** Helped structure manual testing tables, bug logs, and README templates.
AI (**Gemini** and **ChatGPT**) was used throughout this project for planning, debugging, and pair-programming, guided by my project brief and the Code Institute assessment criteria:

* **Planning:** Assisting with initial project scoping, data modeling, and README structure.
* **Debugging:** Identifying and resolving code issues, including PEP 8 styling, terminal environment setup, Django messaging regressions, and Heroku deployment errors.
* **Feature Development:** Assisting with CRUD view permission checks, form date validations, custom JavaScript helpers (date calculations and auto-dismissing alerts), responsive styling, custom error pages (403/404/500), and automated unit tests.
* **Documentation:** Helping document test cases, project reflections, and GitHub issue tracking.


---

## Credits

* **Code Institute:** Project template, deployment guidance, and database maker service.
* **Django Documentation:** Official documentation for custom model methods and field options.

## Acknowledgements

I would like to express my sincere gratitude to the following people who supported me throughout the development of this project:

* **Code Institute Tutor Support, Tim, and Marko:** For their invaluable guidance, technical insights, and continuous support throughout the project.
* **My Amazing Partner:** For endless inspiration, motivation, and encouragement to help me fulfill my full potential.