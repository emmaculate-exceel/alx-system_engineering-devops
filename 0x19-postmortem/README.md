Postmortem : In system_admin/devops Postmortem is the act of Writing out incident report and also the act of escalating an error/system-downtime in a server, machine , programme and many more and how the issue is being resolved.

The structure of the Architecture is as follows:
#Issue Summary:
 i  :short summary (5 sentences)
 ii :list the duration along with the start and end times (include timezone)
 iii:state the impact(most user requests resulted in 500 errors, at peak 100%)
 iv :close with root cause

#Timeline
 i  :list the timezone
 ii :covers the outage duration
 iii:when outage began
 iv :when staff notified
 v  :actions, events
 vi :when service was restored

#Root Cause
 i  :given a detailed explaination of events
 ii :do not sugarcoat

#Resolution and recovery
 i  : give a detailed explaination of actions taken (includes times)

#Corrective and Preventive Measures
 i  :itemized list of ways to prevent it from happening again
 ii :what we can do to make it better next time.