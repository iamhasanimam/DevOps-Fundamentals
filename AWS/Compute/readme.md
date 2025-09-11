# AWS Compute Services – Notes & Documentation  

---

## 📌 Objectives  
- Understand the types of compute services AWS provides.  
- Explore **scalability, elasticity, and serverless computing**.  
- Learn when to use EC2, Lambda, ECS, and Elastic Beanstalk.  
- Understand pricing models and best practices.  

---

## 💻 Core Compute Services  

### 1. Amazon EC2 (Elastic Compute Cloud)  
- Virtual servers in the cloud.  
- Offers instance families (General Purpose, Compute Optimized, Memory Optimized, etc.).  
- Features: Auto Scaling, Elastic Load Balancing, AMIs.  
- Pricing models: On-Demand, Reserved, Spot, Savings Plans.  

### 2. AWS Lambda  
- **Serverless compute** (runs code without provisioning servers).  
- Event-driven (e.g., API Gateway trigger, S3 file upload).  
- Pricing: Pay only for compute time used (per ms).  

### 3. Amazon ECS (Elastic Container Service)  
- Managed container orchestration.  
- Runs Docker containers on EC2 or Fargate.  
- Integrates with IAM, CloudWatch, and ALB.  

### 4. AWS Fargate  
- Serverless compute engine for ECS and EKS.  
- Eliminates the need to manage EC2 instances for containers.  

### 5. AWS Elastic Beanstalk  
- Platform as a Service (PaaS).  
- Deploy web apps quickly (supports Node.js, Python, Java, etc.).  
- Handles provisioning, load balancing, scaling, monitoring.  

### 6. Amazon Lightsail  
- Simple VPS solution for beginners and small apps.  
- Comes with pre-configured dev stacks (WordPress, LAMP, etc.).  
- Flat monthly pricing.  

---

## ⚡ Scalability & Elasticity  
- **Vertical scaling**: Increase resources (CPU/RAM) on one instance.  
- **Horizontal scaling**: Add more instances behind a load balancer.  
- Elasticity = automatic scaling up/down based on demand.  

