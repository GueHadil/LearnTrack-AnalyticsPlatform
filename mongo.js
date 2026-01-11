// Create database
use learntrack;

// Insert student profiles
db.students.insertMany([
  { studentId:"S1", name:"Hadil", email:"hadil@mail.com", speciality:"ILSI", studentLevel:"M2", progress:10, lastUpdated:new Date() },
  { studentId:"S2", name:"Lina", email:"lina@mail.com", speciality:"SCI", studentLevel:"M1", progress:20, lastUpdated:new Date() },
  { studentId:"S3", name:"Slimane", email:"slim@mail.com", speciality:"ILSI", studentLevel:"M2", progress:30, lastUpdated:new Date() },
  { studentId:"S4", name:"Amine", email:"amine@mail.com", speciality:"STIW", studentLevel:"L3", progress:40, lastUpdated:new Date() },
  { studentId:"S5", name:"Chanez", email:"chanez@mail.com", speciality:"SDSI", studentLevel:"L2", progress:50, lastUpdated:new Date() },
  { studentId:"S6", name:"Feriel", email:"feriel@mail.com", speciality:"STIC", studentLevel:"M1", progress:60, lastUpdated:new Date() },
  { studentId:"S7", name:"Cylia", email:"cylia@mail.com", speciality:"SI", studentLevel:"L3", progress:25, lastUpdated:new Date() },
  { studentId:"S8", name:"Lydia", email:"lydia@mail.com", speciality:"ILSI", studentLevel:"M2", progress:35, lastUpdated:new Date() },
  { studentId:"S9", name:"Kenza", email:"kenza@mail.com", speciality:"TI", studentLevel:"L3", progress:45, lastUpdated:new Date() },
  { studentId:"S10", name:"Ahmed", email:"ahmed@mail.com", speciality:"SDIA", studentLevel:"M1", progress:55, lastUpdated:new Date() }
]);

// Insert student activity logs
db.activities.insertMany([
  { studentId:"S1", courseId:"C1", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S1", courseId:"C1", action:"quiz_attempt", timestamp:new Date(), region:"EU" },
  { studentId:"S2", courseId:"C1", action:"quiz_attempt", timestamp:new Date(), region:"US" },
  { studentId:"S3", courseId:"C2", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S3", courseId:"C2", action:"quiz_attempt", timestamp:new Date(), region:"EU" },
  { studentId:"S4", courseId:"C2", action:"page_view", timestamp:new Date(), region:"AF" },
  { studentId:"S5", courseId:"C3", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S5", courseId:"C3", action:"quiz_attempt", timestamp:new Date(), region:"EU" },
  { studentId:"S6", courseId:"C3", action:"page_view", timestamp:new Date(), region:"US" },
  { studentId:"S6", courseId:"C3", action:"quiz_attempt", timestamp:new Date(), region:"US" },
  { studentId:"S7", courseId:"C1", action:"page_view", timestamp:new Date(), region:"AF" },
  { studentId:"S7", courseId:"C1", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S8", courseId:"C2", action:"quiz_attempt", timestamp:new Date(), region:"ASIA" },
  { studentId:"S9", courseId:"C3", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S9", courseId:"C3", action:"quiz_attempt", timestamp:new Date(), region:"US" },
  { studentId:"S10", courseId:"C1", action:"page_view", timestamp:new Date(), region:"EU" },
  { studentId:"S10", courseId:"C1", action:"quiz_attempt", timestamp:new Date(), region:"EU" }
]);


//  Retrieve last 20 activities for a student
db.activities.find(
  {studentId:"S1"}
 ).sort({timestamp:-1}).limit(20)
 

//Update student profile
 db.students.updateOne(
   { studentId: "S5" },
   {
   $set: {
        email: "chanez123@mail.com",
		progress: 70,
		lastUpdated: new Date()
     }
   }
)