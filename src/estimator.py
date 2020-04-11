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

  infections_time = infectionsByRequestedTime(currently_infected, period_type, duration)
  severe_infections_time = infectionsByRequestedTime(severe_currently_infected, period_type, duration)

  impact["currentlyInfected"] = currently_infected
  impact["infectionsByRequestedTime"] = infections_time

  severeImpact["currentlyInfected"] = severe_currently_infected
  severeImpact["infectionsByRequestedTime"] = severe_infections_time

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
