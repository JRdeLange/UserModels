name = c('Chiel', "Nico", "Alissa", 'Patrick', 'Cosmin', 'Joshua', 'Loran', 'Levi')
correct = c(11, 12, 10, 6, 10, 16, 26, 17)
condition = c('Random', 'Random', 'Random', 'Random', 'Ordered', 'Ordered', 'Ordered', 'Ordered')

dat = data.frame(name, correct, condition)
dat$percentOfTotal = c(11/18, 12/12, 10/20, 6/13, 10/17, 16/22, 26/27, 17/24)

summary(dat)
aggregate(dat$correct, by=list(dat$condition), mean)
Rdat = subset(dat, dat$condition == "Random")
Odat = subset(dat, dat$condition == "Ordered")

t.test(Rdat$correct, Odat$correct)


resdat<- read.csv(file="results.csv", header=TRUE, sep=",")
Rallresdat = subset(resdat, resdat$Hierarchy == "False")
Oallresdat = subset(resdat, resdat$Hierarchy == "True")

t.test(Rallresdat$RT, Oallresdat$RT)


Rspeciesresdat = subset(resdat, resdat$Hierarchy == "False" & resdat$Question_type == "Species")
Ospeciesresdat = subset(resdat, resdat$Hierarchy == "True" & resdat$Question_type == "Species")

t.test(Rspeciesresdat$RT, Ospeciesresdat$RT)


Rtextresdat = subset(resdat, resdat$Hierarchy == "False" & resdat$Question_type == "Non-Species")
Otextresdat = subset(resdat, resdat$Hierarchy == "True" & resdat$Question_type == "Non-Species")

t.test(Rtextresdat$RT, Otextresdat$RT)

aggregate(dat$percentOfTotal, by=list(dat$condition), mean)
t.test(Rdat$percentOfTotal, Odat$percentOfTotal)




CorResDat = subset(resdat, resdat$Correct == "True")

Rallcorresdat = subset(CorResDat, CorResDat$Hierarchy == "False")
Oallcorresdat = subset(CorResDat, CorResDat$Hierarchy == "True")

t.test(Rallcorresdat$RT, Oallcorresdat$RT)


Rspeciescorresdat = subset(CorResDat, CorResDat$Hierarchy == "False" & CorResDat$Question_type == "Species")
Ospeciescorresdat = subset(CorResDat, CorResDat$Hierarchy == "True" & CorResDat$Question_type == "Species")

t.test(Rspeciescorresdat$RT, Ospeciescorresdat$RT)


Rtextcorresdat = subset(CorResDat, CorResDat$Hierarchy == "False" & CorResDat$Question_type == "Non-Species")
Otextcorresdat = subset(CorResDat, CorResDat$Hierarchy == "True" & CorResDat$Question_type == "Non-Species")

t.test(Rtextcorresdat$RT, Otextcorresdat$RT)


