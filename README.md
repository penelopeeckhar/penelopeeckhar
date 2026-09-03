<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=Abir%20Majdi&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&descAlignY=60&desc=Security%20Engineer%20%7C%20Digital%20Development%20Engineering&descAlign=50)

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=22&duration=3500&pause=800&color=A78BFA&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=100&lines=Cybersecurity+%26+Digital+Engineering+Student%3BPenetration+Testing+%7C+SIEM+%7C+Malware+Analysis%3BBuilding+Secure+Systems+%7C+Seeking+PFE+in+France)](https://git.io/typing-svg)

![ENSA Fès](https://img.shields.io/badge/ENSA%20F%C3%A8s-5th%20Year%20Engineer-7C3AED?style=for-the-badge&logo=graduation-cap&logoColor=white)
![Program](https://img.shields.io/badge/GDNC-Digital%20Dev%20%26%20Cybersecurity-6D28D9?style=for-the-badge&logo=shield&logoColor=white)
![Location](https://img.shields.io/badge/%F0%9F%93%8D%20Morocco%2C%20Target%3A%20France-4C1D95?style=for-the-badge)

[![Portfolio](https://img.shields.io/badge/Portfolio-penelopeeckhar.github.io-8B5CF6?style=for-the-badge&logo=firefox&logoColor=white)](https://penelopeeckhar.github.io/portfolio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abir%20Majdi-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abir-majdi-a221bb296/)
[![Email](https://img.shields.io/badge/Email-abir.majdi%40usmba.ac.ma-6D28D9?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/?view=cm&to=abir.majdi@usmba.ac.ma)
[![GitHub](https://img.shields.io/badge/GitHub-penelopeeckhar-4C1D95?style=for-the-badge&logo=github&logoColor=white)](https://github.com/penelopeeckhar)

[![Profile Views](https://komarev.com/ghpvc/?username=penelopeeckhar&style=for-the-badge&color=7C3AED&label=PROFILE+VIEWS)](https://github.com/penelopeeckhar)
[![Followers](https://img.shields.io/github/followers/penelopeeckhar?style=for-the-badge&color=6D28D9&label=FOLLOWERS&logo=github)](https://github.com/penelopeeckhar?tab=followers)
[![Stars](https://img.shields.io/github/stars/penelopeeckhar?style=for-the-badge&color=4C1D95&label=STARS&logo=github)](https://github.com/penelopeeckhar?tab=repositories)

</div>

---

## `whoami`

```yaml
name: Abir Majdi
role: Security Engineer — Digital Development & Cybersecurity
institution: ENSA Fès (École Nationale des Sciences Appliquées)
program: GDNC — Génie du Développement Numérique & Cybersécurité
year: 5th year (2022–2027) — annual average 2025-2026: 14.62/20
location: Fès, Morocco → Target: France
availability: PFE (6-month internship) — available from February 2027

profile: |
  Security-focused engineering student with hands-on, end-to-end experience across
  the full attack/defense spectrum: penetration testing, MITRE ATT&CK simulation,
  malware analysis (static + dynamic), DevSecOps (SAST/DAST/SCA), SOC/SIEM/SOAR
  tooling, and secure application development. Methodical, autonomous, and
  production-minded — I document everything and finish what I build, with full
  source code and demos published on GitHub and my portfolio.

open_to:
  - PFE — 6-month cybersecurity internship in France (visa process ready to start)
  - Threat detection, SOC/SIEM engineering & DevSecOps roles
  - AppSec / penetration testing assignments
  - Post-graduation employment in France
```

---

## ⚡ Tech Stack

### Languages & Core

[![Skills](https://skillicons.dev/icons?i=python,bash,c,cpp,java,js,sql&theme=dark)](https://skillicons.dev)

### Backend, APIs & Databases

[![Skills](https://skillicons.dev/icons?i=flask,fastapi,postgres,mysql,oracle&theme=dark)](https://skillicons.dev)

### Security, DevOps & Infrastructure

[![Skills](https://skillicons.dev/icons?i=docker,kubernetes,linux,git,github,githubactions,nginx,elasticsearch&theme=dark)](https://skillicons.dev)

---

## 🔐 Cybersecurity Expertise

| Domain                        | Proficiency              | Details                                                                 |
| ------------------------------ | ------------------------- | ------------------------------------------------------------------------ |
| **DevSecOps (SAST/DAST/SCA)** | ████████░░ Advanced      | Semgrep, Bandit, Gitleaks, Trivy, OWASP ZAP, GitHub Actions CI/CD       |
| **SOC / SIEM / SOAR**          | ████████░░ Advanced      | Splunk, Elasticsearch, Wazuh (EDR/SIEM), TheHive/Cortex, Sigma rules    |
| **Malware Analysis**           | ████████░░ Advanced      | YARA, oletools/olevba, ExifTool, VirusTotal API, sandboxing             |
| **MITRE ATT&CK & Pentest**     | ████████░░ Advanced      | Atomic Red Team, impacket, Meterpreter, Metasploit, Nmap, Nikto, SQLMap |
| **Container / Cluster Security** | ███████░░░ Proficient   | Docker hardening (distroless), Kubernetes (k3s), kube-bench (CIS)       |
| **Email Security**             | ████████░░ Advanced      | Anti-phishing pipeline, sandboxed detonation, risk scoring              |
| **Network Security**           | ███████░░░ Proficient    | TCP/IP, TLS/SSL, Diffie-Hellman, MiTM, Wireshark                        |
| **Cryptography**               | ██████░░░░ Intermediate  | TLS/SSL, symmetric/asymmetric, PKI, Diffie-Hellman                      |

---

## 💼 Professional Experience

### 🛡️ MedSecure Gateway — Stage PFA, Ministère de la Santé (Rabat)
**Jul – Aug 2026**

Designed and autonomously developed a **Secure Email Gateway** on a 3-VM architecture: a Flask/PostgreSQL/SQLAlchemy backend with a real-time dashboard, and two sandbox VMs isolated from the network (Host-Only, no internet access).

- Built a static analysis pipeline (**YARA**, macro analysis with **oletools/olevba**, metadata via **ExifTool**) and checked file reputation against **VirusTotal** (70+ engines), backed by monitored dynamic sandbox execution (**inotify-tools**) feeding an automated risk-scoring engine
- Calibrated YARA detection on 20 clean/malicious samples (MalwareBazaar, EICAR) and validated the pipeline with a simulated phishing attack (SMTP injection via **swaks**) → **100% detection, 0% false positives** across 6 YARA rules

`Python` `Flask` `SQLAlchemy` `PostgreSQL` `YARA` `oletools` `VirusTotal API` `MailHog` `ExifTool` `Paramiko` `Kali Linux`

---

### 🏥 hospital-db-anomaly-detection-siem — Stage d'initiation, CHU Hassan II (Fès)
**Jul 2025**

Developed a lightweight SIEM (Python/Flask/MySQL) to monitor a hospital database, integrating 4 behavioral detection rules: off-hours access, mass data extraction (≥10 req/10min), brute force (5 attempts/5min), and SQL injection (5 req/5min).

- Implemented MySQL triggers for automated logging, a Flask dashboard with severity levels, an integrated SQLMap scanning module, and automated email alerts with daily CSV reports

`Python` `Flask` `MySQL` `pandas` `SQLMap` `Bootstrap`

---

## 🚀 Top 3 Personal Projects — Finalized (full source & demos on GitHub/portfolio)

### ⚙️ SecureOps Shield — End-to-end DevSecOps/SOC pipeline
[Repository →](https://github.com/penelopeeckhar/SecureOps-Shield)

A complete 9-block application security chain on a Debian/Docker VM targeting OWASP Juice Shop.

| Attribute      | Details                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------- |
| **CI/CD**      | GitHub Actions pipeline running SAST (Semgrep, Bandit), secret detection (Gitleaks), SCA/image scanning (Trivy) on every push |
| **Hardening**  | Progressive Docker image hardening (unhardened → slim hardened → distroless) — Trivy findings cut from **350 to 51 CVEs (-85%)** |
| **Cluster**    | Kubernetes cluster (k3s) audited with kube-bench (CIS Benchmark); DAST coverage via OWASP ZAP     |
| **SOC/SOAR**   | Wazuh as EDR/SIEM for real-time detection, connected to TheHive/Cortex for automated incident triage & enrichment |
| **Dashboard**  | Centralized Flask/PostgreSQL security scoring dashboard aggregating results from all 9 blocks     |

`GitHub Actions` `Semgrep` `Bandit` `Gitleaks` `Trivy` `Docker` `Kubernetes (k3s)` `kube-bench` `OWASP ZAP` `Wazuh` `TheHive` `Cortex` `Flask` `PostgreSQL`

---

### ⚔️ MITRE ATT&CK Simulation & SIEM Detection — 5-VM Active Directory Lab
[Repository →](https://github.com/penelopeeckhar/mitre-attack-detection-lab)

A full Active Directory lab (Windows Server 2022 DC, 2× Windows 10 clients, Kali Linux attacker, Ubuntu SIEM running Splunk/Elasticsearch in Docker) used to simulate realistic end-to-end attack chains.

| Attribute          | Details                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------- |
| **Scope**          | 21 MITRE ATT&CK techniques: initial access (phishing), privilege escalation (T1134), lateral movement (Pass-the-Hash, impacket PsExec), exfiltration (T1041) |
| **Tooling**        | Atomic Red Team, impacket, Meterpreter                                                    |
| **Detection Rate** | **85.7% (18/21 techniques detected)**                                                      |
| **Output**         | 3 custom Sigma rules authored to close detection blind spots (T1041, T1134.001, T1048.001) |

`Splunk` `Elasticsearch` `Docker` `Atomic Red Team` `Sigma` `impacket` `Meterpreter`

---

### 🌾 Kaggriculture — AI Agent for Kaggle Competition (~3,800 teams)
[Repository →](https://github.com/penelopeeckhar/kaggriculture)

An AI agent (beam search + calibrated heuristic) for the Kaggriculture Kaggle competition, including a self-sufficient local simulator (**"ShadowEnv"**) that reconstructs game state from raw observations, since no compatible `env.clone()` was available.

| Attribute        | Details                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| **Bug fix**       | Diagnosed and fixed a critical threading incompatibility (`signal.SIGALRM`) blocking execution on the official ladder |
| **Reliability**  | Validated over 719 turns with no crash or memory leak — median decision time of **241.5 ms** for a 450 ms budget |
| **Performance**  | Calibrated heuristic weights & a zone-aware labor strategy over 6 agent iterations, beating the reference (starter) agent by **+74 treasury points** in isolated testing |

`Python` `PyTorch` `Docker` `Heuristic / Beam Search`

---

## 🏆 Achievements

| Recognition                       | Details                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------- |
| 🎯 **ATT&CK Detection Rate**        | 85.7% detection (18/21 techniques) in the full AD simulation lab                |
| 📧 **Email Threat Pipeline**        | 100% detection, 0% false positives across 6 YARA rules (MedSecure Gateway)      |
| 📉 **Container Hardening**          | Trivy findings reduced from 350 to 51 CVEs (-85%) on SecureOps Shield          |
| 🤖 **Kaggle Competition**           | AI agent beat the reference agent by +74 treasury points (~3,800 teams)        |
| 🧩 **Sigma Rules Authored**         | 3 custom detection rules for ATT&CK blind spots (T1041, T1134.001, T1048.001)  |
| 🎓 **Academic Standing**            | 5th-year engineering student at ENSA Fès — annual average 14.62/20             |
| 🌍 **International Target**         | Active PFE candidate for France, available from February 2027                  |

---

## 📜 Certifications

[![Cryptography](https://img.shields.io/badge/Introduction%20to%20Cryptography-Great%20Learning-4C1D95?style=for-the-badge)](https://www.mygreatlearning.com/)
[![SQLMap](https://img.shields.io/badge/SQLMap%20for%20Ethical%20Hacking-Udemy-6D28D9?style=for-the-badge&logo=udemy&logoColor=white)](https://www.udemy.com/)
[![MiTM/RAT](https://img.shields.io/badge/MiTM%20Attacks%20%26%20RAT%20Development-PYCEH%20Udemy-7C3AED?style=for-the-badge&logo=udemy&logoColor=white)](https://www.udemy.com/)
[![Oracle SQL](https://img.shields.io/badge/Database%20Programming%20with%20SQL-Oracle-8B5CF6?style=for-the-badge&logo=oracle&logoColor=white)](https://education.oracle.com/)

---

## 🧩 CTF & Labs

[![TryHackMe](https://img.shields.io/badge/TryHackMe-Active-7C3AED?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/penny1598)
[![HackTheBox](https://img.shields.io/badge/Hack%20The%20Box-Active-6D28D9?style=for-the-badge&logo=hackthebox&logoColor=white)](https://profile.hackthebox.com/profile/019ccd0b-20b9-7309-a4ee-d62a0e6252c8)

**Completed challenges:** n8n exploit · DFIR (Splunk) · DVWA · Metasploitable 2 · Active Directory attack simulations

---

## 📊 GitHub Analytics

<div align="center">

![Metrics](https://raw.githubusercontent.com/penelopeeckhar/penelopeeckhar/main/metrics.svg)

</div>

> ℹ️ This card is generated by the **[lowlighter/metrics](https://github.com/lowlighter/metrics)** GitHub Action (see `metrics.yml` below), refreshed automatically every 6 hours and committed straight to this repository. It replaces the old `github-readme-stats.vercel.app` cards, whose public instance has been intermittently returning `503 DEPLOYMENT_PAUSED` since early 2026 — hosting the graph in this repo removes that dependency entirely.

---

## 📈 Contribution Streak

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com/?user=penelopeeckhar&theme=dark&hide_border=true&background=0D1117&stroke=7C3AED&ring=A78BFA&fire=C4B5FD&currStreakLabel=A78BFA&sideNums=C4B5FD&dates=6D28D9)](https://github.com/DenverCoder1/github-readme-streak-stats)

</div>

---

## 🐍 Contribution Snake

<div align="center">

![github-snake](https://raw.githubusercontent.com/penelopeeckhar/penelopeeckhar/output/github-contribution-grid-snake.svg)

</div>

> ℹ️ Requires the `snake.yml` workflow below (using [Platane/snk](https://github.com/Platane/snk)) to be present and to have run at least once — it generates the SVG on an `output` branch.

---

## 🎯 Current Focus

```yaml
learning:
  - Advanced threat hunting and APT techniques
  - Cloud security (AWS, Azure security posture)
  - Reverse engineering (deeper binary analysis)
  - Kubernetes security and container hardening

finalized_and_published:
  - MedSecure Gateway (Ministry of Health PFA)
  - SecureOps Shield (DevSecOps/SOC pipeline)
  - MITRE ATT&CK Simulation & SIEM Detection Lab
  - Kaggriculture (Kaggle AI agent)

exploring:
  - CTF competitions (DFIR, web exploitation, AD attacks)
  - Purple team methodologies
  - AI/ML applied to threat detection

open_to:
  - PFE internship — 6 months — Cybersecurity — France (from February 2027)
  - Work visa sponsorship welcomed
```

---

## 🤝 Connect

[![Gmail](https://img.shields.io/badge/Gmail-abir.majdi%40usmba.ac.ma-7C3AED?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/?view=cm&to=abir.majdi@usmba.ac.ma)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-6D28D9?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abir-majdi-a221bb296/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-4C1D95?style=for-the-badge&logo=github&logoColor=white)](https://github.com/penelopeeckhar)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-8B5CF6?style=for-the-badge&logo=firefox&logoColor=white)](https://penelopeeckhar.github.io/portfolio)

---

<div align="center">

*"Security is not a product, but a process — and I intend to master every step of it."*

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer)

</div>