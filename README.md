# LearnTrack – Big Data Analytics Platform

## 📌 Project Overview

**LearnTrack** is a backend analytics platform designed to process and analyze online course activity data.  
This project was developed as part of the **Big Data (M2 ILSI – TLSI Department)** coursework at **University of Constantine 2 – Abdelhamid Mehri (2025–2026)**.

The goal is to design a **scalable, highly available, and performant data architecture** capable of handling real-time and batch analytics for online learning systems.

---

## 🎯 Project Objectives

The platform must support the following core requirements:

- Ingest and store **student activity logs** (page views, quiz attempts, etc.)
- Compute **real-time engagement scores** per student
- Enable **flexible queries** on student profiles and activity history
- Perform **batch analytics** for course-level engagement reports
- Detect **suspicious behaviors** such as multi-region access
- Provide **visual dashboards** for analytics results

---

## 📊 Mandatory Query & Data Patterns

The system is designed to efficiently support these operations:

1. Insert activity logs for multiple students  
2. Retrieve the **latest 20 activities** of a given student  
3. Update student profile information (progress, contact details)  
4. Detect students accessing content from **multiple regions within a short time window**  
5. Generate **daily course engagement analytics**  
6. Maintain and update **engagement scores per student**

---

## 🧱 Technical Requirements

- Flexible data modeling for activity documents  
- High availability and horizontal scalability  
- Optimized performance for frequent read/write operations  
- Use of **appropriate processing frameworks** for:
  - Engagement scoring
  - Course-level analytics
- Integration of a **visualization dashboard**
- Optional: advanced features and demo video

---

## 🏗️ Architecture Overview

The system is built using a **polyglot persistence approach**, selecting the most suitable technology for each task:

- **MongoDB** – Flexible storage of student activities and profiles  
- **Redis** – Real-time engagement score storage and retrieval  
- **Neo4j** – Graph-based detection of multi-region access patterns  
- **Apache Cassandra** – Scalable storage for aggregated analytics  
- **Apache Spark** – Batch analytics and data processing  
- **Grafana** – Visualization of engagement metrics and analytics  





