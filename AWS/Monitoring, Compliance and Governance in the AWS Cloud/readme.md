### Monitoring

In the AWS Cloud, monitoring is the continuous process of collecting, visualizing, and tracking the health and performance of your AWS infrastructure, services, and applications. This goal of monitoring is to help ensure optimal performance and identify potential issues.

### Importance of monitoring

Monitoring your cloud resources is important. It provides a way for you to continuously observe and analyze system activity, network traffic, and security events to detect potential threats or anomalies. Monitoring and observability are critical components for ensuring the security, availability, reliability, and performance of your cloud-based workloads and data.

#### Amazon CloudWatch

CloudWatch monitors your AWS resources and the applications that you run on AWS in real time. With CloudWatch, you gain system-wide visibility into resource utilization, application performance, and operational health.  CloudWatch does more than just monitor. It has several features that work together:

CloudWatch metrics

CloudWatch alarms

CloudWatch dashboards

CloudWatch logs

#### Importance of auditing

Imagine a financial company with a hybrid cloud solution trying to figure out what happened when there are changes made to their resources in the cloud and on premises. They need this information for troubleshooting and to provide detailed records for compliance. That's where CloudTrail can help.

#### AWS CloudTrail

CloudTrail tracks user activity and API usage in the AWS Cloud, on premises, and even with other cloud providers. CloudTrail provides a detailed history of API calls, so you can track changes and identify who made them and when. This helps you understand what actions were taken on your AWS resources.

Benefits: CloudTrail provides auditing, security monitoring, and operational troubleshooting. It also helps you prove compliance and improve your security posture.

Use cases: It can be used for compliance and auditing, identifying security incidents, troubleshooting operational issues.

#### CloudTrail events
CloudTrail events capture details about actions performed within your AWS account, such as API calls, console actions, or other activities. Event history provides a viewable, searchable, downloadable, and immutable record of the past 90 days of management events in an AWS Region. There are no CloudTrail charges for viewing event history.

#### CloudTrail logs
CloudTrail monitors events and delivers those events as log files to your Amazon Simple Storage Service (Amazon S3) bucket. Because CloudTrail logs are securely stored, they can be used to prove compliance with regulations such as Payment Card Industry (PCI) and Healthcare Insurance Portability and Accountability Act (HIPAA).

#### CloudTrail Insights
CloudTrail Insights analyzes your normal patterns of API call volume and API error rates. CloudTrail Insights also generates Insights events when API call volumes and error rates deviate from these normal patterns. You can enable CloudTrail Insights in your trails or event data stores to detect anomalous behavior and unusual activity.

#### Benefits of compliance with AWS

Compliance refers to your cloud resources and data adhering to relevant regulations, industry standards, and internal policies regarding security and data protection. AWS helps you meet compliance goals and requirements in the following ways:

Inheriting the latest security controls that AWS uses on its own infrastructure

Third-party validation for thousands of global requirements

Streamlining and automating compliance

On-demand compliance reports

#### AWS Artifact Agreements
Suppose that your company needs to sign an agreement with AWS regarding your use of certain types of information throughout AWS services. You can do this through AWS Artifact Agreements.

In AWS Artifact Agreements, you can review, accept, and manage agreements for an individual account and for all your accounts in AWS Organizations. Different types of agreements are offered to address the needs of customers who are subject to specific regulations, such as the Health Insurance Portability and Accountability Act (HIPAA).

#### AWS Artifact Reports
Next, suppose that a member of your company’s development team is building an application and needs more information about their responsibility for complying with certain regulatory standards. You can advise them to access this information in AWS Artifact Reports.

AWS Artifact Reports provide compliance reports from third-party auditors. These auditors have tested and verified that AWS is compliant with a variety of global, regional, and industry-specific security standards and regulations. AWS Artifact Reports remains up to date with the latest reports released. You can provide the AWS audit artifacts to your auditors or regulators as evidence of AWS security controls.

#### AWS Config

AWS Config is a service that you can use to assess, audit, and evaluate the configurations of your AWS resources.

Benefits: AWS Config helps evaluate configurations against a desired state, manage resource configuration changes, and simplify troubleshooting and remediation.

Use cases: It can be used to continually audit security monitoring and analysis and to streamline operational troubleshooting and change management.

#### AWS Audit Manager

Audit Manager is a service that continually audits your AWS usage to simplify risk and compliance assessment. It helps collect evidence and manage audit data.

Benefits: Audit Manager saves time with automated evidence collection, streamlines collaboration across teams, and helps ensure integrity of audits with read-only permissions.

Use case: It can be used to automate evidence collection, continually audit to assess compliance, and deploy internal risk assessments.