### Non-profit Company:

Dewgood is a small, local non-profit company of 50 employees. They hired you as the sole IT person in the company. The HR person tells you when they need a new computer for an employee. Currently, computers are purchased directly in a physical store on the day that an employee is hired. This is due to budget reasons, as they can’t keep extra stock in the store.

The company has a single server with multiple services on it, a file server, and email. They don’t currently have a messaging system in place. When a new employee is hired, you have to do an orientation with them for login. You’re also responsible for installing all the software they need on their machine, and mapping the file server to their computer. The computers are managed through Windows Active Directory. When an employee leaves, they’re currently not disabled in the directory service.

The company uses an open-source ticketing system to handle all internal requests as well as external non-profit requests. But the ticketing system is confusing and difficult to use, so lots of the employees reach out to you directly to figure out how to do things. In fact, so many things are difficult to find that employees typically ask around when they have a question.

There are nightly backups in place of the file server. You store this information on a disk backup and take it home with you everyday to keep it safe in case something happens onsite. There’s also a small company website that’s hosted on the single server at the company. This website is a single html page that explains the mission of the company and provides contact information. The website has gone down many times, and no one knows what to do when it happens.

### My solution:

Firstly, I think this org should reconfigure AD with roles and GPOs for users so that they can have software automatically installed on their machines at login. When an employee leaves, we can delete the user account to disable the person to access company’s system again.

Secondly, taking the backup disk home with IT person daily is a suggested way. This condition may happen that things being stolen or lost with carelessness. A more secure way is keeping the backup on three different places: the cloud, the local machine, and a separate disk.

Thirdly, training an employee to be responsible for explaining the problems the user or internal person meet when using the open-source ticketing system and make a clear brochure to explain how to use the system. Or otherwise, find an alternative solution to instead of the open source solution.

Fourthly, we can build and maintain a well optimized corporate computer OS Images which some of the working software were pre-installed. So, we can save the workload in the next time when we provide a new computer.

Finally, the company’s website is the face of the company. In my understanding there are lots of workload to maintain a beautiful and attracting website locally. We can move it for a third-party hosting service. It is surely not a large expense.
 
