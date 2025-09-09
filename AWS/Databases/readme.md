#### 
Relational databases use a rigid schema that organizes collections of data into tables with rows and columns, where relationships exist between different tables. In this lesson, you will explore the benefits and use cases for AWS relational database services, including Amazon RDS and Amazon Aurora.


Amazon DMS : Amazon Database migration service


#### Relational databases

Relational databases store data in a way that relates it to other pieces of data, and they use structured query language, or SQL, to manage and query data. This approach stores data in an easily understandable, consistent, and scalable way that works great for applications requiring structured data management.

AWS offers fully managed relational database solutions that remove the burden of database administration while maintaining high availability and security. AWS relational databases support popular database engines like MySQL, PostgreSQL, and Oracle, making it easier to migrate existing databases to AWS.

An example of a relational database would be an inventory management system for a restaurant. Each record in the database includes data for a single item, such as product name, size, price, and so on. The following table shows how this type of data is configured in a relational database.


#### Amazon Relational Database Service (Amazon RDS)

Amazon RDS is a managed relational database service that handles routine database tasks such as backups, patching, and hardware provisioning. Amazon RDS supports multiple database instance class types that optimize for memory, performance, or input/output (I/O).

To improve data resilience, Amazon RDS offers Multi-AZ deployment and automated backups, but you can also manually create backups using DB snapshots. These are full backups of your entire database instance, which can be useful for specific point-in-time recovery or long-term data archiving purposes. Amazon RDS offers security features including network isolation, encryption in transit, and encryption at rest. You can readily scale database resources vertically or horizontally as needed.

Supported database engines
Amazon RDS supports different database engines, including Amazon Aurora, MySQL, PostgreSQL, Microsoft SQL Server, MariaDB, and Oracle Database.

Use cases
Some examples of practical use cases for Amazon RDS are web applications, enterprise workloads, and product inventories for e-commerce platforms.

#### Amazon Aurora

Aurora is a managed relational database designed to help reduce unnecessary I/O operations. It's compatible with MySQL and PostgreSQL, provides high performance and availability, and automatically scales alongside your workloads. Aurora replicates data across multiple Availability Zones for enhanced durability and fault tolerance, and features automated backups, encryption at rest, and continuous monitoring.

Use cases
Some examples of practical use cases for Aurora are gaming applications, media and content management, and real-time analytics.

#### Non relational Database

NoSQL databases use flexible data schemas for storing and retrieving many different types of information. In this lesson, you will explore the benefits and use cases of the NoSQL database service Amazon DynamoDB.

##### NoSQL databases

NoSQL databases are sometimes referred to as non-relational databases because their structures are different than relational databases like Amazon RDS. Instead of row and column relationships, NoSQL databases build a structure for the data that they contain using key-value pairs instead. With key-value pairs, data is organized into items identified by unique keys.

Each key has one or more associated attributes, or values, that represent various characteristics of the data. You can think of a key as a word entry in a dictionary, and the value as its associated definition. Not every item in the table has to have the same attributes, and you can add or remove attributes at any time.

The following table shows an example of how key-value paired data is stored in NoSQL databases.

##### Amazon DynamoDB

DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance for both document and key-value data structures. It's a powerful and incredibly fast database option for use cases that require a flexible schema, and is ideal for applications that require high performance and seamless scaling.

DynamoDB seamlessly scales alongside your data without impacting performance, which means that you only pay for the resources that you use. It also includes built-in security features for enhanced protection, and automatically spreads your data across multiple servers to handle your workload.

Use cases
Some examples of practical use cases for DynamoDB are gaming platforms, financial service applications, and mobile applications with global user bases.

#### In-memory caches

An in-memory cache is a high-speed storage layer that temporarily stores frequently accessed data in a computer's main memory, or RAM. Retrieving data from RAM provides extremely fast processing and retrieval speeds, often hundreds or thousands of times faster than traditional disk-based storage systems.

When applications need specific information, they first check the cache before requesting it from the original data source. This reduces the load on primary databases and speeds up response times for end users. In-memory caches are ideal for storing session data, API responses, database query results, and other information that applications require repeatedly.

#### Amazon ElastiCache

ElastiCache is a fully managed in-memory caching service that was built to help reduce the complexity of administering in-memory caching systems. This means that you can continue to use the same Redis, Valkey, or Memcached tools and configurations to scale your workloads. It automatically detects and replaces failed nodes, which makes it ideal for applications that need consistent high performance.

Use cases
Some examples of practical use cases for ElastiCache are session data management, database query enhancement, and gaming leaderboards.

#### Amazon DocumentDB

A MongoDB-compatible document database service designed for mission-critical workloads with automatic scaling

#### Amazon Backup

A centralized service for automating and managing data backups across AWS services and on-premises resources

#### Amazon Neptune

A graph database service optimized for storing and querying highly connected data relationships