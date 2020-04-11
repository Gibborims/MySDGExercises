import math
def estimator(data):
  output_data = {}
  impact = {}
  severeImpact = {}

  reported_cases = data["reportedCases"]
  currently_infected = covid19ImpactEstimator(reported_cases)
  severe_currently_infected = covid19SevereImpactEstimator(reported_cases)

  period_type = data["periodType"]
  duration = data["timeToElapse"]
  total_hospital_beds = data["totalHospitalBeds"]

  infections_time = infectionsByRequestedTime(currently_infected, period_type, duration)
  severe_infections_time = infectionsByRequestedTime(severe_currently_infected, period_type, duration)
  case_by_time = severeCasesByRequestedTime(infections_time)
  severe_case_by_time = severeCasesByRequestedTime(severe_infections_time)
  hosp_beds_by_reqtime = hospitalBedsByRequestedTime(total_hospital_beds, case_by_time)
  severe_hosp_beds_by_reqtime = hospitalBedsByRequestedTime(total_hospital_beds, severe_case_by_time)

  impact["currentlyInfected"] = currently_infected
  impact["infectionsByRequestedTime"] = infections_time
  impact["severeCasesByRequestedTime"] = case_by_time
  impact["hospitalBedsByRequestedTime"] = hosp_beds_by_reqtime

  severeImpact["currentlyInfected"] = severe_currently_infected
  severeImpact["infectionsByRequestedTime"] = severe_infections_time
  severeImpact["severeCasesByRequestedTime"] = severe_case_by_time
  severeImpact["hospitalBedsByRequestedTime"] = severe_hosp_beds_by_reqtime

  output_data["data"] = data
  output_data["impact"] = impact
  output_data["severeImpact"] = severeImpact

  # print(output_data)
  return output_data


def covid19ImpactEstimator(reported_cases):
  return (reported_cases * 10)


def covid19SevereImpactEstimator(reported_cases):
  return (reported_cases * 50)


def daysFactor(days):
  # return (days % 3)
  return math.trunc(days/3)


def dayNormalizer(period_type, duration):
  days = 0
  if (period_type == "days"):
    days = int(duration)
  elif (period_type == "weeks"):
    days = int(duration) * 7
  elif (period_type == "months"):
    days = int(duration) * 30
  else:
    days = duration

  return int(days)



def infectionsByRequestedTime(currently_infected, period_type, duration):
  days = dayNormalizer(period_type, duration)
  return (currently_infected * (2 ** (daysFactor(days))))


def severeCasesByRequestedTime(infections_by_time):
  return math.trunc(0.15 * infections_by_time)


def required_available_beds(total_hospital_beds):
  return math.trunc(0.35 * total_hospital_beds)


def hospitalBedsByRequestedTime(total_hospital_beds, severe_case_by_time):
  req_available_beds = required_available_beds(total_hospital_beds)
  return (req_available_beds - severe_case_by_time)



# data = {
#   "region": {
#     "name": "Africa",
#     "avgAge": 19.7,
#     "avgDailyIncomeInUSD": 5,
#     "avgDailyIncomePopulation": 0.71
#   },
#   "periodType": "days",
#   "timeToElapse": 58,
#   "reportedCases": 674,
#   "population": 66622705,
#   "totalHospitalBeds": 1380614
# }

# estimator(data)
