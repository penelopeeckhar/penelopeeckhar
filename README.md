<div align="center">

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-static.svg">
  <img src="assets/hero.svg" width="100%" alt="Abir Majdi — Cloud Security · DevSecOps · Detection Engineering">
</picture>

<br>

[![Portfolio](https://img.shields.io/badge/Portfolio-penelopeeckhar.github.io-701A3D?style=flat-square&logo=githubpages&logoColor=F8F0F3)](https://penelopeeckhar.github.io/portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abir%20Majdi-451126?style=flat-square&logo=linkedin&logoColor=F8F0F3)](https://www.linkedin.com/in/abir-majdi-a221bb296/)
[![Email](https://img.shields.io/badge/Email-abir.majdi%40usmba.ac.ma-701A3D?style=flat-square&logo=gmail&logoColor=F8F0F3)](mailto:abir.majdi@usmba.ac.ma)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-penny1598-451126?style=flat-square&logo=tryhackme&logoColor=F8F0F3)](https://tryhackme.com/p/penny1598)

</div>

## `$ whoami`

I'm a 5th-year engineering student in **Digital Development & Cybersecurity (GDNC)** at **ENSA Fès** (USMBA). I work on **cloud security and DevSecOps**: CI/CD pipelines with security gates, container and Kubernetes hardening, GitOps delivery, observability, and the detection and response layer on top.

I build full platforms end to end, measure what they actually enforce or catch, and document the gaps.

<div align="center">

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/impact-mobile-static.svg">
  <source media="(max-width: 600px)" srcset="assets/impact-mobile.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/impact-static.svg">
  <img src="assets/impact.svg" width="100%" alt="Key results: 16/16 Prometheus targets up · 350→51 image CVEs · 85.7% ATT&CK detection · 0 false positives · 6 custom NSE audits">
</picture>

<sub>Every figure above comes from the linked repository's own report or scan output.</sub>

</div>

---

## ◆ Featured work

<table>
<tr>
<td width="50%" valign="top">

### ☁️ [AegisCloud](https://github.com/penelopeeckhar/AegisCloud)
**Cloud-native DevSecOps & GitOps platform** running the full delivery chain on k3s, end to end, without paid cloud.

- **3 Jenkins pipelines** green (9 stages each), SonarQube quality gate
- **Trivy gate** blocks images with fixable CRITICAL CVEs
- **ArgoCD** auto-sync on k3s: Synced & Healthy, 48 resources
- **Prometheus / Grafana / Alertmanager**: 16/16 targets up
- Ansible playbook `failed=0`, Terraform validated

<sub>`Jenkins` `SonarQube` `Trivy` `ArgoCD` `k3s` `Prometheus`</sub>

</td>
<td width="50%" valign="top">

### 🛡️ [SecureOps Shield](https://github.com/penelopeeckhar/secureops-shield)
**End-to-end DevSecOps & SOC pipeline** around OWASP Juice Shop, in 9 blocks.

- CI with **Semgrep, Bandit, Gitleaks, Trivy** on every push
- Image hardening: **350 → 51** HIGH+CRITICAL CVEs (unhardened → distroless)
- **OWASP ZAP** DAST, **k3s** audited with **kube-bench**
- **Wazuh** FIM alert → webhook → auto-created **TheHive** case, enriched by **Cortex**
- Flask scoring dashboard with live incident timeline and PDF export

<sub>`GitHub Actions` `Docker` `k3s` `Wazuh` `TheHive` `Cortex` `Flask`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚔️ [MITRE ATT&CK Detection Lab](https://github.com/penelopeeckhar/mitre-attack-detection-lab)
**5-VM Active Directory lab** (DC, 2 clients, Kali, Splunk SIEM).

- **21 techniques across 7 tactics** simulated with Atomic Red Team
- Sysmon + Universal Forwarder → **Splunk**, 40k+ events centralised
- **85.7 % detection** (18/21)
- **3 Sigma rules** written for the blind spots: T1134.001, T1048.001, T1041
- ATT&CK Navigator layer and full report included

<sub>`Active Directory` `Sysmon` `Splunk` `Atomic Red Team` `Sigma`</sub>

</td>
<td width="50%" valign="top">

### 📧 [MedSecureGateway](https://github.com/penelopeeckhar/MedSecureGateway)
**Secure email gateway for a healthcare context** — PFA internship, Ministry of Health and Social Protection (Rabat).

- Static pipeline: **YARA**, olevba, pdfid, VirusTotal, ExifTool, custom PE analyser
- **Sandboxing** on isolated Linux (strace, tcpdump) and Windows (Sysmon) VMs
- 0–100 risk engine → SAFE / SUSPICIOUS / MALICIOUS, quarantine
- **0 false positives** on the final calibration set (disarmed samples only)
- RBAC dashboard, 90-day purge, GDPR-minded design

<sub>`Python` `Flask` `PostgreSQL` `YARA` `Sysmon` `VirtualBox`</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔎 [NSE-Sentinel](https://github.com/penelopeeckhar/nse-sentinel)
**Custom Nmap NSE auditing toolkit** (Lua) for authorised assessments.

- **6 audits**: HTTP headers, SSH crypto, FTP, SMB signing / SMBv1, MySQL, info disclosure
- Per-service risk score aggregated into a global score
- Terminal and HTML reports

<sub>`Lua` `Nmap NSE` `Bash`</sub>

</td>
<td width="50%" valign="top">

### 🏥 [Hospital DB Anomaly SIEM](https://github.com/penelopeeckhar/hospital-db-anomaly-detection-siem)
**Lightweight SIEM for medical database access** — internship at CHU Hassan II, Fès.

- MySQL triggers log every access; off-hours, repeated and failed queries flagged
- Daily CSV reports and email alerts
- Flask dashboard with integrated SQLMap testing

<sub>`Python` `Flask` `MySQL` `SQLMap`</sub>

</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br>

| Project | What it is | Stack |
| --- | --- | --- |
| [Misconfig Mayhem](https://github.com/penelopeeckhar/projet-misconfig-mayhem) | Red/Blue cycle on a vulnerable FastAPI app: exploit 3 misconfigurations (cleartext credentials, debug mode, directory listing), fix them, verify. ~85 % overall risk reduction | FastAPI · Nginx · PostgreSQL · MinIO · Nmap · Nikto |
| [SSH Honeypot](https://github.com/penelopeeckhar/projet-honeypot-ssh) | Interactive Paramiko honeypot with brute-force alerts, logs shipped to ELK; container confined with AppArmor, seccomp and dropped capabilities | Python · Docker · ELK |
| [Private Cloud Platform](https://github.com/penelopeeckhar/private-cloud-autoscaling-platform) | Proxmox cluster over ZeroTier with HAProxy load balancing; Prometheus alert → webhook → autoscaling script | Proxmox · ZeroTier · HAProxy · Prometheus |
| [Mini-TLS](https://github.com/penelopeeckhar/projet-crypto-tls) | Teaching implementation of a TLS-style handshake: DH-2048, HKDF-SHA256, AES-256-GCM | Python · cryptography |
| [Kaggriculture Agent](https://github.com/penelopeeckhar/kaggriculture-agent) | Beam-search agent for a Kaggle competition (~3,800 teams); ladder score 292.6 → 342.8 over 6 tested versions | Python · Docker |

</details>

---

## ◆ Skills, with evidence

| Area | Tools | Where I used them |
| --- | --- | --- |
| **DevSecOps** | Jenkins · GitHub Actions · SonarQube · Semgrep · Gitleaks · Trivy · OWASP ZAP | AegisCloud · SecureOps Shield |
| **Cloud & Kubernetes security** | Docker · Kubernetes (k3s) · kube-bench · ArgoCD · Ansible · Terraform · Proxmox | AegisCloud · SecureOps Shield · Private Cloud |
| **Observability** | Prometheus · Grafana · Alertmanager | AegisCloud · Private Cloud |
| **Detection & SIEM** | Splunk · Sysmon · Sigma · ELK · Wazuh | ATT&CK lab · Honeypot · SecureOps Shield |
| **SOAR & incident response** | TheHive · Cortex · webhooks | SecureOps Shield |
| **Malware analysis** | YARA · olevba · pdfid · Ghidra · PEStudio · FakeNet-NG · sandboxing | MedSecureGateway · WannaCry coursework |
| **Offensive testing (labs)** | Nmap / NSE · Burp Suite · Metasploit · SQLMap · Hydra · John / Hashcat | NSE-Sentinel · TechBiz internship labs |
| **Network & crypto** | Wireshark · Ettercap · TLS · Diffie-Hellman · AES-GCM | Mini-TLS · network attack labs |

<div align="center">
<br>

[![Stack](https://skillicons.dev/icons?i=docker,kubernetes,jenkins,githubactions,ansible,terraform,linux&theme=dark)](https://skillicons.dev)
<br>
[![Stack](https://skillicons.dev/icons?i=python,bash,lua,c,java,js,mysql&theme=dark)](https://skillicons.dev)
<br>
[![Stack](https://skillicons.dev/icons?i=prometheus,grafana,elasticsearch,nginx,flask,fastapi,postgres,kali&theme=dark)](https://skillicons.dev)

</div>

---

## ◆ Experience

| When | Role | Highlights |
| --- | --- | --- |
| **Aug – Sep 2026** | Ethical Hacking Intern · **TechBiz Security Academy** (remote) | 6 weeks, 18 graded lab tasks: OSINT, enumeration, OWASP Top 10, Burp, Metasploit, capstone pentest with report. Certificate *with distinction* |
| **Aug – Sep 2026** | Cybersecurity Intern · **InternNova** (remote) | 6-week remote program with weekly graded lab tasks and reports |
| **Summer 2026** | Security Engineering Intern (PFA) · **Ministry of Health and Social Protection**, Rabat | Designed and built MedSecureGateway, from architecture to calibration |
| **Jul 2025** | Observation Intern · **CHU Hassan II**, Fès | Built an anomaly-detection SIEM for hospital database access |

---

## ◆ Certifications

[![TechBiz](https://img.shields.io/badge/TechBiz%20Security%20Academy-Ethical%20Hacking%20%C2%B7%20with%20distinction-701A3D?style=flat-square)](https://penelopeeckhar.github.io/portfolio/)
[![InternNova](https://img.shields.io/badge/InternNova-Cyber%20Security%20Internship-451126?style=flat-square)](https://penelopeeckhar.github.io/portfolio/)
[![Forage](https://img.shields.io/badge/Mastercard%20%C3%97%20Forage-Cybersecurity%20Job%20Simulation-701A3D?style=flat-square)](https://penelopeeckhar.github.io/portfolio/)
<br>
[![Oracle](https://img.shields.io/badge/Oracle-Database%20Programming%20with%20SQL-451126?style=flat-square&logo=oracle&logoColor=F8F0F3)](https://penelopeeckhar.github.io/portfolio/)
[![Udemy](https://img.shields.io/badge/Udemy-SQLMap%20for%20Ethical%20Hacking-701A3D?style=flat-square&logo=udemy&logoColor=F8F0F3)](https://penelopeeckhar.github.io/portfolio/)
[![Udemy](https://img.shields.io/badge/Udemy-MiTM%20Attacks%20%26%20RAT%20Dev-451126?style=flat-square&logo=udemy&logoColor=F8F0F3)](https://penelopeeckhar.github.io/portfolio/)
[![Great Learning](https://img.shields.io/badge/Great%20Learning-Introduction%20to%20Cryptography-701A3D?style=flat-square)](https://penelopeeckhar.github.io/portfolio/)

**Hands-on platforms:** [TryHackMe](https://tryhackme.com/p/penny1598) · [HackerDNA](https://hackerdna.com/users/arael) · Hack The Box

---

## ◆ Contribution activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/penelopeeckhar/penelopeeckhar/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/penelopeeckhar/penelopeeckhar/output/github-snake.svg">
  <img alt="Contribution graph animated as a snake" src="https://raw.githubusercontent.com/penelopeeckhar/penelopeeckhar/output/github-snake.svg" width="100%">
</picture>

<sub>Generated daily from my GitHub contribution graph by the <code>Generate Snake</code> workflow.</sub>

</div>

---

<div align="center">

**Cloud Security · DevSecOps · Detection Engineering**

[Portfolio](https://penelopeeckhar.github.io/portfolio/) · [LinkedIn](https://www.linkedin.com/in/abir-majdi-a221bb296/) · [abir.majdi@usmba.ac.ma](mailto:abir.majdi@usmba.ac.ma)

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/footer-static.svg">
  <img src="assets/footer.svg" width="100%" alt="Build · Secure · Observe">
</picture>

</div>
