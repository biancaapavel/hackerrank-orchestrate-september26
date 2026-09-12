# Public-sample error report

Diagnostic use only: labels are never loaded by full-dataset inference.

Samples: 25. Mean absolute safe-amount error / requested amount: 5.20971030%.

| Field | Exact matches |
| --- | --- |
| amount_safe_to_pay | 2 |
| affordability_status | 22 |
| recommended_payment_method | 24 |
| payment_plan | 23 |
| earliest_date_for_full_payment | 19 |
| spending_changes_needed | 21 |

Signed errors below are actual minus expected, in each user's home currency.

| Request | Expected safe | Actual safe | Error | Absolute / request | Trough day | Trough headroom | Salary mode |
| --- | --- | --- | --- | --- | --- | --- | --- |
| request_01 | 25256 | 25256 | 0 | 0.0000% | 10 | 30241.27 | historical |
| request_02 | 17229139.2 | 18336765.49 | 1107626.29 | 2.4069% | 8 | 18336765.49 | increase |
| request_03 | 873000 | 1121649.65 | 248649.65 | 4.5283% | 11 | 1121649.65 | historical |
| request_04 | 8401800 | 12357921.14 | 3956121.14 | 31.1677% | 9 | 12357921.14 | historical |
| request_05 | 737 | 0 | -737 | 4.7585% | 90 | -4939.19 | historical |
| request_06 | 603.3 | 615.58 | 12.28 | 1.9794% | 10 | 615.58 | temporary |
| request_07 | 87170.56 | 86237.22 | -933.34 | 0.4728% | 15 | 86237.22 | delay |
| request_08 | 284.57 | 285.2 | 0.63 | 0.0632% | 6 | 285.2 | reduced |
| request_09 | 166.61 | 151.96 | -14.65 | 8.7930% | 90 | 151.96 | historical |
| request_10 | 12700 | 0 | -12700 | 4.7619% | 90 | -47349.22 | unconfirmed_gig |
| request_11 | 12510645 | 12319866.62 | -190778.38 | 1.4552% | 11 | 12319866.62 | base_only |
| request_12 | 65164 | 60370.23 | -4793.77 | 7.3565% | 87 | 60370.23 | ended |
| request_13 | 433.4 | 812.13 | 378.73 | 40.2220% | 68 | 812.13 | historical |
| request_14 | 597.74 | 616.29 | 18.55 | 0.3426% | 10 | 616.29 | resumed |
| request_15 | 83.05 | 5.08 | -77.97 | 2.1159% | 8 | 5.08 | new_job |
| request_16 | 122500 | 122500 | 0 | 0.0000% | 33 | 149715.53 | historical |
| request_17 | 243849.58 | 243023.67 | -825.91 | 0.3008% | 13 | 243023.67 | historical |
| request_18 | 462 | 546.05 | 84.05 | 2.5893% | 7 | 546.05 | historical |
| request_19 | 28820 | 25176.15 | -3643.85 | 9.1877% | 10 | 25176.15 | historical |
| request_20 | 5400 | 8969.68 | 3569.68 | 1.1754% | 6 | 8969.68 | historical |
| request_21 | 1543.35 | 1574.4 | 31.05 | 1.9722% | 9 | 1673.13 | historical |
| request_22 | 475.46 | 480.69 | 5.23 | 0.7150% | 9 | 480.69 | historical |
| request_23 | 9152 | 8360.17 | -791.83 | 2.0829% | 7 | 8360.17 | historical |
| request_24 | 13420 | 13539.29 | 119.29 | 0.1088% | 9 | 13539.29 | historical |
| request_25 | 1425000 | 2445438.17 | 1020438.17 | 1.6868% | 8 | 2445438.17 | historical |

## request_01 â€” user_01 (ZAR)

Request: 25256 on 2024-03-03; deadline 2024-03-20. Opening 58481.1; minimum 18000.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 25256 | 25256 | yes |
| affordability_status | affordable_now | affordable_now | yes |
| recommended_payment_method | full_payment | full_payment | yes |
| payment_plan | 2024-03-03:25256 | 2024-03-03:25256 | yes |
| earliest_date_for_full_payment | 2024-03-03 | 2024-03-03 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 10 (2024-03-13), balance 48241.27, headroom 30241.27.

Protected: rent|education|groceries|debt_repayment. Reduce: dining. Stop: delivery_membership.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_29 | debt_repayment / Education loan instalment | 5 / 5 | 3487 | 3487.00 | 3487â€“3487 | 3487 | 2024-03-11, 2024-04-11, 2024-05-11 |
| event_31 | delivery_membership / Delivery service plan | 5 / 5 | 306.9 | 306.90 | 306.9â€“306.9 | 306.9 | 2024-03-13, 2024-04-13, 2024-05-13 |
| event_97 | dining / Family dinner | 13 / 6 | 1089.188461538461538461538462 | 1070.17 | 914.64â€“1243.56 | 1089.19 | 2024-03-10, 2024-03-24, 2024-04-07, 2024-04-21, 2024-05-05, 2024-05-19 |
| event_28 | education / Professional training fee | 5 / 5 | 1821.6 | 1821.60 | 1821.6â€“1821.6 | 1821.6 | 2024-03-08, 2024-04-08, 2024-05-08 |
| event_58 | groceries / Local market purchase | 26 / 7 | 785.1373076923076923076923077 | 761.015 | 602.87â€“1030.1 | 785.14 | 2024-03-08, 2024-03-15, 2024-03-22, 2024-03-29, 2024-04-05, 2024-04-12, 2024-04-19, 2024-04-26, 2024-05-03, 2024-05-10, 2024-05-17, 2024-05-24, 2024-05-31 |
| event_30 | music_subscription / Music service subscription | 5 / 5 | 235.4 | 235.40 | 235.4â€“235.4 | 235.4 | 2024-03-11, 2024-04-11, 2024-05-11 |
| event_32 | rent / Apartment rent transfer | 6 / 6 | 5148 | 5148.00 | 5148â€“5148 | 5148 | 2024-04-02, 2024-05-02 |
| event_84 | transport / Local taxi | 26 / 7 | 439.1965384615384615384615385 | 426.74 | 323.58â€“560.21 | 439.2 | 2024-03-09, 2024-03-16, 2024-03-23, 2024-03-30, 2024-04-06, 2024-04-13, 2024-04-20, 2024-04-27, 2024-05-04, 2024-05-11, 2024-05-18, 2024-05-25, 2024-06-01 |
| event_27 | utilities / Household utility payment | 5 / 5 | 1507.8 | 1483.81 | 1386.17â€“1651.81 | 1507.8 | 2024-03-06, 2024-04-06, 2024-05-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-03-05 | -567.6 | event_102 | transport | explicit_event | Pending fuel authorization |
| 2024-03-06 | -1507.8 | event_27 | utilities | recurring_expense | Household utility payment |
| 2024-03-08 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-03-08 | -1821.6 | event_28 | education | recurring_expense | Professional training fee |
| 2024-03-09 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-03-10 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-03-11 | -235.4 | event_30 | music_subscription | recurring_expense | Music service subscription |
| 2024-03-11 | -3487 | event_29 | debt_repayment | recurring_expense | Education loan instalment |
| 2024-03-13 | -306.9 | event_31 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-03-15 | 23320 | event_103 | salary | recurring_income | Next confirmed salary |
| 2024-03-15 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-03-16 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-03-22 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-03-23 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-03-24 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-03-29 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-03-30 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-04-02 | -5148 | event_32 | rent | recurring_expense | Apartment rent transfer |
| 2024-04-05 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-04-06 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-04-06 | -1507.8 | event_27 | utilities | recurring_expense | Household utility payment |
| 2024-04-07 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-04-08 | -1821.6 | event_28 | education | recurring_expense | Professional training fee |
| 2024-04-11 | -235.4 | event_30 | music_subscription | recurring_expense | Music service subscription |
| 2024-04-11 | -3487 | event_29 | debt_repayment | recurring_expense | Education loan instalment |
| 2024-04-12 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-04-13 | -306.9 | event_31 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-04-13 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-04-15 | 23320 | event_103 | salary | recurring_income | Next confirmed salary |
| 2024-04-19 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-04-20 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-04-21 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-04-26 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-04-27 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-05-02 | -5148 | event_32 | rent | recurring_expense | Apartment rent transfer |
| 2024-05-03 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-05-04 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-05-05 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-05-06 | -1507.8 | event_27 | utilities | recurring_expense | Household utility payment |
| 2024-05-08 | -1821.6 | event_28 | education | recurring_expense | Professional training fee |
| 2024-05-10 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-05-11 | -235.4 | event_30 | music_subscription | recurring_expense | Music service subscription |
| 2024-05-11 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-05-11 | -3487 | event_29 | debt_repayment | recurring_expense | Education loan instalment |
| 2024-05-13 | -306.9 | event_31 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-05-15 | 23320 | event_103 | salary | recurring_income | Next confirmed salary |
| 2024-05-17 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-05-18 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-05-19 | -1089.19 | event_97 | dining | recurring_expense | Family dinner |
| 2024-05-24 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-05-25 | -439.2 | event_84 | transport | recurring_expense | Local taxi |
| 2024-05-31 | -785.14 | event_58 | groceries | recurring_expense | Local market purchase |
| 2024-06-01 | -439.2 | event_84 | transport | recurring_expense | Local taxi |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-03-03 | 0 | 58481.1 | 40481.1 | 33225.1 | 33225.1 | 25256 | (empty) |
| 1 | 2024-03-04 | 0 | 58481.1 | 40481.1 | 33225.1 | 33225.1 | 0 | (empty) |
| 2 | 2024-03-05 | -567.6 | 57913.5 | 39913.5 | 32657.5 | 32657.5 | 0 | event_102 |
| 3 | 2024-03-06 | -1507.8 | 56405.7 | 38405.7 | 31149.7 | 31149.7 | 0 | event_27 |
| 4 | 2024-03-07 | 0 | 56405.7 | 38405.7 | 31149.7 | 31149.7 | 0 | (empty) |
| 5 | 2024-03-08 | -2606.74 | 53798.96 | 35798.96 | 28542.96 | 28542.96 | 0 | event_58, event_28 |
| 6 | 2024-03-09 | -439.2 | 53359.76 | 35359.76 | 28103.76 | 28103.76 | 0 | event_84 |
| 7 | 2024-03-10 | -1089.19 | 52270.57 | 34270.57 | 27014.57 | 27014.57 | 0 | event_97 |
| 8 | 2024-03-11 | -3722.4 | 48548.17 | 30548.17 | 23292.17 | 23292.17 | 0 | event_30, event_29 |
| 9 | 2024-03-12 | 0 | 48548.17 | 30548.17 | 23292.17 | 23292.17 | 0 | (empty) |
| 10 | 2024-03-13 | -306.9 | 48241.27 | 30241.27 | 22985.27 | 22985.27 | 0 | event_31 |
| 11 | 2024-03-14 | 0 | 48241.27 | 30241.27 | 22985.27 | 22985.27 | 0 | (empty) |
| 12 | 2024-03-15 | 22534.86 | 70776.13 | 52776.13 | 45520.13 | 45520.13 | 0 | event_103, event_58 |
| 13 | 2024-03-16 | -439.2 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | event_84 |
| 14 | 2024-03-17 | 0 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | (empty) |
| 15 | 2024-03-18 | 0 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | (empty) |
| 16 | 2024-03-19 | 0 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | (empty) |
| 17 | 2024-03-20 | 0 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | (empty) |
| 18 | 2024-03-21 | 0 | 70336.93 | 52336.93 | 45080.93 | 45080.93 | 0 | (empty) |
| 19 | 2024-03-22 | -785.14 | 69551.79 | 51551.79 | 44295.79 | 44295.79 | 0 | event_58 |
| 20 | 2024-03-23 | -439.2 | 69112.59 | 51112.59 | 43856.59 | 43856.59 | 0 | event_84 |
| 21 | 2024-03-24 | -1089.19 | 68023.4 | 50023.4 | 42767.4 | 42767.4 | 0 | event_97 |
| 22 | 2024-03-25 | 0 | 68023.4 | 50023.4 | 42767.4 | 42767.4 | 0 | (empty) |
| 23 | 2024-03-26 | 0 | 68023.4 | 50023.4 | 42767.4 | 42767.4 | 0 | (empty) |
| 24 | 2024-03-27 | 0 | 68023.4 | 50023.4 | 42767.4 | 42767.4 | 0 | (empty) |
| 25 | 2024-03-28 | 0 | 68023.4 | 50023.4 | 42767.4 | 42767.4 | 0 | (empty) |
| 26 | 2024-03-29 | -785.14 | 67238.26 | 49238.26 | 41982.26 | 41982.26 | 0 | event_58 |
| 27 | 2024-03-30 | -439.2 | 66799.06 | 48799.06 | 41543.06 | 41543.06 | 0 | event_84 |
| 28 | 2024-03-31 | 0 | 66799.06 | 48799.06 | 41543.06 | 41543.06 | 0 | (empty) |
| 29 | 2024-04-01 | 0 | 66799.06 | 48799.06 | 41543.06 | 41543.06 | 0 | (empty) |
| 30 | 2024-04-02 | -5148 | 61651.06 | 43651.06 | 36395.06 | 36395.06 | 0 | event_32 |
| 31 | 2024-04-03 | 0 | 61651.06 | 43651.06 | 36395.06 | 36395.06 | 0 | (empty) |
| 32 | 2024-04-04 | 0 | 61651.06 | 43651.06 | 36395.06 | 36395.06 | 0 | (empty) |
| 33 | 2024-04-05 | -785.14 | 60865.92 | 42865.92 | 35609.92 | 35609.92 | 0 | event_58 |
| 34 | 2024-04-06 | -1947 | 58918.92 | 40918.92 | 33662.92 | 33662.92 | 0 | event_84, event_27 |
| 35 | 2024-04-07 | -1089.19 | 57829.73 | 39829.73 | 32573.73 | 32573.73 | 0 | event_97 |
| 36 | 2024-04-08 | -1821.6 | 56008.13 | 38008.13 | 30752.13 | 30752.13 | 0 | event_28 |
| 37 | 2024-04-09 | 0 | 56008.13 | 38008.13 | 30752.13 | 30752.13 | 0 | (empty) |
| 38 | 2024-04-10 | 0 | 56008.13 | 38008.13 | 30752.13 | 30752.13 | 0 | (empty) |
| 39 | 2024-04-11 | -3722.4 | 52285.73 | 34285.73 | 27029.73 | 27029.73 | 0 | event_30, event_29 |
| 40 | 2024-04-12 | -785.14 | 51500.59 | 33500.59 | 26244.59 | 26244.59 | 0 | event_58 |
| 41 | 2024-04-13 | -746.1 | 50754.49 | 32754.49 | 25498.49 | 25498.49 | 0 | event_31, event_84 |
| 42 | 2024-04-14 | 0 | 50754.49 | 32754.49 | 25498.49 | 25498.49 | 0 | (empty) |
| 43 | 2024-04-15 | 23320 | 74074.49 | 56074.49 | 48818.49 | 48818.49 | 0 | event_103 |
| 44 | 2024-04-16 | 0 | 74074.49 | 56074.49 | 48818.49 | 48818.49 | 0 | (empty) |
| 45 | 2024-04-17 | 0 | 74074.49 | 56074.49 | 48818.49 | 48818.49 | 0 | (empty) |
| 46 | 2024-04-18 | 0 | 74074.49 | 56074.49 | 48818.49 | 48818.49 | 0 | (empty) |
| 47 | 2024-04-19 | -785.14 | 73289.35 | 55289.35 | 48033.35 | 48033.35 | 0 | event_58 |
| 48 | 2024-04-20 | -439.2 | 72850.15 | 54850.15 | 47594.15 | 47594.15 | 0 | event_84 |
| 49 | 2024-04-21 | -1089.19 | 71760.96 | 53760.96 | 46504.96 | 46504.96 | 0 | event_97 |
| 50 | 2024-04-22 | 0 | 71760.96 | 53760.96 | 46504.96 | 46504.96 | 0 | (empty) |
| 51 | 2024-04-23 | 0 | 71760.96 | 53760.96 | 46504.96 | 46504.96 | 0 | (empty) |
| 52 | 2024-04-24 | 0 | 71760.96 | 53760.96 | 46504.96 | 46504.96 | 0 | (empty) |
| 53 | 2024-04-25 | 0 | 71760.96 | 53760.96 | 46504.96 | 46504.96 | 0 | (empty) |
| 54 | 2024-04-26 | -785.14 | 70975.82 | 52975.82 | 45719.82 | 45719.82 | 0 | event_58 |
| 55 | 2024-04-27 | -439.2 | 70536.62 | 52536.62 | 45280.62 | 45280.62 | 0 | event_84 |
| 56 | 2024-04-28 | 0 | 70536.62 | 52536.62 | 45280.62 | 45280.62 | 0 | (empty) |
| 57 | 2024-04-29 | 0 | 70536.62 | 52536.62 | 45280.62 | 45280.62 | 0 | (empty) |
| 58 | 2024-04-30 | 0 | 70536.62 | 52536.62 | 45280.62 | 45280.62 | 0 | (empty) |
| 59 | 2024-05-01 | 0 | 70536.62 | 52536.62 | 45280.62 | 45280.62 | 0 | (empty) |
| 60 | 2024-05-02 | -5148 | 65388.62 | 47388.62 | 40132.62 | 40132.62 | 0 | event_32 |
| 61 | 2024-05-03 | -785.14 | 64603.48 | 46603.48 | 39347.48 | 39347.48 | 0 | event_58 |
| 62 | 2024-05-04 | -439.2 | 64164.28 | 46164.28 | 38908.28 | 38908.28 | 0 | event_84 |
| 63 | 2024-05-05 | -1089.19 | 63075.09 | 45075.09 | 37819.09 | 37819.09 | 0 | event_97 |
| 64 | 2024-05-06 | -1507.8 | 61567.29 | 43567.29 | 36311.29 | 36311.29 | 0 | event_27 |
| 65 | 2024-05-07 | 0 | 61567.29 | 43567.29 | 36311.29 | 36311.29 | 0 | (empty) |
| 66 | 2024-05-08 | -1821.6 | 59745.69 | 41745.69 | 34489.69 | 34489.69 | 0 | event_28 |
| 67 | 2024-05-09 | 0 | 59745.69 | 41745.69 | 34489.69 | 34489.69 | 0 | (empty) |
| 68 | 2024-05-10 | -785.14 | 58960.55 | 40960.55 | 33704.55 | 33704.55 | 0 | event_58 |
| 69 | 2024-05-11 | -4161.6 | 54798.95 | 36798.95 | 29542.95 | 29542.95 | 0 | event_30, event_84, event_29 |
| 70 | 2024-05-12 | 0 | 54798.95 | 36798.95 | 29542.95 | 29542.95 | 0 | (empty) |
| 71 | 2024-05-13 | -306.9 | 54492.05 | 36492.05 | 29236.05 | 29236.05 | 0 | event_31 |
| 72 | 2024-05-14 | 0 | 54492.05 | 36492.05 | 29236.05 | 29236.05 | 0 | (empty) |
| 73 | 2024-05-15 | 23320 | 77812.05 | 59812.05 | 52556.05 | 52556.05 | 0 | event_103 |
| 74 | 2024-05-16 | 0 | 77812.05 | 59812.05 | 52556.05 | 52556.05 | 0 | (empty) |
| 75 | 2024-05-17 | -785.14 | 77026.91 | 59026.91 | 51770.91 | 51770.91 | 0 | event_58 |
| 76 | 2024-05-18 | -439.2 | 76587.71 | 58587.71 | 51331.71 | 51331.71 | 0 | event_84 |
| 77 | 2024-05-19 | -1089.19 | 75498.52 | 57498.52 | 50242.52 | 50242.52 | 0 | event_97 |
| 78 | 2024-05-20 | 0 | 75498.52 | 57498.52 | 50242.52 | 50242.52 | 0 | (empty) |
| 79 | 2024-05-21 | 0 | 75498.52 | 57498.52 | 50242.52 | 50242.52 | 0 | (empty) |
| 80 | 2024-05-22 | 0 | 75498.52 | 57498.52 | 50242.52 | 50242.52 | 0 | (empty) |
| 81 | 2024-05-23 | 0 | 75498.52 | 57498.52 | 50242.52 | 50242.52 | 0 | (empty) |
| 82 | 2024-05-24 | -785.14 | 74713.38 | 56713.38 | 49457.38 | 49457.38 | 0 | event_58 |
| 83 | 2024-05-25 | -439.2 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | event_84 |
| 84 | 2024-05-26 | 0 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | (empty) |
| 85 | 2024-05-27 | 0 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | (empty) |
| 86 | 2024-05-28 | 0 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | (empty) |
| 87 | 2024-05-29 | 0 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | (empty) |
| 88 | 2024-05-30 | 0 | 74274.18 | 56274.18 | 49018.18 | 49018.18 | 0 | (empty) |
| 89 | 2024-05-31 | -785.14 | 73489.04 | 55489.04 | 48233.04 | 48233.04 | 0 | event_58 |
| 90 | 2024-06-01 | -439.2 | 73049.84 | 55049.84 | 47793.84 | 47793.84 | 0 | event_84 |

## request_02 â€” user_02 (IDR)

Request: 46018000 on 2025-08-05; deadline 2025-10-10. Opening 60383889.2; minimum 29158400.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 17229139.2 | 18336765.49 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | installments | installments | yes |
| payment_plan | 2025-08-08:15952906.67\|2025-09-07:15952906.67\|2025-10-07:15952906.67 | 2025-08-08:15952906.67\|2025-09-07:15952906.67\|2025-10-07:15952906.67 | yes |
| earliest_date_for_full_payment | 2025-09-15 | 2025-09-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 8 (2025-08-13), balance 47495165.49, headroom 18336765.49.

Protected: housing|utilities|education. Reduce: entertainment. Stop: cloud_storage.

Salary mode: increase. Evidence: message_01. Unparsed messages: none.

- message_01 (employer, 2025-07-29T09:30:00Z): Rincian penggajian Anda di Cobalt Systems telah berubah. Gaji bulanan Anda naik menjadi IDR 42750000. Perubahan ini berlaku mulai 2025-08-15. Jumlah yang diperbarui akan terlihat pada slip gaji berikutnya. Ref payroll EMP-0001.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_143 | cloud_storage / Shared storage plan | 5 / 5 | 369550 | 369550.00 | 369550â€“369550 | 369550 | 2025-08-13, 2025-09-13, 2025-10-13 |
| event_140 | education / Course tuition | 5 / 5 | 3040000 | 3040000.00 | 3040000â€“3040000 | 3040000 | 2025-08-09, 2025-09-09, 2025-10-09 |
| event_142 | entertainment / Cinema and events | 5 / 5 | 1298171.692 | 1289187.40 | 1193699.1â€“1367779.89 | 1298171.69 | 2025-08-15, 2025-09-15, 2025-10-15 |
| event_162 | groceries / Supermarket basket | 18 / 6 | 1908881.303333333333333333333 | 1917086.28 | 1418745.34â€“2477697.53 | 1908881.3 | 2025-08-09, 2025-08-19, 2025-08-29, 2025-09-08, 2025-09-18, 2025-09-28, 2025-10-08, 2025-10-18, 2025-10-28 |
| event_141 | healthcare / Clinic payment | 5 / 5 | 1538993.974 | 1538498.10 | 1452405.16â€“1641668.72 | 1538993.97 | 2025-08-11, 2025-09-11, 2025-10-11 |
| event_144 | housing / Home repair reserve | 6 / 6 | 3534000 | 3534000.00 | 3534000â€“3534000 | 3534000 | 2025-09-04, 2025-10-04 |
| event_139 | insurance / Household insurance | 5 / 5 | 1132400 | 1132400.00 | 1132400â€“1132400 | 1132400 | 2025-08-08, 2025-09-08, 2025-10-08 |
| event_175 | transport / Metro and bus fares | 13 / 6 | 1211967.944615384615384615385 | 1294200.86 | 995704.83â€“1440242.94 | 1211967.94 | 2025-08-12, 2025-08-26, 2025-09-09, 2025-09-23, 2025-10-07, 2025-10-21 |
| event_138 | utilities / Municipal utilities | 5 / 5 | 2035830.496 | 2081730.85 | 1830311.06â€“2143659.02 | 2035830.5 | 2025-08-07, 2025-09-07, 2025-10-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-08-07 | -2035830.5 | event_138 | utilities | recurring_expense | Municipal utilities |
| 2025-08-08 | -1132400 | event_139 | insurance | recurring_expense | Household insurance |
| 2025-08-08 | -1651100 | event_185 | shopping | explicit_event | Pending merchant debit |
| 2025-08-09 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-08-09 | -3040000 | event_140 | education | recurring_expense | Course tuition |
| 2025-08-11 | -1538993.97 | event_141 | healthcare | recurring_expense | Clinic payment |
| 2025-08-12 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-08-13 | -369550 | event_143 | cloud_storage | recurring_expense | Shared storage plan |
| 2025-08-15 | 42750000 | event_136 | salary | recurring_income | Payroll credit |
| 2025-08-15 | -1298171.69 | event_142 | entertainment | recurring_expense | Cinema and events |
| 2025-08-19 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-08-26 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-08-29 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-09-04 | -3534000 | event_144 | housing | recurring_expense | Home repair reserve |
| 2025-09-07 | -2035830.5 | event_138 | utilities | recurring_expense | Municipal utilities |
| 2025-09-08 | -1132400 | event_139 | insurance | recurring_expense | Household insurance |
| 2025-09-08 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-09-09 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-09-09 | -3040000 | event_140 | education | recurring_expense | Course tuition |
| 2025-09-11 | -1538993.97 | event_141 | healthcare | recurring_expense | Clinic payment |
| 2025-09-13 | -369550 | event_143 | cloud_storage | recurring_expense | Shared storage plan |
| 2025-09-15 | 42750000 | event_136 | salary | recurring_income | Payroll credit |
| 2025-09-15 | -1298171.69 | event_142 | entertainment | recurring_expense | Cinema and events |
| 2025-09-18 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-09-23 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-09-28 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-10-04 | -3534000 | event_144 | housing | recurring_expense | Home repair reserve |
| 2025-10-07 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-10-07 | -2035830.5 | event_138 | utilities | recurring_expense | Municipal utilities |
| 2025-10-08 | -1132400 | event_139 | insurance | recurring_expense | Household insurance |
| 2025-10-08 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-10-09 | -3040000 | event_140 | education | recurring_expense | Course tuition |
| 2025-10-11 | -1538993.97 | event_141 | healthcare | recurring_expense | Clinic payment |
| 2025-10-13 | -369550 | event_143 | cloud_storage | recurring_expense | Shared storage plan |
| 2025-10-15 | 42750000 | event_136 | salary | recurring_income | Payroll credit |
| 2025-10-15 | -1298171.69 | event_142 | entertainment | recurring_expense | Cinema and events |
| 2025-10-18 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |
| 2025-10-21 | -1211967.94 | event_175 | transport | recurring_expense | Metro and bus fares |
| 2025-10-28 | -1908881.3 | event_162 | groceries | recurring_expense | Supermarket basket |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-08-05 | 0 | 60383889.2 | 31225489.2 | 43154750 | 60383889.2 | 0 | (empty) |
| 1 | 2025-08-06 | 0 | 60383889.2 | 31225489.2 | 43154750 | 60383889.2 | 0 | (empty) |
| 2 | 2025-08-07 | -2035830.5 | 58348058.7 | 29189658.7 | 41118919.5 | 58348058.7 | 0 | event_138 |
| 3 | 2025-08-08 | -2783500 | 55564558.7 | 26406158.7 | 38335419.5 | 39611652.03 | 15952906.67 | event_139, event_185 |
| 4 | 2025-08-09 | -4948881.3 | 50615677.4 | 21457277.4 | 33386538.2 | 34662770.73 | 0 | event_162, event_140 |
| 5 | 2025-08-10 | 0 | 50615677.4 | 21457277.4 | 33386538.2 | 34662770.73 | 0 | (empty) |
| 6 | 2025-08-11 | -1538993.97 | 49076683.43 | 19918283.43 | 31847544.23 | 33123776.76 | 0 | event_141 |
| 7 | 2025-08-12 | -1211967.94 | 47864715.49 | 18706315.49 | 30635576.29 | 31911808.82 | 0 | event_175 |
| 8 | 2025-08-13 | -369550 | 47495165.49 | 18336765.49 | 30266026.29 | 31542258.82 | 0 | event_143 |
| 9 | 2025-08-14 | 0 | 47495165.49 | 18336765.49 | 30266026.29 | 31542258.82 | 0 | (empty) |
| 10 | 2025-08-15 | 41451828.31 | 88946993.8 | 59788593.8 | 71717854.6 | 72994087.13 | 0 | event_136, event_142 |
| 11 | 2025-08-16 | 0 | 88946993.8 | 59788593.8 | 71717854.6 | 72994087.13 | 0 | (empty) |
| 12 | 2025-08-17 | 0 | 88946993.8 | 59788593.8 | 71717854.6 | 72994087.13 | 0 | (empty) |
| 13 | 2025-08-18 | 0 | 88946993.8 | 59788593.8 | 71717854.6 | 72994087.13 | 0 | (empty) |
| 14 | 2025-08-19 | -1908881.3 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | event_162 |
| 15 | 2025-08-20 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 16 | 2025-08-21 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 17 | 2025-08-22 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 18 | 2025-08-23 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 19 | 2025-08-24 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 20 | 2025-08-25 | 0 | 87038112.5 | 57879712.5 | 69808973.3 | 71085205.83 | 0 | (empty) |
| 21 | 2025-08-26 | -1211967.94 | 85826144.56 | 56667744.56 | 68597005.36 | 69873237.89 | 0 | event_175 |
| 22 | 2025-08-27 | 0 | 85826144.56 | 56667744.56 | 68597005.36 | 69873237.89 | 0 | (empty) |
| 23 | 2025-08-28 | 0 | 85826144.56 | 56667744.56 | 68597005.36 | 69873237.89 | 0 | (empty) |
| 24 | 2025-08-29 | -1908881.3 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | event_162 |
| 25 | 2025-08-30 | 0 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | (empty) |
| 26 | 2025-08-31 | 0 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | (empty) |
| 27 | 2025-09-01 | 0 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | (empty) |
| 28 | 2025-09-02 | 0 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | (empty) |
| 29 | 2025-09-03 | 0 | 83917263.26 | 54758863.26 | 66688124.06 | 67964356.59 | 0 | (empty) |
| 30 | 2025-09-04 | -3534000 | 80383263.26 | 51224863.26 | 63154124.06 | 64430356.59 | 0 | event_144 |
| 31 | 2025-09-05 | 0 | 80383263.26 | 51224863.26 | 63154124.06 | 64430356.59 | 0 | (empty) |
| 32 | 2025-09-06 | 0 | 80383263.26 | 51224863.26 | 63154124.06 | 64430356.59 | 0 | (empty) |
| 33 | 2025-09-07 | -2035830.5 | 78347432.76 | 49189032.76 | 61118293.56 | 46441619.42 | 15952906.67 | event_138 |
| 34 | 2025-09-08 | -3041281.3 | 75306151.46 | 46147751.46 | 58077012.26 | 43400338.12 | 0 | event_139, event_162 |
| 35 | 2025-09-09 | -4251967.94 | 71054183.52 | 41895783.52 | 53825044.32 | 39148370.18 | 0 | event_175, event_140 |
| 36 | 2025-09-10 | 0 | 71054183.52 | 41895783.52 | 53825044.32 | 39148370.18 | 0 | (empty) |
| 37 | 2025-09-11 | -1538993.97 | 69515189.55 | 40356789.55 | 52286050.35 | 37609376.21 | 0 | event_141 |
| 38 | 2025-09-12 | 0 | 69515189.55 | 40356789.55 | 52286050.35 | 37609376.21 | 0 | (empty) |
| 39 | 2025-09-13 | -369550 | 69145639.55 | 39987239.55 | 51916500.35 | 37239826.21 | 0 | event_143 |
| 40 | 2025-09-14 | 0 | 69145639.55 | 39987239.55 | 51916500.35 | 37239826.21 | 0 | (empty) |
| 41 | 2025-09-15 | 41451828.31 | 110597467.86 | 81439067.86 | 93368328.66 | 78691654.52 | 0 | event_136, event_142 |
| 42 | 2025-09-16 | 0 | 110597467.86 | 81439067.86 | 93368328.66 | 78691654.52 | 0 | (empty) |
| 43 | 2025-09-17 | 0 | 110597467.86 | 81439067.86 | 93368328.66 | 78691654.52 | 0 | (empty) |
| 44 | 2025-09-18 | -1908881.3 | 108688586.56 | 79530186.56 | 91459447.36 | 76782773.22 | 0 | event_162 |
| 45 | 2025-09-19 | 0 | 108688586.56 | 79530186.56 | 91459447.36 | 76782773.22 | 0 | (empty) |
| 46 | 2025-09-20 | 0 | 108688586.56 | 79530186.56 | 91459447.36 | 76782773.22 | 0 | (empty) |
| 47 | 2025-09-21 | 0 | 108688586.56 | 79530186.56 | 91459447.36 | 76782773.22 | 0 | (empty) |
| 48 | 2025-09-22 | 0 | 108688586.56 | 79530186.56 | 91459447.36 | 76782773.22 | 0 | (empty) |
| 49 | 2025-09-23 | -1211967.94 | 107476618.62 | 78318218.62 | 90247479.42 | 75570805.28 | 0 | event_175 |
| 50 | 2025-09-24 | 0 | 107476618.62 | 78318218.62 | 90247479.42 | 75570805.28 | 0 | (empty) |
| 51 | 2025-09-25 | 0 | 107476618.62 | 78318218.62 | 90247479.42 | 75570805.28 | 0 | (empty) |
| 52 | 2025-09-26 | 0 | 107476618.62 | 78318218.62 | 90247479.42 | 75570805.28 | 0 | (empty) |
| 53 | 2025-09-27 | 0 | 107476618.62 | 78318218.62 | 90247479.42 | 75570805.28 | 0 | (empty) |
| 54 | 2025-09-28 | -1908881.3 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | event_162 |
| 55 | 2025-09-29 | 0 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | (empty) |
| 56 | 2025-09-30 | 0 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | (empty) |
| 57 | 2025-10-01 | 0 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | (empty) |
| 58 | 2025-10-02 | 0 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | (empty) |
| 59 | 2025-10-03 | 0 | 105567737.32 | 76409337.32 | 88338598.12 | 73661923.98 | 0 | (empty) |
| 60 | 2025-10-04 | -3534000 | 102033737.32 | 72875337.32 | 84804598.12 | 70127923.98 | 0 | event_144 |
| 61 | 2025-10-05 | 0 | 102033737.32 | 72875337.32 | 84804598.12 | 70127923.98 | 0 | (empty) |
| 62 | 2025-10-06 | 0 | 102033737.32 | 72875337.32 | 84804598.12 | 70127923.98 | 0 | (empty) |
| 63 | 2025-10-07 | -3247798.44 | 98785938.88 | 69627538.88 | 81556799.68 | 50927218.87 | 15952906.67 | event_175, event_138 |
| 64 | 2025-10-08 | -3041281.3 | 95744657.58 | 66586257.58 | 78515518.38 | 47885937.57 | 0 | event_139, event_162 |
| 65 | 2025-10-09 | -3040000 | 92704657.58 | 63546257.58 | 75475518.38 | 44845937.57 | 0 | event_140 |
| 66 | 2025-10-10 | 0 | 92704657.58 | 63546257.58 | 75475518.38 | 44845937.57 | 0 | (empty) |
| 67 | 2025-10-11 | -1538993.97 | 91165663.61 | 62007263.61 | 73936524.41 | 43306943.6 | 0 | event_141 |
| 68 | 2025-10-12 | 0 | 91165663.61 | 62007263.61 | 73936524.41 | 43306943.6 | 0 | (empty) |
| 69 | 2025-10-13 | -369550 | 90796113.61 | 61637713.61 | 73566974.41 | 42937393.6 | 0 | event_143 |
| 70 | 2025-10-14 | 0 | 90796113.61 | 61637713.61 | 73566974.41 | 42937393.6 | 0 | (empty) |
| 71 | 2025-10-15 | 41451828.31 | 132247941.92 | 103089541.92 | 115018802.72 | 84389221.91 | 0 | event_136, event_142 |
| 72 | 2025-10-16 | 0 | 132247941.92 | 103089541.92 | 115018802.72 | 84389221.91 | 0 | (empty) |
| 73 | 2025-10-17 | 0 | 132247941.92 | 103089541.92 | 115018802.72 | 84389221.91 | 0 | (empty) |
| 74 | 2025-10-18 | -1908881.3 | 130339060.62 | 101180660.62 | 113109921.42 | 82480340.61 | 0 | event_162 |
| 75 | 2025-10-19 | 0 | 130339060.62 | 101180660.62 | 113109921.42 | 82480340.61 | 0 | (empty) |
| 76 | 2025-10-20 | 0 | 130339060.62 | 101180660.62 | 113109921.42 | 82480340.61 | 0 | (empty) |
| 77 | 2025-10-21 | -1211967.94 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | event_175 |
| 78 | 2025-10-22 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 79 | 2025-10-23 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 80 | 2025-10-24 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 81 | 2025-10-25 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 82 | 2025-10-26 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 83 | 2025-10-27 | 0 | 129127092.68 | 99968692.68 | 111897953.48 | 81268372.67 | 0 | (empty) |
| 84 | 2025-10-28 | -1908881.3 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | event_162 |
| 85 | 2025-10-29 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |
| 86 | 2025-10-30 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |
| 87 | 2025-10-31 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |
| 88 | 2025-11-01 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |
| 89 | 2025-11-02 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |
| 90 | 2025-11-03 | 0 | 127218211.38 | 98059811.38 | 109989072.18 | 79359491.37 | 0 | (empty) |

## request_03 â€” user_03 (IDR)

Request: 5491000 on 2019-09-03; deadline 2019-11-15. Opening 5810300; minimum 2668700.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 873000 | 1121649.65 | NO |
| affordability_status | affordable_later | affordable_later | yes |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2019-11-15:5491000 | 2019-11-15:5491000 | yes |
| earliest_date_for_full_payment | 2019-11-15 | 2019-11-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 11 (2019-09-14), balance 3790349.65, headroom 1121649.65.

Protected: rent|utilities|groceries. Reduce: streaming|shopping. Stop: streaming|cloud_storage.

Salary mode: historical. Evidence: none. Unparsed messages: message_02.

- message_02 (employer, 2019-08-31T09:30:00Z): Tim payroll BrightPath Media telah mengirim pembaruan. Gaji rutin untuk penggajian berikutnya sudah dikonfirmasi. Slip gaji berikutnya akan menampilkan gaji rutin dan penyesuaian satu kali secara terpisah. Ref payroll EMP-0002.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_214 | cloud_storage / Shared storage plan | 5 / 5 | 20900 | 20900.00 | 20900â€“20900 | 20900 | 2019-09-14, 2019-10-14, 2019-11-14 |
| event_234 | groceries / Neighbourhood grocer | 18 / 6 | 193164.7855555555555555555556 | 184466.855 | 145691.38â€“240706.45 | 193164.79 | 2019-09-08, 2019-09-18, 2019-09-28, 2019-10-08, 2019-10-18, 2019-10-28, 2019-11-07, 2019-11-17, 2019-11-27 |
| event_212 | rent / Landlord standing order | 5 / 5 | 1140000 | 1140000.00 | 1140000â€“1140000 | 1140000 | 2019-09-04, 2019-10-04, 2019-11-04 |
| event_216 | shopping / Clothing and household items | 5 / 5 | 168697.75 | 173930.81 | 151493.37â€“184274.02 | 168697.75 | 2019-09-14, 2019-10-14, 2019-11-14 |
| event_215 | streaming / Video streaming plan | 5 / 5 | 117800 | 117800.00 | 117800â€“117800 | 117800 | 2019-09-11, 2019-10-11, 2019-11-11 |
| event_243 | transport / Rail pass | 9 / 6 | 91041.06444444444444444444444 | 83523.33 | 71790.29â€“116319.21 | 91041.06 | 2019-09-18, 2019-10-09, 2019-10-30, 2019-11-20 |
| event_213 | utilities / Water and power payment | 5 / 5 | 284387.814 | 290684.15 | 262344.55â€“303042.45 | 284387.81 | 2019-09-08, 2019-10-08, 2019-11-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2019-09-04 | -1140000 | event_212 | rent | recurring_expense | Landlord standing order |
| 2019-09-07 | -95000 | event_254 | healthcare | explicit_event | Pending pharmacy card charge |
| 2019-09-08 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-09-08 | -284387.81 | event_213 | utilities | recurring_expense | Water and power payment |
| 2019-09-11 | -117800 | event_215 | streaming | recurring_expense | Video streaming plan |
| 2019-09-14 | -20900 | event_214 | cloud_storage | recurring_expense | Shared storage plan |
| 2019-09-14 | -168697.75 | event_216 | shopping | recurring_expense | Clothing and household items |
| 2019-09-15 | 4365000 | event_210 | salary | recurring_income | Payroll credit |
| 2019-09-18 | -91041.06 | event_243 | transport | recurring_expense | Rail pass |
| 2019-09-18 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-09-28 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-10-04 | -1140000 | event_212 | rent | recurring_expense | Landlord standing order |
| 2019-10-08 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-10-08 | -284387.81 | event_213 | utilities | recurring_expense | Water and power payment |
| 2019-10-09 | -91041.06 | event_243 | transport | recurring_expense | Rail pass |
| 2019-10-11 | -117800 | event_215 | streaming | recurring_expense | Video streaming plan |
| 2019-10-14 | -20900 | event_214 | cloud_storage | recurring_expense | Shared storage plan |
| 2019-10-14 | -168697.75 | event_216 | shopping | recurring_expense | Clothing and household items |
| 2019-10-15 | 4365000 | event_210 | salary | recurring_income | Payroll credit |
| 2019-10-18 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-10-28 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-10-30 | -91041.06 | event_243 | transport | recurring_expense | Rail pass |
| 2019-11-04 | -1140000 | event_212 | rent | recurring_expense | Landlord standing order |
| 2019-11-07 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-11-08 | -284387.81 | event_213 | utilities | recurring_expense | Water and power payment |
| 2019-11-11 | -117800 | event_215 | streaming | recurring_expense | Video streaming plan |
| 2019-11-14 | -20900 | event_214 | cloud_storage | recurring_expense | Shared storage plan |
| 2019-11-14 | -168697.75 | event_216 | shopping | recurring_expense | Clothing and household items |
| 2019-11-15 | 4365000 | event_210 | salary | recurring_income | Payroll credit |
| 2019-11-17 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |
| 2019-11-20 | -91041.06 | event_243 | transport | recurring_expense | Rail pass |
| 2019-11-27 | -193164.79 | event_234 | groceries | recurring_expense | Neighbourhood grocer |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2019-09-03 | 0 | 5810300 | 3141600 | 4937300 | 5810300 | 0 | (empty) |
| 1 | 2019-09-04 | -1140000 | 4670300 | 2001600 | 3797300 | 4670300 | 0 | event_212 |
| 2 | 2019-09-05 | 0 | 4670300 | 2001600 | 3797300 | 4670300 | 0 | (empty) |
| 3 | 2019-09-06 | 0 | 4670300 | 2001600 | 3797300 | 4670300 | 0 | (empty) |
| 4 | 2019-09-07 | -95000 | 4575300 | 1906600 | 3702300 | 4575300 | 0 | event_254 |
| 5 | 2019-09-08 | -477552.6 | 4097747.4 | 1429047.4 | 3224747.4 | 4097747.4 | 0 | event_234, event_213 |
| 6 | 2019-09-09 | 0 | 4097747.4 | 1429047.4 | 3224747.4 | 4097747.4 | 0 | (empty) |
| 7 | 2019-09-10 | 0 | 4097747.4 | 1429047.4 | 3224747.4 | 4097747.4 | 0 | (empty) |
| 8 | 2019-09-11 | -117800 | 3979947.4 | 1311247.4 | 3106947.4 | 3979947.4 | 0 | event_215 |
| 9 | 2019-09-12 | 0 | 3979947.4 | 1311247.4 | 3106947.4 | 3979947.4 | 0 | (empty) |
| 10 | 2019-09-13 | 0 | 3979947.4 | 1311247.4 | 3106947.4 | 3979947.4 | 0 | (empty) |
| 11 | 2019-09-14 | -189597.75 | 3790349.65 | 1121649.65 | 2917349.65 | 3790349.65 | 0 | event_214, event_216 |
| 12 | 2019-09-15 | 4365000 | 8155349.65 | 5486649.65 | 7282349.65 | 8155349.65 | 0 | event_210 |
| 13 | 2019-09-16 | 0 | 8155349.65 | 5486649.65 | 7282349.65 | 8155349.65 | 0 | (empty) |
| 14 | 2019-09-17 | 0 | 8155349.65 | 5486649.65 | 7282349.65 | 8155349.65 | 0 | (empty) |
| 15 | 2019-09-18 | -284205.85 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | event_243, event_234 |
| 16 | 2019-09-19 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 17 | 2019-09-20 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 18 | 2019-09-21 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 19 | 2019-09-22 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 20 | 2019-09-23 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 21 | 2019-09-24 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 22 | 2019-09-25 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 23 | 2019-09-26 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 24 | 2019-09-27 | 0 | 7871143.8 | 5202443.8 | 6998143.8 | 7871143.8 | 0 | (empty) |
| 25 | 2019-09-28 | -193164.79 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | event_234 |
| 26 | 2019-09-29 | 0 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | (empty) |
| 27 | 2019-09-30 | 0 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | (empty) |
| 28 | 2019-10-01 | 0 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | (empty) |
| 29 | 2019-10-02 | 0 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | (empty) |
| 30 | 2019-10-03 | 0 | 7677979.01 | 5009279.01 | 6804979.01 | 7677979.01 | 0 | (empty) |
| 31 | 2019-10-04 | -1140000 | 6537979.01 | 3869279.01 | 5664979.01 | 6537979.01 | 0 | event_212 |
| 32 | 2019-10-05 | 0 | 6537979.01 | 3869279.01 | 5664979.01 | 6537979.01 | 0 | (empty) |
| 33 | 2019-10-06 | 0 | 6537979.01 | 3869279.01 | 5664979.01 | 6537979.01 | 0 | (empty) |
| 34 | 2019-10-07 | 0 | 6537979.01 | 3869279.01 | 5664979.01 | 6537979.01 | 0 | (empty) |
| 35 | 2019-10-08 | -477552.6 | 6060426.41 | 3391726.41 | 5187426.41 | 6060426.41 | 0 | event_234, event_213 |
| 36 | 2019-10-09 | -91041.06 | 5969385.35 | 3300685.35 | 5096385.35 | 5969385.35 | 0 | event_243 |
| 37 | 2019-10-10 | 0 | 5969385.35 | 3300685.35 | 5096385.35 | 5969385.35 | 0 | (empty) |
| 38 | 2019-10-11 | -117800 | 5851585.35 | 3182885.35 | 4978585.35 | 5851585.35 | 0 | event_215 |
| 39 | 2019-10-12 | 0 | 5851585.35 | 3182885.35 | 4978585.35 | 5851585.35 | 0 | (empty) |
| 40 | 2019-10-13 | 0 | 5851585.35 | 3182885.35 | 4978585.35 | 5851585.35 | 0 | (empty) |
| 41 | 2019-10-14 | -189597.75 | 5661987.6 | 2993287.6 | 4788987.6 | 5661987.6 | 0 | event_214, event_216 |
| 42 | 2019-10-15 | 4365000 | 10026987.6 | 7358287.6 | 9153987.6 | 10026987.6 | 0 | event_210 |
| 43 | 2019-10-16 | 0 | 10026987.6 | 7358287.6 | 9153987.6 | 10026987.6 | 0 | (empty) |
| 44 | 2019-10-17 | 0 | 10026987.6 | 7358287.6 | 9153987.6 | 10026987.6 | 0 | (empty) |
| 45 | 2019-10-18 | -193164.79 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | event_234 |
| 46 | 2019-10-19 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 47 | 2019-10-20 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 48 | 2019-10-21 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 49 | 2019-10-22 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 50 | 2019-10-23 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 51 | 2019-10-24 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 52 | 2019-10-25 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 53 | 2019-10-26 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 54 | 2019-10-27 | 0 | 9833822.81 | 7165122.81 | 8960822.81 | 9833822.81 | 0 | (empty) |
| 55 | 2019-10-28 | -193164.79 | 9640658.02 | 6971958.02 | 8767658.02 | 9640658.02 | 0 | event_234 |
| 56 | 2019-10-29 | 0 | 9640658.02 | 6971958.02 | 8767658.02 | 9640658.02 | 0 | (empty) |
| 57 | 2019-10-30 | -91041.06 | 9549616.96 | 6880916.96 | 8676616.96 | 9549616.96 | 0 | event_243 |
| 58 | 2019-10-31 | 0 | 9549616.96 | 6880916.96 | 8676616.96 | 9549616.96 | 0 | (empty) |
| 59 | 2019-11-01 | 0 | 9549616.96 | 6880916.96 | 8676616.96 | 9549616.96 | 0 | (empty) |
| 60 | 2019-11-02 | 0 | 9549616.96 | 6880916.96 | 8676616.96 | 9549616.96 | 0 | (empty) |
| 61 | 2019-11-03 | 0 | 9549616.96 | 6880916.96 | 8676616.96 | 9549616.96 | 0 | (empty) |
| 62 | 2019-11-04 | -1140000 | 8409616.96 | 5740916.96 | 7536616.96 | 8409616.96 | 0 | event_212 |
| 63 | 2019-11-05 | 0 | 8409616.96 | 5740916.96 | 7536616.96 | 8409616.96 | 0 | (empty) |
| 64 | 2019-11-06 | 0 | 8409616.96 | 5740916.96 | 7536616.96 | 8409616.96 | 0 | (empty) |
| 65 | 2019-11-07 | -193164.79 | 8216452.17 | 5547752.17 | 7343452.17 | 8216452.17 | 0 | event_234 |
| 66 | 2019-11-08 | -284387.81 | 7932064.36 | 5263364.36 | 7059064.36 | 7932064.36 | 0 | event_213 |
| 67 | 2019-11-09 | 0 | 7932064.36 | 5263364.36 | 7059064.36 | 7932064.36 | 0 | (empty) |
| 68 | 2019-11-10 | 0 | 7932064.36 | 5263364.36 | 7059064.36 | 7932064.36 | 0 | (empty) |
| 69 | 2019-11-11 | -117800 | 7814264.36 | 5145564.36 | 6941264.36 | 7814264.36 | 0 | event_215 |
| 70 | 2019-11-12 | 0 | 7814264.36 | 5145564.36 | 6941264.36 | 7814264.36 | 0 | (empty) |
| 71 | 2019-11-13 | 0 | 7814264.36 | 5145564.36 | 6941264.36 | 7814264.36 | 0 | (empty) |
| 72 | 2019-11-14 | -189597.75 | 7624666.61 | 4955966.61 | 6751666.61 | 7624666.61 | 0 | event_214, event_216 |
| 73 | 2019-11-15 | 4365000 | 11989666.61 | 9320966.61 | 11116666.61 | 6498666.61 | 5491000 | event_210 |
| 74 | 2019-11-16 | 0 | 11989666.61 | 9320966.61 | 11116666.61 | 6498666.61 | 0 | (empty) |
| 75 | 2019-11-17 | -193164.79 | 11796501.82 | 9127801.82 | 10923501.82 | 6305501.82 | 0 | event_234 |
| 76 | 2019-11-18 | 0 | 11796501.82 | 9127801.82 | 10923501.82 | 6305501.82 | 0 | (empty) |
| 77 | 2019-11-19 | 0 | 11796501.82 | 9127801.82 | 10923501.82 | 6305501.82 | 0 | (empty) |
| 78 | 2019-11-20 | -91041.06 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | event_243 |
| 79 | 2019-11-21 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 80 | 2019-11-22 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 81 | 2019-11-23 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 82 | 2019-11-24 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 83 | 2019-11-25 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 84 | 2019-11-26 | 0 | 11705460.76 | 9036760.76 | 10832460.76 | 6214460.76 | 0 | (empty) |
| 85 | 2019-11-27 | -193164.79 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | event_234 |
| 86 | 2019-11-28 | 0 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | (empty) |
| 87 | 2019-11-29 | 0 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | (empty) |
| 88 | 2019-11-30 | 0 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | (empty) |
| 89 | 2019-12-01 | 0 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | (empty) |
| 90 | 2019-12-02 | 0 | 11512295.97 | 8843595.97 | 10639295.97 | 6021295.97 | 0 | (empty) |

## request_04 â€” user_04 (IDR)

Request: 12693000 on 2024-06-04; deadline 2024-06-19. Opening 52206950; minimum 30686600.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 8401800 | 12357921.14 | NO |
| affordability_status | affordable_later | affordable_later | yes |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2024-06-15:12693000 | 2024-06-15:12693000 | yes |
| earliest_date_for_full_payment | 2024-06-15 | 2024-06-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 9 (2024-06-13), balance 43044521.14, headroom 12357921.14.

Protected: rent|groceries|transport. Reduce: entertainment. Stop: music_subscription.

Salary mode: historical. Evidence: none. Unparsed messages: message_03.

- message_03 (employer, 2024-06-01T09:30:00Z): Rincian penggajian Anda di Greenfield Foods telah berubah. Bonus kuartalan Anda masih menunggu hasil akhir penilaian kinerja. Jumlah akhir dan tanggal pembayaran belum disetujui. Kami akan mengirim pembaruan setelah tim payroll mengonfirmasi jumlah dan tanggalnya. Ref payroll EMP-0003.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_288 | delivery_membership / Food delivery membership | 5 / 5 | 377150 | 377150.00 | 377150â€“377150 | 377150 | 2024-06-12, 2024-07-12, 2024-08-12 |
| event_290 | entertainment / Local event tickets | 5 / 5 | 1385201.354 | 1375854.05 | 1231859.39â€“1542620 | 1385201.35 | 2024-06-13, 2024-07-13, 2024-08-13 |
| event_317 | groceries / Bulk pantry shop | 26 / 7 | 1499474.475384615384615384615 | 1468304.315 | 1075064.04â€“1831437.58 | 1499474.48 | 2024-06-08, 2024-06-15, 2024-06-22, 2024-06-29, 2024-07-06, 2024-07-13, 2024-07-20, 2024-07-27, 2024-08-03, 2024-08-10, 2024-08-17, 2024-08-24, 2024-08-31 |
| event_289 | gym / Gym membership | 5 / 5 | 1027900 | 1027900.00 | 1027900â€“1027900 | 1027900 | 2024-06-09, 2024-07-09, 2024-08-09 |
| event_287 | music_subscription / Music service subscription | 5 / 5 | 332500 | 332500.00 | 332500â€“332500 | 332500 | 2024-06-10, 2024-07-10, 2024-08-10 |
| event_291 | rent / Residential rent payment | 6 / 6 | 12293000 | 12293000.00 | 12293000â€“12293000 | 12293000 | 2024-07-01, 2024-08-01, 2024-09-01 |
| event_343 | transport / Rail pass | 26 / 7 | 832507.4142307692307692307692 | 848248.97 | 589707.32â€“1030376.9 | 832507.41 | 2024-06-09, 2024-06-16, 2024-06-23, 2024-06-30, 2024-07-07, 2024-07-14, 2024-07-21, 2024-07-28, 2024-08-04, 2024-08-11, 2024-08-18, 2024-08-25, 2024-09-01 |
| event_286 | utilities / Municipal utilities | 5 / 5 | 2003395.618 | 2004118.60 | 1980834.82â€“2033868.83 | 2003395.62 | 2024-06-05, 2024-07-05, 2024-08-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-06-05 | -2003395.62 | event_286 | utilities | recurring_expense | Municipal utilities |
| 2024-06-08 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-06-09 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-06-09 | -1027900 | event_289 | gym | recurring_expense | Gym membership |
| 2024-06-10 | -332500 | event_287 | music_subscription | recurring_expense | Music service subscription |
| 2024-06-11 | -1704300 | event_357 | education | explicit_event | Scheduled school fee |
| 2024-06-12 | -377150 | event_288 | delivery_membership | recurring_expense | Food delivery membership |
| 2024-06-13 | -1385201.35 | event_290 | entertainment | recurring_expense | Local event tickets |
| 2024-06-15 | 38190000 | event_284 | salary | recurring_income | Payroll credit |
| 2024-06-15 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-06-16 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-06-22 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-06-23 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-06-29 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-06-30 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-07-01 | -12293000 | event_291 | rent | recurring_expense | Residential rent payment |
| 2024-07-05 | -2003395.62 | event_286 | utilities | recurring_expense | Municipal utilities |
| 2024-07-06 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-07-07 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-07-09 | -1027900 | event_289 | gym | recurring_expense | Gym membership |
| 2024-07-10 | -332500 | event_287 | music_subscription | recurring_expense | Music service subscription |
| 2024-07-12 | -377150 | event_288 | delivery_membership | recurring_expense | Food delivery membership |
| 2024-07-13 | -1385201.35 | event_290 | entertainment | recurring_expense | Local event tickets |
| 2024-07-13 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-07-14 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-07-15 | 38190000 | event_284 | salary | recurring_income | Payroll credit |
| 2024-07-20 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-07-21 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-07-27 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-07-28 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-08-01 | -12293000 | event_291 | rent | recurring_expense | Residential rent payment |
| 2024-08-03 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-08-04 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-08-05 | -2003395.62 | event_286 | utilities | recurring_expense | Municipal utilities |
| 2024-08-09 | -1027900 | event_289 | gym | recurring_expense | Gym membership |
| 2024-08-10 | -332500 | event_287 | music_subscription | recurring_expense | Music service subscription |
| 2024-08-10 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-08-11 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-08-12 | -377150 | event_288 | delivery_membership | recurring_expense | Food delivery membership |
| 2024-08-13 | -1385201.35 | event_290 | entertainment | recurring_expense | Local event tickets |
| 2024-08-15 | 38190000 | event_284 | salary | recurring_income | Payroll credit |
| 2024-08-17 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-08-18 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-08-24 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-08-25 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-08-31 | -1499474.48 | event_317 | groceries | recurring_expense | Bulk pantry shop |
| 2024-09-01 | -832507.41 | event_343 | transport | recurring_expense | Rail pass |
| 2024-09-01 | -12293000 | event_291 | rent | recurring_expense | Residential rent payment |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-06-04 | 0 | 52206950 | 21520350 | 43805150 | 52206950 | 0 | (empty) |
| 1 | 2024-06-05 | -2003395.62 | 50203554.38 | 19516954.38 | 41801754.38 | 50203554.38 | 0 | event_286 |
| 2 | 2024-06-06 | 0 | 50203554.38 | 19516954.38 | 41801754.38 | 50203554.38 | 0 | (empty) |
| 3 | 2024-06-07 | 0 | 50203554.38 | 19516954.38 | 41801754.38 | 50203554.38 | 0 | (empty) |
| 4 | 2024-06-08 | -1499474.48 | 48704079.9 | 18017479.9 | 40302279.9 | 48704079.9 | 0 | event_317 |
| 5 | 2024-06-09 | -1860407.41 | 46843672.49 | 16157072.49 | 38441872.49 | 46843672.49 | 0 | event_343, event_289 |
| 6 | 2024-06-10 | -332500 | 46511172.49 | 15824572.49 | 38109372.49 | 46511172.49 | 0 | event_287 |
| 7 | 2024-06-11 | -1704300 | 44806872.49 | 14120272.49 | 36405072.49 | 44806872.49 | 0 | event_357 |
| 8 | 2024-06-12 | -377150 | 44429722.49 | 13743122.49 | 36027922.49 | 44429722.49 | 0 | event_288 |
| 9 | 2024-06-13 | -1385201.35 | 43044521.14 | 12357921.14 | 34642721.14 | 43044521.14 | 0 | event_290 |
| 10 | 2024-06-14 | 0 | 43044521.14 | 12357921.14 | 34642721.14 | 43044521.14 | 0 | (empty) |
| 11 | 2024-06-15 | 36690525.52 | 79735046.66 | 49048446.66 | 71333246.66 | 67042046.66 | 12693000 | event_284, event_317 |
| 12 | 2024-06-16 | -832507.41 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | event_343 |
| 13 | 2024-06-17 | 0 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | (empty) |
| 14 | 2024-06-18 | 0 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | (empty) |
| 15 | 2024-06-19 | 0 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | (empty) |
| 16 | 2024-06-20 | 0 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | (empty) |
| 17 | 2024-06-21 | 0 | 78902539.25 | 48215939.25 | 70500739.25 | 66209539.25 | 0 | (empty) |
| 18 | 2024-06-22 | -1499474.48 | 77403064.77 | 46716464.77 | 69001264.77 | 64710064.77 | 0 | event_317 |
| 19 | 2024-06-23 | -832507.41 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | event_343 |
| 20 | 2024-06-24 | 0 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | (empty) |
| 21 | 2024-06-25 | 0 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | (empty) |
| 22 | 2024-06-26 | 0 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | (empty) |
| 23 | 2024-06-27 | 0 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | (empty) |
| 24 | 2024-06-28 | 0 | 76570557.36 | 45883957.36 | 68168757.36 | 63877557.36 | 0 | (empty) |
| 25 | 2024-06-29 | -1499474.48 | 75071082.88 | 44384482.88 | 66669282.88 | 62378082.88 | 0 | event_317 |
| 26 | 2024-06-30 | -832507.41 | 74238575.47 | 43551975.47 | 65836775.47 | 61545575.47 | 0 | event_343 |
| 27 | 2024-07-01 | -12293000 | 61945575.47 | 31258975.47 | 53543775.47 | 49252575.47 | 0 | event_291 |
| 28 | 2024-07-02 | 0 | 61945575.47 | 31258975.47 | 53543775.47 | 49252575.47 | 0 | (empty) |
| 29 | 2024-07-03 | 0 | 61945575.47 | 31258975.47 | 53543775.47 | 49252575.47 | 0 | (empty) |
| 30 | 2024-07-04 | 0 | 61945575.47 | 31258975.47 | 53543775.47 | 49252575.47 | 0 | (empty) |
| 31 | 2024-07-05 | -2003395.62 | 59942179.85 | 29255579.85 | 51540379.85 | 47249179.85 | 0 | event_286 |
| 32 | 2024-07-06 | -1499474.48 | 58442705.37 | 27756105.37 | 50040905.37 | 45749705.37 | 0 | event_317 |
| 33 | 2024-07-07 | -832507.41 | 57610197.96 | 26923597.96 | 49208397.96 | 44917197.96 | 0 | event_343 |
| 34 | 2024-07-08 | 0 | 57610197.96 | 26923597.96 | 49208397.96 | 44917197.96 | 0 | (empty) |
| 35 | 2024-07-09 | -1027900 | 56582297.96 | 25895697.96 | 48180497.96 | 43889297.96 | 0 | event_289 |
| 36 | 2024-07-10 | -332500 | 56249797.96 | 25563197.96 | 47847997.96 | 43556797.96 | 0 | event_287 |
| 37 | 2024-07-11 | 0 | 56249797.96 | 25563197.96 | 47847997.96 | 43556797.96 | 0 | (empty) |
| 38 | 2024-07-12 | -377150 | 55872647.96 | 25186047.96 | 47470847.96 | 43179647.96 | 0 | event_288 |
| 39 | 2024-07-13 | -2884675.83 | 52987972.13 | 22301372.13 | 44586172.13 | 40294972.13 | 0 | event_290, event_317 |
| 40 | 2024-07-14 | -832507.41 | 52155464.72 | 21468864.72 | 43753664.72 | 39462464.72 | 0 | event_343 |
| 41 | 2024-07-15 | 38190000 | 90345464.72 | 59658864.72 | 81943664.72 | 77652464.72 | 0 | event_284 |
| 42 | 2024-07-16 | 0 | 90345464.72 | 59658864.72 | 81943664.72 | 77652464.72 | 0 | (empty) |
| 43 | 2024-07-17 | 0 | 90345464.72 | 59658864.72 | 81943664.72 | 77652464.72 | 0 | (empty) |
| 44 | 2024-07-18 | 0 | 90345464.72 | 59658864.72 | 81943664.72 | 77652464.72 | 0 | (empty) |
| 45 | 2024-07-19 | 0 | 90345464.72 | 59658864.72 | 81943664.72 | 77652464.72 | 0 | (empty) |
| 46 | 2024-07-20 | -1499474.48 | 88845990.24 | 58159390.24 | 80444190.24 | 76152990.24 | 0 | event_317 |
| 47 | 2024-07-21 | -832507.41 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | event_343 |
| 48 | 2024-07-22 | 0 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | (empty) |
| 49 | 2024-07-23 | 0 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | (empty) |
| 50 | 2024-07-24 | 0 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | (empty) |
| 51 | 2024-07-25 | 0 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | (empty) |
| 52 | 2024-07-26 | 0 | 88013482.83 | 57326882.83 | 79611682.83 | 75320482.83 | 0 | (empty) |
| 53 | 2024-07-27 | -1499474.48 | 86514008.35 | 55827408.35 | 78112208.35 | 73821008.35 | 0 | event_317 |
| 54 | 2024-07-28 | -832507.41 | 85681500.94 | 54994900.94 | 77279700.94 | 72988500.94 | 0 | event_343 |
| 55 | 2024-07-29 | 0 | 85681500.94 | 54994900.94 | 77279700.94 | 72988500.94 | 0 | (empty) |
| 56 | 2024-07-30 | 0 | 85681500.94 | 54994900.94 | 77279700.94 | 72988500.94 | 0 | (empty) |
| 57 | 2024-07-31 | 0 | 85681500.94 | 54994900.94 | 77279700.94 | 72988500.94 | 0 | (empty) |
| 58 | 2024-08-01 | -12293000 | 73388500.94 | 42701900.94 | 64986700.94 | 60695500.94 | 0 | event_291 |
| 59 | 2024-08-02 | 0 | 73388500.94 | 42701900.94 | 64986700.94 | 60695500.94 | 0 | (empty) |
| 60 | 2024-08-03 | -1499474.48 | 71889026.46 | 41202426.46 | 63487226.46 | 59196026.46 | 0 | event_317 |
| 61 | 2024-08-04 | -832507.41 | 71056519.05 | 40369919.05 | 62654719.05 | 58363519.05 | 0 | event_343 |
| 62 | 2024-08-05 | -2003395.62 | 69053123.43 | 38366523.43 | 60651323.43 | 56360123.43 | 0 | event_286 |
| 63 | 2024-08-06 | 0 | 69053123.43 | 38366523.43 | 60651323.43 | 56360123.43 | 0 | (empty) |
| 64 | 2024-08-07 | 0 | 69053123.43 | 38366523.43 | 60651323.43 | 56360123.43 | 0 | (empty) |
| 65 | 2024-08-08 | 0 | 69053123.43 | 38366523.43 | 60651323.43 | 56360123.43 | 0 | (empty) |
| 66 | 2024-08-09 | -1027900 | 68025223.43 | 37338623.43 | 59623423.43 | 55332223.43 | 0 | event_289 |
| 67 | 2024-08-10 | -1831974.48 | 66193248.95 | 35506648.95 | 57791448.95 | 53500248.95 | 0 | event_287, event_317 |
| 68 | 2024-08-11 | -832507.41 | 65360741.54 | 34674141.54 | 56958941.54 | 52667741.54 | 0 | event_343 |
| 69 | 2024-08-12 | -377150 | 64983591.54 | 34296991.54 | 56581791.54 | 52290591.54 | 0 | event_288 |
| 70 | 2024-08-13 | -1385201.35 | 63598390.19 | 32911790.19 | 55196590.19 | 50905390.19 | 0 | event_290 |
| 71 | 2024-08-14 | 0 | 63598390.19 | 32911790.19 | 55196590.19 | 50905390.19 | 0 | (empty) |
| 72 | 2024-08-15 | 38190000 | 101788390.19 | 71101790.19 | 93386590.19 | 89095390.19 | 0 | event_284 |
| 73 | 2024-08-16 | 0 | 101788390.19 | 71101790.19 | 93386590.19 | 89095390.19 | 0 | (empty) |
| 74 | 2024-08-17 | -1499474.48 | 100288915.71 | 69602315.71 | 91887115.71 | 87595915.71 | 0 | event_317 |
| 75 | 2024-08-18 | -832507.41 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | event_343 |
| 76 | 2024-08-19 | 0 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | (empty) |
| 77 | 2024-08-20 | 0 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | (empty) |
| 78 | 2024-08-21 | 0 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | (empty) |
| 79 | 2024-08-22 | 0 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | (empty) |
| 80 | 2024-08-23 | 0 | 99456408.3 | 68769808.3 | 91054608.3 | 86763408.3 | 0 | (empty) |
| 81 | 2024-08-24 | -1499474.48 | 97956933.82 | 67270333.82 | 89555133.82 | 85263933.82 | 0 | event_317 |
| 82 | 2024-08-25 | -832507.41 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | event_343 |
| 83 | 2024-08-26 | 0 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | (empty) |
| 84 | 2024-08-27 | 0 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | (empty) |
| 85 | 2024-08-28 | 0 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | (empty) |
| 86 | 2024-08-29 | 0 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | (empty) |
| 87 | 2024-08-30 | 0 | 97124426.41 | 66437826.41 | 88722626.41 | 84431426.41 | 0 | (empty) |
| 88 | 2024-08-31 | -1499474.48 | 95624951.93 | 64938351.93 | 87223151.93 | 82931951.93 | 0 | event_317 |
| 89 | 2024-09-01 | -13125507.41 | 82499444.52 | 51812844.52 | 74097644.52 | 69806444.52 | 0 | event_343, event_291 |
| 90 | 2024-09-02 | 0 | 82499444.52 | 51812844.52 | 74097644.52 | 69806444.52 | 0 | (empty) |

## request_05 â€” user_05 (ZAR)

Request: 15488 on 2025-11-06; deadline 2026-01-12. Opening 46475.1; minimum 13100.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 737 | 0 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 90 (2026-02-04), balance 8160.81, headroom -4939.19.

Protected: rent|healthcare|family_support|groceries. Reduce: shopping. Stop: cloud_storage.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_396 | cloud_storage / Cloud storage plan | 5 / 5 | 113.3 | 113.30 | 113.3â€“113.3 | 113.3 | 2025-11-12, 2025-12-12, 2026-01-12 |
| event_393 | debt_repayment / Vehicle loan payment | 5 / 5 | 968 | 968.00 | 968â€“968 | 968 | 2025-11-11, 2025-12-11, 2026-01-11 |
| event_395 | family_support / Dependent care payment | 5 / 5 | 840.4 | 840.40 | 840.4â€“840.4 | 840.4 | 2025-11-13, 2025-12-13, 2026-01-13 |
| event_424 | groceries / Fresh food shop | 26 / 7 | 721.7042307692307692307692308 | 741.58 | 515.4â€“853.42 | 721.7 | 2025-11-11, 2025-11-18, 2025-11-25, 2025-12-02, 2025-12-09, 2025-12-16, 2025-12-23, 2025-12-30, 2026-01-06, 2026-01-13, 2026-01-20, 2026-01-27, 2026-02-03 |
| event_394 | healthcare / Therapy appointment | 5 / 5 | 699.008 | 721.44 | 632.59â€“777.27 | 699.01 | 2025-11-10, 2025-12-10, 2026-01-10 |
| event_398 | rent / Apartment rent transfer | 6 / 6 | 4972 | 4972.00 | 4972â€“4972 | 4972 | 2025-12-02, 2026-01-02, 2026-02-02 |
| event_397 | shopping / Personal shopping | 5 / 5 | 397.85 | 404.24 | 362.09â€“422.67 | 397.85 | 2025-11-12, 2025-12-12, 2026-01-12 |
| event_437 | transport / Rail pass | 13 / 6 | 414.3438461538461538461538462 | 411.47 | 311â€“504.23 | 414.34 | 2025-11-12, 2025-11-26, 2025-12-10, 2025-12-24, 2026-01-07, 2026-01-21, 2026-02-04 |
| event_392 | utilities / Municipal utilities | 5 / 5 | 686.706 | 706.37 | 604.15â€“750.89 | 686.71 | 2025-11-06, 2025-12-06, 2026-01-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-11-06 | -686.71 | event_392 | utilities | recurring_expense | Municipal utilities |
| 2025-11-10 | -699.01 | event_394 | healthcare | recurring_expense | Therapy appointment |
| 2025-11-11 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-11-11 | -968 | event_393 | debt_repayment | recurring_expense | Vehicle loan payment |
| 2025-11-12 | -113.3 | event_396 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-11-12 | -397.85 | event_397 | shopping | recurring_expense | Personal shopping |
| 2025-11-12 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2025-11-13 | -840.4 | event_395 | family_support | recurring_expense | Dependent care payment |
| 2025-11-18 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-11-25 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-11-26 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2025-12-02 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-12-02 | -4972 | event_398 | rent | recurring_expense | Apartment rent transfer |
| 2025-12-06 | -686.71 | event_392 | utilities | recurring_expense | Municipal utilities |
| 2025-12-09 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-12-10 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2025-12-10 | -699.01 | event_394 | healthcare | recurring_expense | Therapy appointment |
| 2025-12-11 | -968 | event_393 | debt_repayment | recurring_expense | Vehicle loan payment |
| 2025-12-12 | -113.3 | event_396 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-12-12 | -397.85 | event_397 | shopping | recurring_expense | Personal shopping |
| 2025-12-13 | -840.4 | event_395 | family_support | recurring_expense | Dependent care payment |
| 2025-12-16 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-12-23 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2025-12-24 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2025-12-30 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-01-02 | -4972 | event_398 | rent | recurring_expense | Apartment rent transfer |
| 2026-01-06 | -686.71 | event_392 | utilities | recurring_expense | Municipal utilities |
| 2026-01-06 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-01-07 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2026-01-10 | -699.01 | event_394 | healthcare | recurring_expense | Therapy appointment |
| 2026-01-11 | -968 | event_393 | debt_repayment | recurring_expense | Vehicle loan payment |
| 2026-01-12 | -113.3 | event_396 | cloud_storage | recurring_expense | Cloud storage plan |
| 2026-01-12 | -397.85 | event_397 | shopping | recurring_expense | Personal shopping |
| 2026-01-13 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-01-13 | -840.4 | event_395 | family_support | recurring_expense | Dependent care payment |
| 2026-01-20 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-01-21 | -414.34 | event_437 | transport | recurring_expense | Rail pass |
| 2026-01-27 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-02-02 | -4972 | event_398 | rent | recurring_expense | Apartment rent transfer |
| 2026-02-03 | -721.7 | event_424 | groceries | recurring_expense | Fresh food shop |
| 2026-02-04 | -414.34 | event_437 | transport | recurring_expense | Rail pass |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-11-06 | -686.71 | 45788.39 | 32688.39 | 45051.39 | 45788.39 | 0 | event_392 |
| 1 | 2025-11-07 | 0 | 45788.39 | 32688.39 | 45051.39 | 45788.39 | 0 | (empty) |
| 2 | 2025-11-08 | 0 | 45788.39 | 32688.39 | 45051.39 | 45788.39 | 0 | (empty) |
| 3 | 2025-11-09 | 0 | 45788.39 | 32688.39 | 45051.39 | 45788.39 | 0 | (empty) |
| 4 | 2025-11-10 | -699.01 | 45089.38 | 31989.38 | 44352.38 | 45089.38 | 0 | event_394 |
| 5 | 2025-11-11 | -1689.7 | 43399.68 | 30299.68 | 42662.68 | 43399.68 | 0 | event_424, event_393 |
| 6 | 2025-11-12 | -925.49 | 42474.19 | 29374.19 | 41737.19 | 42474.19 | 0 | event_396, event_397, event_437 |
| 7 | 2025-11-13 | -840.4 | 41633.79 | 28533.79 | 40896.79 | 41633.79 | 0 | event_395 |
| 8 | 2025-11-14 | 0 | 41633.79 | 28533.79 | 40896.79 | 41633.79 | 0 | (empty) |
| 9 | 2025-11-15 | 0 | 41633.79 | 28533.79 | 40896.79 | 41633.79 | 0 | (empty) |
| 10 | 2025-11-16 | 0 | 41633.79 | 28533.79 | 40896.79 | 41633.79 | 0 | (empty) |
| 11 | 2025-11-17 | 0 | 41633.79 | 28533.79 | 40896.79 | 41633.79 | 0 | (empty) |
| 12 | 2025-11-18 | -721.7 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | event_424 |
| 13 | 2025-11-19 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 14 | 2025-11-20 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 15 | 2025-11-21 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 16 | 2025-11-22 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 17 | 2025-11-23 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 18 | 2025-11-24 | 0 | 40912.09 | 27812.09 | 40175.09 | 40912.09 | 0 | (empty) |
| 19 | 2025-11-25 | -721.7 | 40190.39 | 27090.39 | 39453.39 | 40190.39 | 0 | event_424 |
| 20 | 2025-11-26 | -414.34 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | event_437 |
| 21 | 2025-11-27 | 0 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | (empty) |
| 22 | 2025-11-28 | 0 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | (empty) |
| 23 | 2025-11-29 | 0 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | (empty) |
| 24 | 2025-11-30 | 0 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | (empty) |
| 25 | 2025-12-01 | 0 | 39776.05 | 26676.05 | 39039.05 | 39776.05 | 0 | (empty) |
| 26 | 2025-12-02 | -5693.7 | 34082.35 | 20982.35 | 33345.35 | 34082.35 | 0 | event_424, event_398 |
| 27 | 2025-12-03 | 0 | 34082.35 | 20982.35 | 33345.35 | 34082.35 | 0 | (empty) |
| 28 | 2025-12-04 | 0 | 34082.35 | 20982.35 | 33345.35 | 34082.35 | 0 | (empty) |
| 29 | 2025-12-05 | 0 | 34082.35 | 20982.35 | 33345.35 | 34082.35 | 0 | (empty) |
| 30 | 2025-12-06 | -686.71 | 33395.64 | 20295.64 | 32658.64 | 33395.64 | 0 | event_392 |
| 31 | 2025-12-07 | 0 | 33395.64 | 20295.64 | 32658.64 | 33395.64 | 0 | (empty) |
| 32 | 2025-12-08 | 0 | 33395.64 | 20295.64 | 32658.64 | 33395.64 | 0 | (empty) |
| 33 | 2025-12-09 | -721.7 | 32673.94 | 19573.94 | 31936.94 | 32673.94 | 0 | event_424 |
| 34 | 2025-12-10 | -1113.35 | 31560.59 | 18460.59 | 30823.59 | 31560.59 | 0 | event_437, event_394 |
| 35 | 2025-12-11 | -968 | 30592.59 | 17492.59 | 29855.59 | 30592.59 | 0 | event_393 |
| 36 | 2025-12-12 | -511.15 | 30081.44 | 16981.44 | 29344.44 | 30081.44 | 0 | event_396, event_397 |
| 37 | 2025-12-13 | -840.4 | 29241.04 | 16141.04 | 28504.04 | 29241.04 | 0 | event_395 |
| 38 | 2025-12-14 | 0 | 29241.04 | 16141.04 | 28504.04 | 29241.04 | 0 | (empty) |
| 39 | 2025-12-15 | 0 | 29241.04 | 16141.04 | 28504.04 | 29241.04 | 0 | (empty) |
| 40 | 2025-12-16 | -721.7 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | event_424 |
| 41 | 2025-12-17 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 42 | 2025-12-18 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 43 | 2025-12-19 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 44 | 2025-12-20 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 45 | 2025-12-21 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 46 | 2025-12-22 | 0 | 28519.34 | 15419.34 | 27782.34 | 28519.34 | 0 | (empty) |
| 47 | 2025-12-23 | -721.7 | 27797.64 | 14697.64 | 27060.64 | 27797.64 | 0 | event_424 |
| 48 | 2025-12-24 | -414.34 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | event_437 |
| 49 | 2025-12-25 | 0 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | (empty) |
| 50 | 2025-12-26 | 0 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | (empty) |
| 51 | 2025-12-27 | 0 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | (empty) |
| 52 | 2025-12-28 | 0 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | (empty) |
| 53 | 2025-12-29 | 0 | 27383.3 | 14283.3 | 26646.3 | 27383.3 | 0 | (empty) |
| 54 | 2025-12-30 | -721.7 | 26661.6 | 13561.6 | 25924.6 | 26661.6 | 0 | event_424 |
| 55 | 2025-12-31 | 0 | 26661.6 | 13561.6 | 25924.6 | 26661.6 | 0 | (empty) |
| 56 | 2026-01-01 | 0 | 26661.6 | 13561.6 | 25924.6 | 26661.6 | 0 | (empty) |
| 57 | 2026-01-02 | -4972 | 21689.6 | 8589.6 | 20952.6 | 21689.6 | 0 | event_398 |
| 58 | 2026-01-03 | 0 | 21689.6 | 8589.6 | 20952.6 | 21689.6 | 0 | (empty) |
| 59 | 2026-01-04 | 0 | 21689.6 | 8589.6 | 20952.6 | 21689.6 | 0 | (empty) |
| 60 | 2026-01-05 | 0 | 21689.6 | 8589.6 | 20952.6 | 21689.6 | 0 | (empty) |
| 61 | 2026-01-06 | -1408.41 | 20281.19 | 7181.19 | 19544.19 | 20281.19 | 0 | event_392, event_424 |
| 62 | 2026-01-07 | -414.34 | 19866.85 | 6766.85 | 19129.85 | 19866.85 | 0 | event_437 |
| 63 | 2026-01-08 | 0 | 19866.85 | 6766.85 | 19129.85 | 19866.85 | 0 | (empty) |
| 64 | 2026-01-09 | 0 | 19866.85 | 6766.85 | 19129.85 | 19866.85 | 0 | (empty) |
| 65 | 2026-01-10 | -699.01 | 19167.84 | 6067.84 | 18430.84 | 19167.84 | 0 | event_394 |
| 66 | 2026-01-11 | -968 | 18199.84 | 5099.84 | 17462.84 | 18199.84 | 0 | event_393 |
| 67 | 2026-01-12 | -511.15 | 17688.69 | 4588.69 | 16951.69 | 17688.69 | 0 | event_396, event_397 |
| 68 | 2026-01-13 | -1562.1 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | event_424, event_395 |
| 69 | 2026-01-14 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 70 | 2026-01-15 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 71 | 2026-01-16 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 72 | 2026-01-17 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 73 | 2026-01-18 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 74 | 2026-01-19 | 0 | 16126.59 | 3026.59 | 15389.59 | 16126.59 | 0 | (empty) |
| 75 | 2026-01-20 | -721.7 | 15404.89 | 2304.89 | 14667.89 | 15404.89 | 0 | event_424 |
| 76 | 2026-01-21 | -414.34 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | event_437 |
| 77 | 2026-01-22 | 0 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | (empty) |
| 78 | 2026-01-23 | 0 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | (empty) |
| 79 | 2026-01-24 | 0 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | (empty) |
| 80 | 2026-01-25 | 0 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | (empty) |
| 81 | 2026-01-26 | 0 | 14990.55 | 1890.55 | 14253.55 | 14990.55 | 0 | (empty) |
| 82 | 2026-01-27 | -721.7 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | event_424 |
| 83 | 2026-01-28 | 0 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | (empty) |
| 84 | 2026-01-29 | 0 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | (empty) |
| 85 | 2026-01-30 | 0 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | (empty) |
| 86 | 2026-01-31 | 0 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | (empty) |
| 87 | 2026-02-01 | 0 | 14268.85 | 1168.85 | 13531.85 | 14268.85 | 0 | (empty) |
| 88 | 2026-02-02 | -4972 | 9296.85 | -3803.15 | 8559.85 | 9296.85 | 0 | event_398 |
| 89 | 2026-02-03 | -721.7 | 8575.15 | -4524.85 | 7838.15 | 8575.15 | 0 | event_424 |
| 90 | 2026-02-04 | -414.34 | 8160.81 | -4939.19 | 7423.81 | 8160.81 | 0 | event_437 |

## request_06 â€” user_06 (EUR)

Request: 620.4 on 2026-01-03; deadline 2026-01-14. Opening 1942.4; minimum 800.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 603.3 | 615.58 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | full_payment | full_payment | yes |
| payment_plan | 2026-01-03:620.40 | 2026-01-03:620.40 | yes |
| earliest_date_for_full_payment | 2026-01-15 | 2026-01-15 | yes |
| spending_changes_needed | stop:event_476 | stop:event_476 | yes |

Baseline trough: day 10 (2026-01-13), balance 1415.58, headroom 615.58.

Protected: rent|insurance|transport. Reduce: . Stop: streaming.

Salary mode: temporary. Evidence: message_04. Unparsed messages: none.

- message_04 (employer, 2025-12-28T09:30:00Z): Here’s the latest payroll information from Northstar Labs. Your temporary monthly pay is EUR 1037.52. The reduced amount continues for the next payroll. This is the amount currently scheduled for the affected pay cycle. Payroll ref EMP-0004.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_475 | cloud_storage / Shared storage plan | 5 / 5 | 5 | 5.00 | 5â€“5 | 5 | 2026-01-13, 2026-02-13, 2026-03-13 |
| event_478 | entertainment / Monthly entertainment spend | 5 / 5 | 35.014 | 35.10 | 32.1â€“38.33 | 35.01 | 2026-01-15, 2026-02-15, 2026-03-15 |
| event_496 | groceries / Bulk pantry shop | 18 / 6 | 45.07833333333333333333333333 | 47.27 | 31.69â€“53.56 | 45.08 | 2026-01-07, 2026-01-17, 2026-01-27, 2026-02-06, 2026-02-16, 2026-02-26, 2026-03-08, 2026-03-18, 2026-03-28 |
| event_474 | insurance / Vehicle insurance premium | 5 / 5 | 26 | 26.00 | 26â€“26 | 26 | 2026-01-08, 2026-02-08, 2026-03-08 |
| event_472 | rent / Monthly rent | 5 / 5 | 254.1 | 254.10 | 254.1â€“254.1 | 254.1 | 2026-01-03, 2026-02-03, 2026-03-03, 2026-04-03 |
| event_477 | shopping / Household shopping | 5 / 5 | 40.998 | 39.88 | 37.96â€“46.25 | 41 | 2026-01-13, 2026-02-13, 2026-03-13 |
| event_476 | streaming / Family streaming plan | 5 / 5 | 19 | 19.00 | 19â€“19 | 19 | 2026-01-10, 2026-02-10, 2026-03-10 |
| event_531 | transport / Parking and tolls | 35 / 6 | 26.976 | 27.80 | 19.18â€“32.9 | 26.98 | 2026-01-03, 2026-01-08, 2026-01-13, 2026-01-18, 2026-01-23, 2026-01-28, 2026-02-02, 2026-02-07, 2026-02-12, 2026-02-17, 2026-02-22, 2026-02-27, 2026-03-04, 2026-03-09, 2026-03-14, 2026-03-19, 2026-03-24, 2026-03-29, 2026-04-03 |
| event_473 | utilities / Water and power payment | 5 / 5 | 55.702 | 56.71 | 51.86â€“58.98 | 55.7 | 2026-01-07, 2026-02-07, 2026-03-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-01-03 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-01-03 | -254.1 | event_472 | rent | recurring_expense | Monthly rent |
| 2026-01-07 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-01-07 | -55.7 | event_473 | utilities | recurring_expense | Water and power payment |
| 2026-01-08 | -26 | event_474 | insurance | recurring_expense | Vehicle insurance premium |
| 2026-01-08 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-01-10 | -19 | event_476 | streaming | recurring_expense | Family streaming plan |
| 2026-01-13 | -5 | event_475 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-01-13 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-01-13 | -41 | event_477 | shopping | recurring_expense | Household shopping |
| 2026-01-15 | 1037.52 | event_471 | salary | recurring_income | Payroll credit |
| 2026-01-15 | -35.01 | event_478 | entertainment | recurring_expense | Monthly entertainment spend |
| 2026-01-17 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-01-18 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-01-23 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-01-27 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-01-28 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-02 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-03 | -254.1 | event_472 | rent | recurring_expense | Monthly rent |
| 2026-02-06 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-02-07 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-07 | -55.7 | event_473 | utilities | recurring_expense | Water and power payment |
| 2026-02-08 | -26 | event_474 | insurance | recurring_expense | Vehicle insurance premium |
| 2026-02-10 | -19 | event_476 | streaming | recurring_expense | Family streaming plan |
| 2026-02-12 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-13 | -5 | event_475 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-02-13 | -41 | event_477 | shopping | recurring_expense | Household shopping |
| 2026-02-15 | 1037.52 | event_471 | salary | recurring_income | Payroll credit |
| 2026-02-15 | -35.01 | event_478 | entertainment | recurring_expense | Monthly entertainment spend |
| 2026-02-16 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-02-17 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-22 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-02-26 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-02-27 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-03 | -254.1 | event_472 | rent | recurring_expense | Monthly rent |
| 2026-03-04 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-07 | -55.7 | event_473 | utilities | recurring_expense | Water and power payment |
| 2026-03-08 | -26 | event_474 | insurance | recurring_expense | Vehicle insurance premium |
| 2026-03-08 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-03-09 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-10 | -19 | event_476 | streaming | recurring_expense | Family streaming plan |
| 2026-03-13 | -5 | event_475 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-03-13 | -41 | event_477 | shopping | recurring_expense | Household shopping |
| 2026-03-14 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-15 | 1037.52 | event_471 | salary | recurring_income | Payroll credit |
| 2026-03-15 | -35.01 | event_478 | entertainment | recurring_expense | Monthly entertainment spend |
| 2026-03-18 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-03-19 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-24 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-03-28 | -45.08 | event_496 | groceries | recurring_expense | Bulk pantry shop |
| 2026-03-29 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-04-03 | -26.98 | event_531 | transport | recurring_expense | Parking and tolls |
| 2026-04-03 | -254.1 | event_472 | rent | recurring_expense | Monthly rent |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-01-03 | -281.08 | 1661.32 | 861.32 | 1058.02 | 1040.92 | 620.4 | event_531, event_472 |
| 1 | 2026-01-04 | 0 | 1661.32 | 861.32 | 1058.02 | 1040.92 | 0 | (empty) |
| 2 | 2026-01-05 | 0 | 1661.32 | 861.32 | 1058.02 | 1040.92 | 0 | (empty) |
| 3 | 2026-01-06 | 0 | 1661.32 | 861.32 | 1058.02 | 1040.92 | 0 | (empty) |
| 4 | 2026-01-07 | -100.78 | 1560.54 | 760.54 | 957.24 | 940.14 | 0 | event_496, event_473 |
| 5 | 2026-01-08 | -52.98 | 1507.56 | 707.56 | 904.26 | 887.16 | 0 | event_474, event_531 |
| 6 | 2026-01-09 | 0 | 1507.56 | 707.56 | 904.26 | 887.16 | 0 | (empty) |
| 7 | 2026-01-10 | -19 | 1488.56 | 688.56 | 885.26 | 887.16 | 0 | event_476 |
| 8 | 2026-01-11 | 0 | 1488.56 | 688.56 | 885.26 | 887.16 | 0 | (empty) |
| 9 | 2026-01-12 | 0 | 1488.56 | 688.56 | 885.26 | 887.16 | 0 | (empty) |
| 10 | 2026-01-13 | -72.98 | 1415.58 | 615.58 | 812.28 | 814.18 | 0 | event_475, event_531, event_477 |
| 11 | 2026-01-14 | 0 | 1415.58 | 615.58 | 812.28 | 814.18 | 0 | (empty) |
| 12 | 2026-01-15 | 1002.51 | 2418.09 | 1618.09 | 1814.79 | 1816.69 | 0 | event_471, event_478 |
| 13 | 2026-01-16 | 0 | 2418.09 | 1618.09 | 1814.79 | 1816.69 | 0 | (empty) |
| 14 | 2026-01-17 | -45.08 | 2373.01 | 1573.01 | 1769.71 | 1771.61 | 0 | event_496 |
| 15 | 2026-01-18 | -26.98 | 2346.03 | 1546.03 | 1742.73 | 1744.63 | 0 | event_531 |
| 16 | 2026-01-19 | 0 | 2346.03 | 1546.03 | 1742.73 | 1744.63 | 0 | (empty) |
| 17 | 2026-01-20 | 0 | 2346.03 | 1546.03 | 1742.73 | 1744.63 | 0 | (empty) |
| 18 | 2026-01-21 | 0 | 2346.03 | 1546.03 | 1742.73 | 1744.63 | 0 | (empty) |
| 19 | 2026-01-22 | 0 | 2346.03 | 1546.03 | 1742.73 | 1744.63 | 0 | (empty) |
| 20 | 2026-01-23 | -26.98 | 2319.05 | 1519.05 | 1715.75 | 1717.65 | 0 | event_531 |
| 21 | 2026-01-24 | 0 | 2319.05 | 1519.05 | 1715.75 | 1717.65 | 0 | (empty) |
| 22 | 2026-01-25 | 0 | 2319.05 | 1519.05 | 1715.75 | 1717.65 | 0 | (empty) |
| 23 | 2026-01-26 | 0 | 2319.05 | 1519.05 | 1715.75 | 1717.65 | 0 | (empty) |
| 24 | 2026-01-27 | -45.08 | 2273.97 | 1473.97 | 1670.67 | 1672.57 | 0 | event_496 |
| 25 | 2026-01-28 | -26.98 | 2246.99 | 1446.99 | 1643.69 | 1645.59 | 0 | event_531 |
| 26 | 2026-01-29 | 0 | 2246.99 | 1446.99 | 1643.69 | 1645.59 | 0 | (empty) |
| 27 | 2026-01-30 | 0 | 2246.99 | 1446.99 | 1643.69 | 1645.59 | 0 | (empty) |
| 28 | 2026-01-31 | 0 | 2246.99 | 1446.99 | 1643.69 | 1645.59 | 0 | (empty) |
| 29 | 2026-02-01 | 0 | 2246.99 | 1446.99 | 1643.69 | 1645.59 | 0 | (empty) |
| 30 | 2026-02-02 | -26.98 | 2220.01 | 1420.01 | 1616.71 | 1618.61 | 0 | event_531 |
| 31 | 2026-02-03 | -254.1 | 1965.91 | 1165.91 | 1362.61 | 1364.51 | 0 | event_472 |
| 32 | 2026-02-04 | 0 | 1965.91 | 1165.91 | 1362.61 | 1364.51 | 0 | (empty) |
| 33 | 2026-02-05 | 0 | 1965.91 | 1165.91 | 1362.61 | 1364.51 | 0 | (empty) |
| 34 | 2026-02-06 | -45.08 | 1920.83 | 1120.83 | 1317.53 | 1319.43 | 0 | event_496 |
| 35 | 2026-02-07 | -82.68 | 1838.15 | 1038.15 | 1234.85 | 1236.75 | 0 | event_531, event_473 |
| 36 | 2026-02-08 | -26 | 1812.15 | 1012.15 | 1208.85 | 1210.75 | 0 | event_474 |
| 37 | 2026-02-09 | 0 | 1812.15 | 1012.15 | 1208.85 | 1210.75 | 0 | (empty) |
| 38 | 2026-02-10 | -19 | 1793.15 | 993.15 | 1189.85 | 1210.75 | 0 | event_476 |
| 39 | 2026-02-11 | 0 | 1793.15 | 993.15 | 1189.85 | 1210.75 | 0 | (empty) |
| 40 | 2026-02-12 | -26.98 | 1766.17 | 966.17 | 1162.87 | 1183.77 | 0 | event_531 |
| 41 | 2026-02-13 | -46 | 1720.17 | 920.17 | 1116.87 | 1137.77 | 0 | event_475, event_477 |
| 42 | 2026-02-14 | 0 | 1720.17 | 920.17 | 1116.87 | 1137.77 | 0 | (empty) |
| 43 | 2026-02-15 | 1002.51 | 2722.68 | 1922.68 | 2119.38 | 2140.28 | 0 | event_471, event_478 |
| 44 | 2026-02-16 | -45.08 | 2677.6 | 1877.6 | 2074.3 | 2095.2 | 0 | event_496 |
| 45 | 2026-02-17 | -26.98 | 2650.62 | 1850.62 | 2047.32 | 2068.22 | 0 | event_531 |
| 46 | 2026-02-18 | 0 | 2650.62 | 1850.62 | 2047.32 | 2068.22 | 0 | (empty) |
| 47 | 2026-02-19 | 0 | 2650.62 | 1850.62 | 2047.32 | 2068.22 | 0 | (empty) |
| 48 | 2026-02-20 | 0 | 2650.62 | 1850.62 | 2047.32 | 2068.22 | 0 | (empty) |
| 49 | 2026-02-21 | 0 | 2650.62 | 1850.62 | 2047.32 | 2068.22 | 0 | (empty) |
| 50 | 2026-02-22 | -26.98 | 2623.64 | 1823.64 | 2020.34 | 2041.24 | 0 | event_531 |
| 51 | 2026-02-23 | 0 | 2623.64 | 1823.64 | 2020.34 | 2041.24 | 0 | (empty) |
| 52 | 2026-02-24 | 0 | 2623.64 | 1823.64 | 2020.34 | 2041.24 | 0 | (empty) |
| 53 | 2026-02-25 | 0 | 2623.64 | 1823.64 | 2020.34 | 2041.24 | 0 | (empty) |
| 54 | 2026-02-26 | -45.08 | 2578.56 | 1778.56 | 1975.26 | 1996.16 | 0 | event_496 |
| 55 | 2026-02-27 | -26.98 | 2551.58 | 1751.58 | 1948.28 | 1969.18 | 0 | event_531 |
| 56 | 2026-02-28 | 0 | 2551.58 | 1751.58 | 1948.28 | 1969.18 | 0 | (empty) |
| 57 | 2026-03-01 | 0 | 2551.58 | 1751.58 | 1948.28 | 1969.18 | 0 | (empty) |
| 58 | 2026-03-02 | 0 | 2551.58 | 1751.58 | 1948.28 | 1969.18 | 0 | (empty) |
| 59 | 2026-03-03 | -254.1 | 2297.48 | 1497.48 | 1694.18 | 1715.08 | 0 | event_472 |
| 60 | 2026-03-04 | -26.98 | 2270.5 | 1470.5 | 1667.2 | 1688.1 | 0 | event_531 |
| 61 | 2026-03-05 | 0 | 2270.5 | 1470.5 | 1667.2 | 1688.1 | 0 | (empty) |
| 62 | 2026-03-06 | 0 | 2270.5 | 1470.5 | 1667.2 | 1688.1 | 0 | (empty) |
| 63 | 2026-03-07 | -55.7 | 2214.8 | 1414.8 | 1611.5 | 1632.4 | 0 | event_473 |
| 64 | 2026-03-08 | -71.08 | 2143.72 | 1343.72 | 1540.42 | 1561.32 | 0 | event_474, event_496 |
| 65 | 2026-03-09 | -26.98 | 2116.74 | 1316.74 | 1513.44 | 1534.34 | 0 | event_531 |
| 66 | 2026-03-10 | -19 | 2097.74 | 1297.74 | 1494.44 | 1534.34 | 0 | event_476 |
| 67 | 2026-03-11 | 0 | 2097.74 | 1297.74 | 1494.44 | 1534.34 | 0 | (empty) |
| 68 | 2026-03-12 | 0 | 2097.74 | 1297.74 | 1494.44 | 1534.34 | 0 | (empty) |
| 69 | 2026-03-13 | -46 | 2051.74 | 1251.74 | 1448.44 | 1488.34 | 0 | event_475, event_477 |
| 70 | 2026-03-14 | -26.98 | 2024.76 | 1224.76 | 1421.46 | 1461.36 | 0 | event_531 |
| 71 | 2026-03-15 | 1002.51 | 3027.27 | 2227.27 | 2423.97 | 2463.87 | 0 | event_471, event_478 |
| 72 | 2026-03-16 | 0 | 3027.27 | 2227.27 | 2423.97 | 2463.87 | 0 | (empty) |
| 73 | 2026-03-17 | 0 | 3027.27 | 2227.27 | 2423.97 | 2463.87 | 0 | (empty) |
| 74 | 2026-03-18 | -45.08 | 2982.19 | 2182.19 | 2378.89 | 2418.79 | 0 | event_496 |
| 75 | 2026-03-19 | -26.98 | 2955.21 | 2155.21 | 2351.91 | 2391.81 | 0 | event_531 |
| 76 | 2026-03-20 | 0 | 2955.21 | 2155.21 | 2351.91 | 2391.81 | 0 | (empty) |
| 77 | 2026-03-21 | 0 | 2955.21 | 2155.21 | 2351.91 | 2391.81 | 0 | (empty) |
| 78 | 2026-03-22 | 0 | 2955.21 | 2155.21 | 2351.91 | 2391.81 | 0 | (empty) |
| 79 | 2026-03-23 | 0 | 2955.21 | 2155.21 | 2351.91 | 2391.81 | 0 | (empty) |
| 80 | 2026-03-24 | -26.98 | 2928.23 | 2128.23 | 2324.93 | 2364.83 | 0 | event_531 |
| 81 | 2026-03-25 | 0 | 2928.23 | 2128.23 | 2324.93 | 2364.83 | 0 | (empty) |
| 82 | 2026-03-26 | 0 | 2928.23 | 2128.23 | 2324.93 | 2364.83 | 0 | (empty) |
| 83 | 2026-03-27 | 0 | 2928.23 | 2128.23 | 2324.93 | 2364.83 | 0 | (empty) |
| 84 | 2026-03-28 | -45.08 | 2883.15 | 2083.15 | 2279.85 | 2319.75 | 0 | event_496 |
| 85 | 2026-03-29 | -26.98 | 2856.17 | 2056.17 | 2252.87 | 2292.77 | 0 | event_531 |
| 86 | 2026-03-30 | 0 | 2856.17 | 2056.17 | 2252.87 | 2292.77 | 0 | (empty) |
| 87 | 2026-03-31 | 0 | 2856.17 | 2056.17 | 2252.87 | 2292.77 | 0 | (empty) |
| 88 | 2026-04-01 | 0 | 2856.17 | 2056.17 | 2252.87 | 2292.77 | 0 | (empty) |
| 89 | 2026-04-02 | 0 | 2856.17 | 2056.17 | 2252.87 | 2292.77 | 0 | (empty) |
| 90 | 2026-04-03 | -281.08 | 2575.09 | 1775.09 | 1971.79 | 2011.69 | 0 | event_531, event_472 |

## request_07 â€” user_07 (INR)

Request: 197400 on 2024-09-05; deadline 2024-11-14. Opening 218945.56; minimum 93000.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 87170.56 | 86237.22 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | installments | installments | yes |
| payment_plan | 2024-09-12:68432\|2024-10-10:68432\|2024-11-07:68432 | 2024-09-12:68432\|2024-10-10:68432\|2024-11-07:68432 | yes |
| earliest_date_for_full_payment | 2024-10-23 | 2024-10-23 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 15 (2024-09-20), balance 179237.22, headroom 86237.22.

Protected: rent|utilities|debt_repayment. Reduce: dining. Stop: music_subscription.

Salary mode: delay. Evidence: message_05. Unparsed messages: none.

- message_05 (employer, 2024-08-29T09:30:00Z): BrightPath Media has updated your payroll record. Your confirmed salary is now expected on 2024-09-23. This replaces the payroll date shown in the earlier update. Please use the revised date for anything you normally pay around payday. Payroll ref EMP-0005.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_581 | debt_repayment / Personal loan payment | 5 / 5 | 15650 | 15650.00 | 15650â€“15650 | 15650 | 2024-09-13, 2024-10-13, 2024-11-13 |
| event_614 | dining / Bakery and snacks | 9 / 6 | 5927.314444444444444444444444 | 6313.91 | 4111.12â€“7246.72 | 5927.31 | 2024-09-16, 2024-10-07, 2024-10-28, 2024-11-18 |
| event_596 | groceries / Household groceries | 13 / 6 | 7116.46 | 7280.22 | 5665.77â€“8380.73 | 7116.46 | 2024-09-12, 2024-09-26, 2024-10-10, 2024-10-24, 2024-11-07, 2024-11-21 |
| event_582 | music_subscription / Music subscription | 5 / 5 | 1005 | 1005.00 | 1005â€“1005 | 1005 | 2024-09-13, 2024-10-13, 2024-11-13 |
| event_583 | rent / Monthly rent | 6 / 6 | 34200 | 34200.00 | 34200â€“34200 | 34200 | 2024-10-04, 2024-11-04, 2024-12-04 |
| event_605 | transport / Commuter pass | 9 / 6 | 3220.133333333333333333333333 | 3145.62 | 2439.43â€“3822.62 | 3220.13 | 2024-09-20, 2024-10-11, 2024-11-01, 2024-11-22 |
| event_580 | utilities / Electricity bill | 5 / 5 | 6789.444 | 7049.68 | 6081.25â€“7387.41 | 6789.44 | 2024-09-08, 2024-10-08, 2024-11-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-09-08 | -6789.44 | event_580 | utilities | recurring_expense | Electricity bill |
| 2024-09-12 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-09-13 | -1005 | event_582 | music_subscription | recurring_expense | Music subscription |
| 2024-09-13 | -15650 | event_581 | debt_repayment | recurring_expense | Personal loan payment |
| 2024-09-16 | -5927.31 | event_614 | dining | recurring_expense | Bakery and snacks |
| 2024-09-20 | -3220.13 | event_605 | transport | recurring_expense | Commuter pass |
| 2024-09-23 | 149000 | event_578 | salary | recurring_income | Payroll credit |
| 2024-09-26 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-10-04 | -34200 | event_583 | rent | recurring_expense | Monthly rent |
| 2024-10-07 | -5927.31 | event_614 | dining | recurring_expense | Bakery and snacks |
| 2024-10-08 | -6789.44 | event_580 | utilities | recurring_expense | Electricity bill |
| 2024-10-10 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-10-11 | -3220.13 | event_605 | transport | recurring_expense | Commuter pass |
| 2024-10-13 | -1005 | event_582 | music_subscription | recurring_expense | Music subscription |
| 2024-10-13 | -15650 | event_581 | debt_repayment | recurring_expense | Personal loan payment |
| 2024-10-23 | 149000 | event_578 | salary | recurring_income | Payroll credit |
| 2024-10-24 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-10-28 | -5927.31 | event_614 | dining | recurring_expense | Bakery and snacks |
| 2024-11-01 | -3220.13 | event_605 | transport | recurring_expense | Commuter pass |
| 2024-11-04 | -34200 | event_583 | rent | recurring_expense | Monthly rent |
| 2024-11-07 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-11-08 | -6789.44 | event_580 | utilities | recurring_expense | Electricity bill |
| 2024-11-13 | -1005 | event_582 | music_subscription | recurring_expense | Music subscription |
| 2024-11-13 | -15650 | event_581 | debt_repayment | recurring_expense | Personal loan payment |
| 2024-11-18 | -5927.31 | event_614 | dining | recurring_expense | Bakery and snacks |
| 2024-11-21 | -7116.46 | event_596 | groceries | recurring_expense | Household groceries |
| 2024-11-22 | -3220.13 | event_605 | transport | recurring_expense | Commuter pass |
| 2024-11-23 | 149000 | event_578 | salary | recurring_income | Payroll credit |
| 2024-12-04 | -34200 | event_583 | rent | recurring_expense | Monthly rent |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-09-05 | 0 | 218945.56 | 125945.56 | 131775 | 218945.56 | 0 | (empty) |
| 1 | 2024-09-06 | 0 | 218945.56 | 125945.56 | 131775 | 218945.56 | 0 | (empty) |
| 2 | 2024-09-07 | 0 | 218945.56 | 125945.56 | 131775 | 218945.56 | 0 | (empty) |
| 3 | 2024-09-08 | -6789.44 | 212156.12 | 119156.12 | 124985.56 | 212156.12 | 0 | event_580 |
| 4 | 2024-09-09 | 0 | 212156.12 | 119156.12 | 124985.56 | 212156.12 | 0 | (empty) |
| 5 | 2024-09-10 | 0 | 212156.12 | 119156.12 | 124985.56 | 212156.12 | 0 | (empty) |
| 6 | 2024-09-11 | 0 | 212156.12 | 119156.12 | 124985.56 | 212156.12 | 0 | (empty) |
| 7 | 2024-09-12 | -7116.46 | 205039.66 | 112039.66 | 117869.1 | 136607.66 | 68432 | event_596 |
| 8 | 2024-09-13 | -16655 | 188384.66 | 95384.66 | 101214.1 | 119952.66 | 0 | event_582, event_581 |
| 9 | 2024-09-14 | 0 | 188384.66 | 95384.66 | 101214.1 | 119952.66 | 0 | (empty) |
| 10 | 2024-09-15 | 0 | 188384.66 | 95384.66 | 101214.1 | 119952.66 | 0 | (empty) |
| 11 | 2024-09-16 | -5927.31 | 182457.35 | 89457.35 | 95286.79 | 114025.35 | 0 | event_614 |
| 12 | 2024-09-17 | 0 | 182457.35 | 89457.35 | 95286.79 | 114025.35 | 0 | (empty) |
| 13 | 2024-09-18 | 0 | 182457.35 | 89457.35 | 95286.79 | 114025.35 | 0 | (empty) |
| 14 | 2024-09-19 | 0 | 182457.35 | 89457.35 | 95286.79 | 114025.35 | 0 | (empty) |
| 15 | 2024-09-20 | -3220.13 | 179237.22 | 86237.22 | 92066.66 | 110805.22 | 0 | event_605 |
| 16 | 2024-09-21 | 0 | 179237.22 | 86237.22 | 92066.66 | 110805.22 | 0 | (empty) |
| 17 | 2024-09-22 | 0 | 179237.22 | 86237.22 | 92066.66 | 110805.22 | 0 | (empty) |
| 18 | 2024-09-23 | 149000 | 328237.22 | 235237.22 | 241066.66 | 259805.22 | 0 | event_578 |
| 19 | 2024-09-24 | 0 | 328237.22 | 235237.22 | 241066.66 | 259805.22 | 0 | (empty) |
| 20 | 2024-09-25 | 0 | 328237.22 | 235237.22 | 241066.66 | 259805.22 | 0 | (empty) |
| 21 | 2024-09-26 | -7116.46 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | event_596 |
| 22 | 2024-09-27 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 23 | 2024-09-28 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 24 | 2024-09-29 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 25 | 2024-09-30 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 26 | 2024-10-01 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 27 | 2024-10-02 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 28 | 2024-10-03 | 0 | 321120.76 | 228120.76 | 233950.2 | 252688.76 | 0 | (empty) |
| 29 | 2024-10-04 | -34200 | 286920.76 | 193920.76 | 199750.2 | 218488.76 | 0 | event_583 |
| 30 | 2024-10-05 | 0 | 286920.76 | 193920.76 | 199750.2 | 218488.76 | 0 | (empty) |
| 31 | 2024-10-06 | 0 | 286920.76 | 193920.76 | 199750.2 | 218488.76 | 0 | (empty) |
| 32 | 2024-10-07 | -5927.31 | 280993.45 | 187993.45 | 193822.89 | 212561.45 | 0 | event_614 |
| 33 | 2024-10-08 | -6789.44 | 274204.01 | 181204.01 | 187033.45 | 205772.01 | 0 | event_580 |
| 34 | 2024-10-09 | 0 | 274204.01 | 181204.01 | 187033.45 | 205772.01 | 0 | (empty) |
| 35 | 2024-10-10 | -7116.46 | 267087.55 | 174087.55 | 179916.99 | 130223.55 | 68432 | event_596 |
| 36 | 2024-10-11 | -3220.13 | 263867.42 | 170867.42 | 176696.86 | 127003.42 | 0 | event_605 |
| 37 | 2024-10-12 | 0 | 263867.42 | 170867.42 | 176696.86 | 127003.42 | 0 | (empty) |
| 38 | 2024-10-13 | -16655 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | event_582, event_581 |
| 39 | 2024-10-14 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 40 | 2024-10-15 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 41 | 2024-10-16 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 42 | 2024-10-17 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 43 | 2024-10-18 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 44 | 2024-10-19 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 45 | 2024-10-20 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 46 | 2024-10-21 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 47 | 2024-10-22 | 0 | 247212.42 | 154212.42 | 160041.86 | 110348.42 | 0 | (empty) |
| 48 | 2024-10-23 | 149000 | 396212.42 | 303212.42 | 309041.86 | 259348.42 | 0 | event_578 |
| 49 | 2024-10-24 | -7116.46 | 389095.96 | 296095.96 | 301925.4 | 252231.96 | 0 | event_596 |
| 50 | 2024-10-25 | 0 | 389095.96 | 296095.96 | 301925.4 | 252231.96 | 0 | (empty) |
| 51 | 2024-10-26 | 0 | 389095.96 | 296095.96 | 301925.4 | 252231.96 | 0 | (empty) |
| 52 | 2024-10-27 | 0 | 389095.96 | 296095.96 | 301925.4 | 252231.96 | 0 | (empty) |
| 53 | 2024-10-28 | -5927.31 | 383168.65 | 290168.65 | 295998.09 | 246304.65 | 0 | event_614 |
| 54 | 2024-10-29 | 0 | 383168.65 | 290168.65 | 295998.09 | 246304.65 | 0 | (empty) |
| 55 | 2024-10-30 | 0 | 383168.65 | 290168.65 | 295998.09 | 246304.65 | 0 | (empty) |
| 56 | 2024-10-31 | 0 | 383168.65 | 290168.65 | 295998.09 | 246304.65 | 0 | (empty) |
| 57 | 2024-11-01 | -3220.13 | 379948.52 | 286948.52 | 292777.96 | 243084.52 | 0 | event_605 |
| 58 | 2024-11-02 | 0 | 379948.52 | 286948.52 | 292777.96 | 243084.52 | 0 | (empty) |
| 59 | 2024-11-03 | 0 | 379948.52 | 286948.52 | 292777.96 | 243084.52 | 0 | (empty) |
| 60 | 2024-11-04 | -34200 | 345748.52 | 252748.52 | 258577.96 | 208884.52 | 0 | event_583 |
| 61 | 2024-11-05 | 0 | 345748.52 | 252748.52 | 258577.96 | 208884.52 | 0 | (empty) |
| 62 | 2024-11-06 | 0 | 345748.52 | 252748.52 | 258577.96 | 208884.52 | 0 | (empty) |
| 63 | 2024-11-07 | -7116.46 | 338632.06 | 245632.06 | 251461.5 | 133336.06 | 68432 | event_596 |
| 64 | 2024-11-08 | -6789.44 | 331842.62 | 238842.62 | 244672.06 | 126546.62 | 0 | event_580 |
| 65 | 2024-11-09 | 0 | 331842.62 | 238842.62 | 244672.06 | 126546.62 | 0 | (empty) |
| 66 | 2024-11-10 | 0 | 331842.62 | 238842.62 | 244672.06 | 126546.62 | 0 | (empty) |
| 67 | 2024-11-11 | 0 | 331842.62 | 238842.62 | 244672.06 | 126546.62 | 0 | (empty) |
| 68 | 2024-11-12 | 0 | 331842.62 | 238842.62 | 244672.06 | 126546.62 | 0 | (empty) |
| 69 | 2024-11-13 | -16655 | 315187.62 | 222187.62 | 228017.06 | 109891.62 | 0 | event_582, event_581 |
| 70 | 2024-11-14 | 0 | 315187.62 | 222187.62 | 228017.06 | 109891.62 | 0 | (empty) |
| 71 | 2024-11-15 | 0 | 315187.62 | 222187.62 | 228017.06 | 109891.62 | 0 | (empty) |
| 72 | 2024-11-16 | 0 | 315187.62 | 222187.62 | 228017.06 | 109891.62 | 0 | (empty) |
| 73 | 2024-11-17 | 0 | 315187.62 | 222187.62 | 228017.06 | 109891.62 | 0 | (empty) |
| 74 | 2024-11-18 | -5927.31 | 309260.31 | 216260.31 | 222089.75 | 103964.31 | 0 | event_614 |
| 75 | 2024-11-19 | 0 | 309260.31 | 216260.31 | 222089.75 | 103964.31 | 0 | (empty) |
| 76 | 2024-11-20 | 0 | 309260.31 | 216260.31 | 222089.75 | 103964.31 | 0 | (empty) |
| 77 | 2024-11-21 | -7116.46 | 302143.85 | 209143.85 | 214973.29 | 96847.85 | 0 | event_596 |
| 78 | 2024-11-22 | -3220.13 | 298923.72 | 205923.72 | 211753.16 | 93627.72 | 0 | event_605 |
| 79 | 2024-11-23 | 149000 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | event_578 |
| 80 | 2024-11-24 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 81 | 2024-11-25 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 82 | 2024-11-26 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 83 | 2024-11-27 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 84 | 2024-11-28 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 85 | 2024-11-29 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 86 | 2024-11-30 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 87 | 2024-12-01 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 88 | 2024-12-02 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 89 | 2024-12-03 | 0 | 447923.72 | 354923.72 | 360753.16 | 242627.72 | 0 | (empty) |
| 90 | 2024-12-04 | -34200 | 413723.72 | 320723.72 | 326553.16 | 208427.72 | 0 | event_583 |

## request_08 â€” user_08 (EUR)

Request: 996.6 on 2025-02-07; deadline 2025-04-15. Opening 1536.57; minimum 800.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 284.57 | 285.2 | NO |
| affordability_status | affordable_later | affordable_with_plan | NO |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2025-04-15:996.60 | 2025-04-15:996.60 | yes |
| earliest_date_for_full_payment | 2025-04-15 | (empty) | NO |
| spending_changes_needed | none | stop:event_649\|reduce_to:event_716:24.50 | NO |

Baseline trough: day 6 (2025-02-13), balance 1085.2, headroom 285.2.

Protected: rent|education|groceries|debt_repayment. Reduce: dining. Stop: music_subscription|delivery_membership.

Salary mode: reduced. Evidence: message_06. Unparsed messages: none.

- message_06 (employer, 2025-02-06T09:30:00Z): Hi, Greenfield Foods payroll here. Your next salary is reduced to EUR 1422.85. The adjustment is due to approved unpaid leave. The adjustment will be visible on your next payslip. Payroll ref EMP-0006.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_647 | debt_repayment / Personal loan payment | 5 / 5 | 177 | 177.00 | 177â€“177 | 177 | 2025-02-10, 2025-03-10, 2025-04-10 |
| event_649 | delivery_membership / Grocery delivery membership | 5 / 5 | 24 | 24.00 | 24â€“24 | 24 | 2025-02-12, 2025-03-12, 2025-04-12 |
| event_716 | dining / Bakery and snacks | 13 / 6 | 50.84307692307692307692307692 | 49.45 | 41.5â€“60.66 | 50.84 | 2025-02-13, 2025-02-27, 2025-03-13, 2025-03-27, 2025-04-10, 2025-04-24, 2025-05-08 |
| event_646 | education / School fee payment | 5 / 5 | 89 | 89.00 | 89â€“89 | 89 | 2025-02-07, 2025-03-07, 2025-04-07, 2025-05-07 |
| event_677 | groceries / Weekly produce market | 26 / 7 | 59.04153846153846153846153846 | 54.685 | 45.99â€“78.42 | 59.04 | 2025-02-11, 2025-02-18, 2025-02-25, 2025-03-04, 2025-03-11, 2025-03-18, 2025-03-25, 2025-04-01, 2025-04-08, 2025-04-15, 2025-04-22, 2025-04-29, 2025-05-06 |
| event_648 | music_subscription / Music subscription | 5 / 5 | 14 | 14.00 | 14â€“14 | 14 | 2025-02-10, 2025-03-10, 2025-04-10 |
| event_650 | rent / Apartment rent transfer | 6 / 6 | 467.5 | 467.50 | 467.5â€“467.5 | 467.5 | 2025-03-01, 2025-04-01, 2025-05-01 |
| event_703 | transport / Fuel refill | 26 / 7 | 37.48769230769230769230769231 | 37.31 | 26.69â€“47.21 | 37.49 | 2025-02-12, 2025-02-19, 2025-02-26, 2025-03-05, 2025-03-12, 2025-03-19, 2025-03-26, 2025-04-02, 2025-04-09, 2025-04-16, 2025-04-23, 2025-04-30, 2025-05-07 |
| event_651 | utilities / Municipal utilities | 6 / 6 | 76.82833333333333333333333333 | 79.87 | 68.44â€“82.61 | 76.83 | 2025-03-05, 2025-04-05, 2025-05-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-02-07 | -89 | event_646 | education | recurring_expense | School fee payment |
| 2025-02-10 | -14 | event_648 | music_subscription | recurring_expense | Music subscription |
| 2025-02-10 | -177 | event_647 | debt_repayment | recurring_expense | Personal loan payment |
| 2025-02-11 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-02-12 | -24 | event_649 | delivery_membership | recurring_expense | Grocery delivery membership |
| 2025-02-12 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-02-13 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-02-15 | 1422.85 | event_643 | salary | recurring_income | Payroll credit |
| 2025-02-18 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-02-19 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-02-25 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-02-26 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-02-27 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-03-01 | -467.5 | event_650 | rent | recurring_expense | Apartment rent transfer |
| 2025-03-04 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-03-05 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-03-05 | -76.83 | event_651 | utilities | recurring_expense | Municipal utilities |
| 2025-03-07 | -89 | event_646 | education | recurring_expense | School fee payment |
| 2025-03-10 | -14 | event_648 | music_subscription | recurring_expense | Music subscription |
| 2025-03-10 | -177 | event_647 | debt_repayment | recurring_expense | Personal loan payment |
| 2025-03-11 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-03-12 | -24 | event_649 | delivery_membership | recurring_expense | Grocery delivery membership |
| 2025-03-12 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-03-13 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-03-15 | 1422.85 | event_643 | salary | recurring_income | Payroll credit |
| 2025-03-18 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-03-19 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-03-25 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-03-26 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-03-27 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-04-01 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-04-01 | -467.5 | event_650 | rent | recurring_expense | Apartment rent transfer |
| 2025-04-02 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-04-05 | -76.83 | event_651 | utilities | recurring_expense | Municipal utilities |
| 2025-04-07 | -89 | event_646 | education | recurring_expense | School fee payment |
| 2025-04-08 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-04-09 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-04-10 | -14 | event_648 | music_subscription | recurring_expense | Music subscription |
| 2025-04-10 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-04-10 | -177 | event_647 | debt_repayment | recurring_expense | Personal loan payment |
| 2025-04-12 | -24 | event_649 | delivery_membership | recurring_expense | Grocery delivery membership |
| 2025-04-15 | 1422.85 | event_643 | salary | recurring_income | Payroll credit |
| 2025-04-15 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-04-16 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-04-22 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-04-23 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-04-24 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |
| 2025-04-29 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-04-30 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-05-01 | -467.5 | event_650 | rent | recurring_expense | Apartment rent transfer |
| 2025-05-05 | -76.83 | event_651 | utilities | recurring_expense | Municipal utilities |
| 2025-05-06 | -59.04 | event_677 | groceries | recurring_expense | Weekly produce market |
| 2025-05-07 | -37.49 | event_703 | transport | recurring_expense | Fuel refill |
| 2025-05-07 | -89 | event_646 | education | recurring_expense | School fee payment |
| 2025-05-08 | -50.84 | event_716 | dining | recurring_expense | Bakery and snacks |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-02-07 | -89 | 1447.57 | 647.57 | 1163 | 1447.57 | 0 | event_646 |
| 1 | 2025-02-08 | 0 | 1447.57 | 647.57 | 1163 | 1447.57 | 0 | (empty) |
| 2 | 2025-02-09 | 0 | 1447.57 | 647.57 | 1163 | 1447.57 | 0 | (empty) |
| 3 | 2025-02-10 | -191 | 1256.57 | 456.57 | 972 | 1256.57 | 0 | event_648, event_647 |
| 4 | 2025-02-11 | -59.04 | 1197.53 | 397.53 | 912.96 | 1197.53 | 0 | event_677 |
| 5 | 2025-02-12 | -61.49 | 1136.04 | 336.04 | 851.47 | 1160.04 | 0 | event_649, event_703 |
| 6 | 2025-02-13 | -50.84 | 1085.2 | 285.2 | 800.63 | 1135.54 | 0 | event_716 |
| 7 | 2025-02-14 | 0 | 1085.2 | 285.2 | 800.63 | 1135.54 | 0 | (empty) |
| 8 | 2025-02-15 | 1422.85 | 2508.05 | 1708.05 | 2223.48 | 2558.39 | 0 | event_643 |
| 9 | 2025-02-16 | 0 | 2508.05 | 1708.05 | 2223.48 | 2558.39 | 0 | (empty) |
| 10 | 2025-02-17 | 0 | 2508.05 | 1708.05 | 2223.48 | 2558.39 | 0 | (empty) |
| 11 | 2025-02-18 | -59.04 | 2449.01 | 1649.01 | 2164.44 | 2499.35 | 0 | event_677 |
| 12 | 2025-02-19 | -37.49 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | event_703 |
| 13 | 2025-02-20 | 0 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | (empty) |
| 14 | 2025-02-21 | 0 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | (empty) |
| 15 | 2025-02-22 | 0 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | (empty) |
| 16 | 2025-02-23 | 0 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | (empty) |
| 17 | 2025-02-24 | 0 | 2411.52 | 1611.52 | 2126.95 | 2461.86 | 0 | (empty) |
| 18 | 2025-02-25 | -59.04 | 2352.48 | 1552.48 | 2067.91 | 2402.82 | 0 | event_677 |
| 19 | 2025-02-26 | -37.49 | 2314.99 | 1514.99 | 2030.42 | 2365.33 | 0 | event_703 |
| 20 | 2025-02-27 | -50.84 | 2264.15 | 1464.15 | 1979.58 | 2340.83 | 0 | event_716 |
| 21 | 2025-02-28 | 0 | 2264.15 | 1464.15 | 1979.58 | 2340.83 | 0 | (empty) |
| 22 | 2025-03-01 | -467.5 | 1796.65 | 996.65 | 1512.08 | 1873.33 | 0 | event_650 |
| 23 | 2025-03-02 | 0 | 1796.65 | 996.65 | 1512.08 | 1873.33 | 0 | (empty) |
| 24 | 2025-03-03 | 0 | 1796.65 | 996.65 | 1512.08 | 1873.33 | 0 | (empty) |
| 25 | 2025-03-04 | -59.04 | 1737.61 | 937.61 | 1453.04 | 1814.29 | 0 | event_677 |
| 26 | 2025-03-05 | -114.32 | 1623.29 | 823.29 | 1338.72 | 1699.97 | 0 | event_703, event_651 |
| 27 | 2025-03-06 | 0 | 1623.29 | 823.29 | 1338.72 | 1699.97 | 0 | (empty) |
| 28 | 2025-03-07 | -89 | 1534.29 | 734.29 | 1249.72 | 1610.97 | 0 | event_646 |
| 29 | 2025-03-08 | 0 | 1534.29 | 734.29 | 1249.72 | 1610.97 | 0 | (empty) |
| 30 | 2025-03-09 | 0 | 1534.29 | 734.29 | 1249.72 | 1610.97 | 0 | (empty) |
| 31 | 2025-03-10 | -191 | 1343.29 | 543.29 | 1058.72 | 1419.97 | 0 | event_648, event_647 |
| 32 | 2025-03-11 | -59.04 | 1284.25 | 484.25 | 999.68 | 1360.93 | 0 | event_677 |
| 33 | 2025-03-12 | -61.49 | 1222.76 | 422.76 | 938.19 | 1323.44 | 0 | event_649, event_703 |
| 34 | 2025-03-13 | -50.84 | 1171.92 | 371.92 | 887.35 | 1298.94 | 0 | event_716 |
| 35 | 2025-03-14 | 0 | 1171.92 | 371.92 | 887.35 | 1298.94 | 0 | (empty) |
| 36 | 2025-03-15 | 1422.85 | 2594.77 | 1794.77 | 2310.2 | 2721.79 | 0 | event_643 |
| 37 | 2025-03-16 | 0 | 2594.77 | 1794.77 | 2310.2 | 2721.79 | 0 | (empty) |
| 38 | 2025-03-17 | 0 | 2594.77 | 1794.77 | 2310.2 | 2721.79 | 0 | (empty) |
| 39 | 2025-03-18 | -59.04 | 2535.73 | 1735.73 | 2251.16 | 2662.75 | 0 | event_677 |
| 40 | 2025-03-19 | -37.49 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | event_703 |
| 41 | 2025-03-20 | 0 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | (empty) |
| 42 | 2025-03-21 | 0 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | (empty) |
| 43 | 2025-03-22 | 0 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | (empty) |
| 44 | 2025-03-23 | 0 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | (empty) |
| 45 | 2025-03-24 | 0 | 2498.24 | 1698.24 | 2213.67 | 2625.26 | 0 | (empty) |
| 46 | 2025-03-25 | -59.04 | 2439.2 | 1639.2 | 2154.63 | 2566.22 | 0 | event_677 |
| 47 | 2025-03-26 | -37.49 | 2401.71 | 1601.71 | 2117.14 | 2528.73 | 0 | event_703 |
| 48 | 2025-03-27 | -50.84 | 2350.87 | 1550.87 | 2066.3 | 2504.23 | 0 | event_716 |
| 49 | 2025-03-28 | 0 | 2350.87 | 1550.87 | 2066.3 | 2504.23 | 0 | (empty) |
| 50 | 2025-03-29 | 0 | 2350.87 | 1550.87 | 2066.3 | 2504.23 | 0 | (empty) |
| 51 | 2025-03-30 | 0 | 2350.87 | 1550.87 | 2066.3 | 2504.23 | 0 | (empty) |
| 52 | 2025-03-31 | 0 | 2350.87 | 1550.87 | 2066.3 | 2504.23 | 0 | (empty) |
| 53 | 2025-04-01 | -526.54 | 1824.33 | 1024.33 | 1539.76 | 1977.69 | 0 | event_677, event_650 |
| 54 | 2025-04-02 | -37.49 | 1786.84 | 986.84 | 1502.27 | 1940.2 | 0 | event_703 |
| 55 | 2025-04-03 | 0 | 1786.84 | 986.84 | 1502.27 | 1940.2 | 0 | (empty) |
| 56 | 2025-04-04 | 0 | 1786.84 | 986.84 | 1502.27 | 1940.2 | 0 | (empty) |
| 57 | 2025-04-05 | -76.83 | 1710.01 | 910.01 | 1425.44 | 1863.37 | 0 | event_651 |
| 58 | 2025-04-06 | 0 | 1710.01 | 910.01 | 1425.44 | 1863.37 | 0 | (empty) |
| 59 | 2025-04-07 | -89 | 1621.01 | 821.01 | 1336.44 | 1774.37 | 0 | event_646 |
| 60 | 2025-04-08 | -59.04 | 1561.97 | 761.97 | 1277.4 | 1715.33 | 0 | event_677 |
| 61 | 2025-04-09 | -37.49 | 1524.48 | 724.48 | 1239.91 | 1677.84 | 0 | event_703 |
| 62 | 2025-04-10 | -241.84 | 1282.64 | 482.64 | 998.07 | 1462.34 | 0 | event_648, event_716, event_647 |
| 63 | 2025-04-11 | 0 | 1282.64 | 482.64 | 998.07 | 1462.34 | 0 | (empty) |
| 64 | 2025-04-12 | -24 | 1258.64 | 458.64 | 974.07 | 1462.34 | 0 | event_649 |
| 65 | 2025-04-13 | 0 | 1258.64 | 458.64 | 974.07 | 1462.34 | 0 | (empty) |
| 66 | 2025-04-14 | 0 | 1258.64 | 458.64 | 974.07 | 1462.34 | 0 | (empty) |
| 67 | 2025-04-15 | 1363.81 | 2622.45 | 1822.45 | 2337.88 | 1829.55 | 996.6 | event_643, event_677 |
| 68 | 2025-04-16 | -37.49 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | event_703 |
| 69 | 2025-04-17 | 0 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | (empty) |
| 70 | 2025-04-18 | 0 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | (empty) |
| 71 | 2025-04-19 | 0 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | (empty) |
| 72 | 2025-04-20 | 0 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | (empty) |
| 73 | 2025-04-21 | 0 | 2584.96 | 1784.96 | 2300.39 | 1792.06 | 0 | (empty) |
| 74 | 2025-04-22 | -59.04 | 2525.92 | 1725.92 | 2241.35 | 1733.02 | 0 | event_677 |
| 75 | 2025-04-23 | -37.49 | 2488.43 | 1688.43 | 2203.86 | 1695.53 | 0 | event_703 |
| 76 | 2025-04-24 | -50.84 | 2437.59 | 1637.59 | 2153.02 | 1671.03 | 0 | event_716 |
| 77 | 2025-04-25 | 0 | 2437.59 | 1637.59 | 2153.02 | 1671.03 | 0 | (empty) |
| 78 | 2025-04-26 | 0 | 2437.59 | 1637.59 | 2153.02 | 1671.03 | 0 | (empty) |
| 79 | 2025-04-27 | 0 | 2437.59 | 1637.59 | 2153.02 | 1671.03 | 0 | (empty) |
| 80 | 2025-04-28 | 0 | 2437.59 | 1637.59 | 2153.02 | 1671.03 | 0 | (empty) |
| 81 | 2025-04-29 | -59.04 | 2378.55 | 1578.55 | 2093.98 | 1611.99 | 0 | event_677 |
| 82 | 2025-04-30 | -37.49 | 2341.06 | 1541.06 | 2056.49 | 1574.5 | 0 | event_703 |
| 83 | 2025-05-01 | -467.5 | 1873.56 | 1073.56 | 1588.99 | 1107 | 0 | event_650 |
| 84 | 2025-05-02 | 0 | 1873.56 | 1073.56 | 1588.99 | 1107 | 0 | (empty) |
| 85 | 2025-05-03 | 0 | 1873.56 | 1073.56 | 1588.99 | 1107 | 0 | (empty) |
| 86 | 2025-05-04 | 0 | 1873.56 | 1073.56 | 1588.99 | 1107 | 0 | (empty) |
| 87 | 2025-05-05 | -76.83 | 1796.73 | 996.73 | 1512.16 | 1030.17 | 0 | event_651 |
| 88 | 2025-05-06 | -59.04 | 1737.69 | 937.69 | 1453.12 | 971.13 | 0 | event_677 |
| 89 | 2025-05-07 | -126.49 | 1611.2 | 811.2 | 1326.63 | 844.64 | 0 | event_703, event_646 |
| 90 | 2025-05-08 | -50.84 | 1560.36 | 760.36 | 1275.79 | 820.14 | 0 | event_716 |

## request_09 â€” user_09 (EUR)

Request: 166.61 on 2026-07-04; deadline 2026-07-23. Opening 2231.1; minimum 600.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 166.61 | 151.96 | NO |
| affordability_status | affordable_now | not_affordable | NO |
| recommended_payment_method | full_payment | not_recommended | NO |
| payment_plan | 2026-07-04:166.61 | none | NO |
| earliest_date_for_full_payment | 2026-07-04 | (empty) | NO |
| spending_changes_needed | none | none | yes |

Baseline trough: day 90 (2026-10-02), balance 751.96, headroom 151.96.

Protected: rent|utilities|groceries. Reduce: . Stop: .

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_749 | cloud_storage / Cloud storage plan | 5 / 5 | 5 | 5.00 | 5â€“5 | 5 | 2026-07-12, 2026-08-12, 2026-09-12 |
| event_770 | groceries / Bulk pantry shop | 18 / 6 | 44.56722222222222222222222222 | 46.965 | 31.82â€“54.9 | 44.57 | 2026-07-07, 2026-07-17, 2026-07-27, 2026-08-06, 2026-08-16, 2026-08-26, 2026-09-05, 2026-09-15, 2026-09-25 |
| event_752 | rent / Monthly rent | 6 / 6 | 211.2 | 211.20 | 211.2â€“211.2 | 211.2 | 2026-08-02, 2026-09-02, 2026-10-02 |
| event_751 | shopping / Household shopping | 5 / 5 | 26.632 | 25.52 | 24.68â€“29.14 | 26.63 | 2026-07-12, 2026-08-12, 2026-09-12 |
| event_750 | streaming / Video streaming plan | 5 / 5 | 20 | 20.00 | 20â€“20 | 20 | 2026-07-09, 2026-08-09, 2026-09-09 |
| event_779 | transport / Commuter pass | 9 / 6 | 24.11444444444444444444444444 | 24.59 | 16.59â€“28.34 | 24.11 | 2026-07-17, 2026-08-07, 2026-08-28, 2026-09-18 |
| event_748 | utilities / Water and power payment | 5 / 5 | 64.362 | 63.66 | 59.39â€“71.04 | 64.36 | 2026-07-06, 2026-08-06, 2026-09-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-07-06 | -64.36 | event_748 | utilities | recurring_expense | Water and power payment |
| 2026-07-07 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-07-09 | -20 | event_750 | streaming | recurring_expense | Video streaming plan |
| 2026-07-12 | -5 | event_749 | cloud_storage | recurring_expense | Cloud storage plan |
| 2026-07-12 | -26.63 | event_751 | shopping | recurring_expense | Household shopping |
| 2026-07-17 | -24.11 | event_779 | transport | recurring_expense | Commuter pass |
| 2026-07-17 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-07-27 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-08-02 | -211.2 | event_752 | rent | recurring_expense | Monthly rent |
| 2026-08-06 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-08-06 | -64.36 | event_748 | utilities | recurring_expense | Water and power payment |
| 2026-08-07 | -24.11 | event_779 | transport | recurring_expense | Commuter pass |
| 2026-08-09 | -20 | event_750 | streaming | recurring_expense | Video streaming plan |
| 2026-08-12 | -5 | event_749 | cloud_storage | recurring_expense | Cloud storage plan |
| 2026-08-12 | -26.63 | event_751 | shopping | recurring_expense | Household shopping |
| 2026-08-16 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-08-26 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-08-28 | -24.11 | event_779 | transport | recurring_expense | Commuter pass |
| 2026-09-02 | -211.2 | event_752 | rent | recurring_expense | Monthly rent |
| 2026-09-05 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-09-06 | -64.36 | event_748 | utilities | recurring_expense | Water and power payment |
| 2026-09-09 | -20 | event_750 | streaming | recurring_expense | Video streaming plan |
| 2026-09-12 | -5 | event_749 | cloud_storage | recurring_expense | Cloud storage plan |
| 2026-09-12 | -26.63 | event_751 | shopping | recurring_expense | Household shopping |
| 2026-09-15 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-09-18 | -24.11 | event_779 | transport | recurring_expense | Commuter pass |
| 2026-09-25 | -44.57 | event_770 | groceries | recurring_expense | Bulk pantry shop |
| 2026-10-02 | -211.2 | event_752 | rent | recurring_expense | Monthly rent |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-07-04 | 0 | 2231.1 | 1631.1 | 2064.49 | 2231.1 | 0 | (empty) |
| 1 | 2026-07-05 | 0 | 2231.1 | 1631.1 | 2064.49 | 2231.1 | 0 | (empty) |
| 2 | 2026-07-06 | -64.36 | 2166.74 | 1566.74 | 2000.13 | 2166.74 | 0 | event_748 |
| 3 | 2026-07-07 | -44.57 | 2122.17 | 1522.17 | 1955.56 | 2122.17 | 0 | event_770 |
| 4 | 2026-07-08 | 0 | 2122.17 | 1522.17 | 1955.56 | 2122.17 | 0 | (empty) |
| 5 | 2026-07-09 | -20 | 2102.17 | 1502.17 | 1935.56 | 2102.17 | 0 | event_750 |
| 6 | 2026-07-10 | 0 | 2102.17 | 1502.17 | 1935.56 | 2102.17 | 0 | (empty) |
| 7 | 2026-07-11 | 0 | 2102.17 | 1502.17 | 1935.56 | 2102.17 | 0 | (empty) |
| 8 | 2026-07-12 | -31.63 | 2070.54 | 1470.54 | 1903.93 | 2070.54 | 0 | event_749, event_751 |
| 9 | 2026-07-13 | 0 | 2070.54 | 1470.54 | 1903.93 | 2070.54 | 0 | (empty) |
| 10 | 2026-07-14 | 0 | 2070.54 | 1470.54 | 1903.93 | 2070.54 | 0 | (empty) |
| 11 | 2026-07-15 | 0 | 2070.54 | 1470.54 | 1903.93 | 2070.54 | 0 | (empty) |
| 12 | 2026-07-16 | 0 | 2070.54 | 1470.54 | 1903.93 | 2070.54 | 0 | (empty) |
| 13 | 2026-07-17 | -68.68 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | event_779, event_770 |
| 14 | 2026-07-18 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 15 | 2026-07-19 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 16 | 2026-07-20 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 17 | 2026-07-21 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 18 | 2026-07-22 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 19 | 2026-07-23 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 20 | 2026-07-24 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 21 | 2026-07-25 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 22 | 2026-07-26 | 0 | 2001.86 | 1401.86 | 1835.25 | 2001.86 | 0 | (empty) |
| 23 | 2026-07-27 | -44.57 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | event_770 |
| 24 | 2026-07-28 | 0 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | (empty) |
| 25 | 2026-07-29 | 0 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | (empty) |
| 26 | 2026-07-30 | 0 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | (empty) |
| 27 | 2026-07-31 | 0 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | (empty) |
| 28 | 2026-08-01 | 0 | 1957.29 | 1357.29 | 1790.68 | 1957.29 | 0 | (empty) |
| 29 | 2026-08-02 | -211.2 | 1746.09 | 1146.09 | 1579.48 | 1746.09 | 0 | event_752 |
| 30 | 2026-08-03 | 0 | 1746.09 | 1146.09 | 1579.48 | 1746.09 | 0 | (empty) |
| 31 | 2026-08-04 | 0 | 1746.09 | 1146.09 | 1579.48 | 1746.09 | 0 | (empty) |
| 32 | 2026-08-05 | 0 | 1746.09 | 1146.09 | 1579.48 | 1746.09 | 0 | (empty) |
| 33 | 2026-08-06 | -108.93 | 1637.16 | 1037.16 | 1470.55 | 1637.16 | 0 | event_770, event_748 |
| 34 | 2026-08-07 | -24.11 | 1613.05 | 1013.05 | 1446.44 | 1613.05 | 0 | event_779 |
| 35 | 2026-08-08 | 0 | 1613.05 | 1013.05 | 1446.44 | 1613.05 | 0 | (empty) |
| 36 | 2026-08-09 | -20 | 1593.05 | 993.05 | 1426.44 | 1593.05 | 0 | event_750 |
| 37 | 2026-08-10 | 0 | 1593.05 | 993.05 | 1426.44 | 1593.05 | 0 | (empty) |
| 38 | 2026-08-11 | 0 | 1593.05 | 993.05 | 1426.44 | 1593.05 | 0 | (empty) |
| 39 | 2026-08-12 | -31.63 | 1561.42 | 961.42 | 1394.81 | 1561.42 | 0 | event_749, event_751 |
| 40 | 2026-08-13 | 0 | 1561.42 | 961.42 | 1394.81 | 1561.42 | 0 | (empty) |
| 41 | 2026-08-14 | 0 | 1561.42 | 961.42 | 1394.81 | 1561.42 | 0 | (empty) |
| 42 | 2026-08-15 | 0 | 1561.42 | 961.42 | 1394.81 | 1561.42 | 0 | (empty) |
| 43 | 2026-08-16 | -44.57 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | event_770 |
| 44 | 2026-08-17 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 45 | 2026-08-18 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 46 | 2026-08-19 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 47 | 2026-08-20 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 48 | 2026-08-21 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 49 | 2026-08-22 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 50 | 2026-08-23 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 51 | 2026-08-24 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 52 | 2026-08-25 | 0 | 1516.85 | 916.85 | 1350.24 | 1516.85 | 0 | (empty) |
| 53 | 2026-08-26 | -44.57 | 1472.28 | 872.28 | 1305.67 | 1472.28 | 0 | event_770 |
| 54 | 2026-08-27 | 0 | 1472.28 | 872.28 | 1305.67 | 1472.28 | 0 | (empty) |
| 55 | 2026-08-28 | -24.11 | 1448.17 | 848.17 | 1281.56 | 1448.17 | 0 | event_779 |
| 56 | 2026-08-29 | 0 | 1448.17 | 848.17 | 1281.56 | 1448.17 | 0 | (empty) |
| 57 | 2026-08-30 | 0 | 1448.17 | 848.17 | 1281.56 | 1448.17 | 0 | (empty) |
| 58 | 2026-08-31 | 0 | 1448.17 | 848.17 | 1281.56 | 1448.17 | 0 | (empty) |
| 59 | 2026-09-01 | 0 | 1448.17 | 848.17 | 1281.56 | 1448.17 | 0 | (empty) |
| 60 | 2026-09-02 | -211.2 | 1236.97 | 636.97 | 1070.36 | 1236.97 | 0 | event_752 |
| 61 | 2026-09-03 | 0 | 1236.97 | 636.97 | 1070.36 | 1236.97 | 0 | (empty) |
| 62 | 2026-09-04 | 0 | 1236.97 | 636.97 | 1070.36 | 1236.97 | 0 | (empty) |
| 63 | 2026-09-05 | -44.57 | 1192.4 | 592.4 | 1025.79 | 1192.4 | 0 | event_770 |
| 64 | 2026-09-06 | -64.36 | 1128.04 | 528.04 | 961.43 | 1128.04 | 0 | event_748 |
| 65 | 2026-09-07 | 0 | 1128.04 | 528.04 | 961.43 | 1128.04 | 0 | (empty) |
| 66 | 2026-09-08 | 0 | 1128.04 | 528.04 | 961.43 | 1128.04 | 0 | (empty) |
| 67 | 2026-09-09 | -20 | 1108.04 | 508.04 | 941.43 | 1108.04 | 0 | event_750 |
| 68 | 2026-09-10 | 0 | 1108.04 | 508.04 | 941.43 | 1108.04 | 0 | (empty) |
| 69 | 2026-09-11 | 0 | 1108.04 | 508.04 | 941.43 | 1108.04 | 0 | (empty) |
| 70 | 2026-09-12 | -31.63 | 1076.41 | 476.41 | 909.8 | 1076.41 | 0 | event_749, event_751 |
| 71 | 2026-09-13 | 0 | 1076.41 | 476.41 | 909.8 | 1076.41 | 0 | (empty) |
| 72 | 2026-09-14 | 0 | 1076.41 | 476.41 | 909.8 | 1076.41 | 0 | (empty) |
| 73 | 2026-09-15 | -44.57 | 1031.84 | 431.84 | 865.23 | 1031.84 | 0 | event_770 |
| 74 | 2026-09-16 | 0 | 1031.84 | 431.84 | 865.23 | 1031.84 | 0 | (empty) |
| 75 | 2026-09-17 | 0 | 1031.84 | 431.84 | 865.23 | 1031.84 | 0 | (empty) |
| 76 | 2026-09-18 | -24.11 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | event_779 |
| 77 | 2026-09-19 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 78 | 2026-09-20 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 79 | 2026-09-21 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 80 | 2026-09-22 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 81 | 2026-09-23 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 82 | 2026-09-24 | 0 | 1007.73 | 407.73 | 841.12 | 1007.73 | 0 | (empty) |
| 83 | 2026-09-25 | -44.57 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | event_770 |
| 84 | 2026-09-26 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 85 | 2026-09-27 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 86 | 2026-09-28 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 87 | 2026-09-29 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 88 | 2026-09-30 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 89 | 2026-10-01 | 0 | 963.16 | 363.16 | 796.55 | 963.16 | 0 | (empty) |
| 90 | 2026-10-02 | -211.2 | 751.96 | 151.96 | 585.35 | 751.96 | 0 | event_752 |

## request_10 â€” user_10 (INR)

Request: 266700 on 2024-12-06; deadline 2025-02-10. Opening 750155; minimum 225400.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 12700 | 0 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 90 (2025-03-06), balance 178050.78, headroom -47349.22.

Protected: rent|groceries|transport. Reduce: dining|gym|entertainment. Stop: music_subscription|delivery_membership.

Salary mode: unconfirmed_gig. Evidence: message_07. Unparsed messages: none.

- message_07 (service_provider, 2024-11-25T09:30:00Z): Here’s the latest service update from QuickCrew. The next QuickCrew payout is still pending. The weekly earnings shown in the QuickCrew app can change until the payout is closed. The balance isn’t withdrawable until the payout shows as completed. Case ref SER-0007.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_836 | delivery_membership / Delivery service plan | 5 / 5 | 1895 | 1895.00 | 1895â€“1895 | 1895 | 2024-12-14, 2025-01-14, 2025-02-14 |
| event_904 | dining / Takeaway order | 13 / 6 | 8837.768461538461538461538462 | 8813.96 | 6375.03â€“10525.43 | 8837.77 | 2024-12-14, 2024-12-28, 2025-01-11, 2025-01-25, 2025-02-08, 2025-02-22 |
| event_838 | entertainment / Cinema and events | 5 / 5 | 4645.192 | 4700.56 | 4366.61â€“4883.78 | 4645.19 | 2024-12-15, 2025-01-15, 2025-02-15 |
| event_866 | groceries / Weekly produce market | 26 / 7 | 10776.07192307692307692307692 | 10635.76 | 8011.08â€“13621.53 | 10776.07 | 2024-12-12, 2024-12-19, 2024-12-26, 2025-01-02, 2025-01-09, 2025-01-16, 2025-01-23, 2025-01-30, 2025-02-06, 2025-02-13, 2025-02-20, 2025-02-27, 2025-03-06 |
| event_837 | gym / Community fitness plan | 5 / 5 | 4860 | 4860.00 | 4860â€“4860 | 4860 | 2024-12-11, 2025-01-11, 2025-02-11 |
| event_835 | music_subscription / Music subscription | 5 / 5 | 2800 | 2800.00 | 2800â€“2800 | 2800 | 2024-12-12, 2025-01-12, 2025-02-12 |
| event_840 | rent / Monthly rent | 6 / 6 | 69100 | 69100.00 | 69100â€“69100 | 69100 | 2025-01-03, 2025-02-03, 2025-03-03 |
| event_891 | transport / Ride-hailing trip | 25 / 6 | 5982.7904 | 5776.08 | 4356.14â€“7568.88 | 5982.79 | 2024-12-06, 2024-12-13, 2024-12-20, 2024-12-27, 2025-01-03, 2025-01-10, 2025-01-17, 2025-01-24, 2025-01-31, 2025-02-07, 2025-02-14, 2025-02-21, 2025-02-28 |
| event_834 | utilities / Electricity and water bill | 5 / 5 | 17103.95 | 17538.11 | 15236.94â€“19224.83 | 17103.95 | 2024-12-07, 2025-01-07, 2025-02-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-12-06 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2024-12-07 | -17103.95 | event_834 | utilities | recurring_expense | Electricity and water bill |
| 2024-12-11 | -4860 | event_837 | gym | recurring_expense | Community fitness plan |
| 2024-12-12 | -2800 | event_835 | music_subscription | recurring_expense | Music subscription |
| 2024-12-12 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2024-12-13 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2024-12-14 | -1895 | event_836 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-12-14 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2024-12-15 | -4645.19 | event_838 | entertainment | recurring_expense | Cinema and events |
| 2024-12-19 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2024-12-20 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2024-12-26 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2024-12-27 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2024-12-28 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2025-01-02 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-01-03 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-01-03 | -69100 | event_840 | rent | recurring_expense | Monthly rent |
| 2025-01-07 | -17103.95 | event_834 | utilities | recurring_expense | Electricity and water bill |
| 2025-01-09 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-01-10 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-01-11 | -4860 | event_837 | gym | recurring_expense | Community fitness plan |
| 2025-01-11 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2025-01-12 | -2800 | event_835 | music_subscription | recurring_expense | Music subscription |
| 2025-01-14 | -1895 | event_836 | delivery_membership | recurring_expense | Delivery service plan |
| 2025-01-15 | -4645.19 | event_838 | entertainment | recurring_expense | Cinema and events |
| 2025-01-16 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-01-17 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-01-23 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-01-24 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-01-25 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2025-01-30 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-01-31 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-02-03 | -69100 | event_840 | rent | recurring_expense | Monthly rent |
| 2025-02-06 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-02-07 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-02-07 | -17103.95 | event_834 | utilities | recurring_expense | Electricity and water bill |
| 2025-02-08 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2025-02-11 | -4860 | event_837 | gym | recurring_expense | Community fitness plan |
| 2025-02-12 | -2800 | event_835 | music_subscription | recurring_expense | Music subscription |
| 2025-02-13 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-02-14 | -1895 | event_836 | delivery_membership | recurring_expense | Delivery service plan |
| 2025-02-14 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-02-15 | -4645.19 | event_838 | entertainment | recurring_expense | Cinema and events |
| 2025-02-20 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-02-21 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-02-22 | -8837.77 | event_904 | dining | recurring_expense | Takeaway order |
| 2025-02-27 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |
| 2025-02-28 | -5982.79 | event_891 | transport | recurring_expense | Ride-hailing trip |
| 2025-03-03 | -69100 | event_840 | rent | recurring_expense | Monthly rent |
| 2025-03-06 | -10776.07 | event_866 | groceries | recurring_expense | Weekly produce market |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-12-06 | -5982.79 | 744172.21 | 518772.21 | 731472.21 | 744172.21 | 0 | event_891 |
| 1 | 2024-12-07 | -17103.95 | 727068.26 | 501668.26 | 714368.26 | 727068.26 | 0 | event_834 |
| 2 | 2024-12-08 | 0 | 727068.26 | 501668.26 | 714368.26 | 727068.26 | 0 | (empty) |
| 3 | 2024-12-09 | 0 | 727068.26 | 501668.26 | 714368.26 | 727068.26 | 0 | (empty) |
| 4 | 2024-12-10 | 0 | 727068.26 | 501668.26 | 714368.26 | 727068.26 | 0 | (empty) |
| 5 | 2024-12-11 | -4860 | 722208.26 | 496808.26 | 709508.26 | 722208.26 | 0 | event_837 |
| 6 | 2024-12-12 | -13576.07 | 708632.19 | 483232.19 | 695932.19 | 708632.19 | 0 | event_835, event_866 |
| 7 | 2024-12-13 | -5982.79 | 702649.4 | 477249.4 | 689949.4 | 702649.4 | 0 | event_891 |
| 8 | 2024-12-14 | -10732.77 | 691916.63 | 466516.63 | 679216.63 | 691916.63 | 0 | event_836, event_904 |
| 9 | 2024-12-15 | -4645.19 | 687271.44 | 461871.44 | 674571.44 | 687271.44 | 0 | event_838 |
| 10 | 2024-12-16 | 0 | 687271.44 | 461871.44 | 674571.44 | 687271.44 | 0 | (empty) |
| 11 | 2024-12-17 | 0 | 687271.44 | 461871.44 | 674571.44 | 687271.44 | 0 | (empty) |
| 12 | 2024-12-18 | 0 | 687271.44 | 461871.44 | 674571.44 | 687271.44 | 0 | (empty) |
| 13 | 2024-12-19 | -10776.07 | 676495.37 | 451095.37 | 663795.37 | 676495.37 | 0 | event_866 |
| 14 | 2024-12-20 | -5982.79 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | event_891 |
| 15 | 2024-12-21 | 0 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | (empty) |
| 16 | 2024-12-22 | 0 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | (empty) |
| 17 | 2024-12-23 | 0 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | (empty) |
| 18 | 2024-12-24 | 0 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | (empty) |
| 19 | 2024-12-25 | 0 | 670512.58 | 445112.58 | 657812.58 | 670512.58 | 0 | (empty) |
| 20 | 2024-12-26 | -10776.07 | 659736.51 | 434336.51 | 647036.51 | 659736.51 | 0 | event_866 |
| 21 | 2024-12-27 | -5982.79 | 653753.72 | 428353.72 | 641053.72 | 653753.72 | 0 | event_891 |
| 22 | 2024-12-28 | -8837.77 | 644915.95 | 419515.95 | 632215.95 | 644915.95 | 0 | event_904 |
| 23 | 2024-12-29 | 0 | 644915.95 | 419515.95 | 632215.95 | 644915.95 | 0 | (empty) |
| 24 | 2024-12-30 | 0 | 644915.95 | 419515.95 | 632215.95 | 644915.95 | 0 | (empty) |
| 25 | 2024-12-31 | 0 | 644915.95 | 419515.95 | 632215.95 | 644915.95 | 0 | (empty) |
| 26 | 2025-01-01 | 0 | 644915.95 | 419515.95 | 632215.95 | 644915.95 | 0 | (empty) |
| 27 | 2025-01-02 | -10776.07 | 634139.88 | 408739.88 | 621439.88 | 634139.88 | 0 | event_866 |
| 28 | 2025-01-03 | -75082.79 | 559057.09 | 333657.09 | 546357.09 | 559057.09 | 0 | event_891, event_840 |
| 29 | 2025-01-04 | 0 | 559057.09 | 333657.09 | 546357.09 | 559057.09 | 0 | (empty) |
| 30 | 2025-01-05 | 0 | 559057.09 | 333657.09 | 546357.09 | 559057.09 | 0 | (empty) |
| 31 | 2025-01-06 | 0 | 559057.09 | 333657.09 | 546357.09 | 559057.09 | 0 | (empty) |
| 32 | 2025-01-07 | -17103.95 | 541953.14 | 316553.14 | 529253.14 | 541953.14 | 0 | event_834 |
| 33 | 2025-01-08 | 0 | 541953.14 | 316553.14 | 529253.14 | 541953.14 | 0 | (empty) |
| 34 | 2025-01-09 | -10776.07 | 531177.07 | 305777.07 | 518477.07 | 531177.07 | 0 | event_866 |
| 35 | 2025-01-10 | -5982.79 | 525194.28 | 299794.28 | 512494.28 | 525194.28 | 0 | event_891 |
| 36 | 2025-01-11 | -13697.77 | 511496.51 | 286096.51 | 498796.51 | 511496.51 | 0 | event_837, event_904 |
| 37 | 2025-01-12 | -2800 | 508696.51 | 283296.51 | 495996.51 | 508696.51 | 0 | event_835 |
| 38 | 2025-01-13 | 0 | 508696.51 | 283296.51 | 495996.51 | 508696.51 | 0 | (empty) |
| 39 | 2025-01-14 | -1895 | 506801.51 | 281401.51 | 494101.51 | 506801.51 | 0 | event_836 |
| 40 | 2025-01-15 | -4645.19 | 502156.32 | 276756.32 | 489456.32 | 502156.32 | 0 | event_838 |
| 41 | 2025-01-16 | -10776.07 | 491380.25 | 265980.25 | 478680.25 | 491380.25 | 0 | event_866 |
| 42 | 2025-01-17 | -5982.79 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | event_891 |
| 43 | 2025-01-18 | 0 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | (empty) |
| 44 | 2025-01-19 | 0 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | (empty) |
| 45 | 2025-01-20 | 0 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | (empty) |
| 46 | 2025-01-21 | 0 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | (empty) |
| 47 | 2025-01-22 | 0 | 485397.46 | 259997.46 | 472697.46 | 485397.46 | 0 | (empty) |
| 48 | 2025-01-23 | -10776.07 | 474621.39 | 249221.39 | 461921.39 | 474621.39 | 0 | event_866 |
| 49 | 2025-01-24 | -5982.79 | 468638.6 | 243238.6 | 455938.6 | 468638.6 | 0 | event_891 |
| 50 | 2025-01-25 | -8837.77 | 459800.83 | 234400.83 | 447100.83 | 459800.83 | 0 | event_904 |
| 51 | 2025-01-26 | 0 | 459800.83 | 234400.83 | 447100.83 | 459800.83 | 0 | (empty) |
| 52 | 2025-01-27 | 0 | 459800.83 | 234400.83 | 447100.83 | 459800.83 | 0 | (empty) |
| 53 | 2025-01-28 | 0 | 459800.83 | 234400.83 | 447100.83 | 459800.83 | 0 | (empty) |
| 54 | 2025-01-29 | 0 | 459800.83 | 234400.83 | 447100.83 | 459800.83 | 0 | (empty) |
| 55 | 2025-01-30 | -10776.07 | 449024.76 | 223624.76 | 436324.76 | 449024.76 | 0 | event_866 |
| 56 | 2025-01-31 | -5982.79 | 443041.97 | 217641.97 | 430341.97 | 443041.97 | 0 | event_891 |
| 57 | 2025-02-01 | 0 | 443041.97 | 217641.97 | 430341.97 | 443041.97 | 0 | (empty) |
| 58 | 2025-02-02 | 0 | 443041.97 | 217641.97 | 430341.97 | 443041.97 | 0 | (empty) |
| 59 | 2025-02-03 | -69100 | 373941.97 | 148541.97 | 361241.97 | 373941.97 | 0 | event_840 |
| 60 | 2025-02-04 | 0 | 373941.97 | 148541.97 | 361241.97 | 373941.97 | 0 | (empty) |
| 61 | 2025-02-05 | 0 | 373941.97 | 148541.97 | 361241.97 | 373941.97 | 0 | (empty) |
| 62 | 2025-02-06 | -10776.07 | 363165.9 | 137765.9 | 350465.9 | 363165.9 | 0 | event_866 |
| 63 | 2025-02-07 | -23086.74 | 340079.16 | 114679.16 | 327379.16 | 340079.16 | 0 | event_891, event_834 |
| 64 | 2025-02-08 | -8837.77 | 331241.39 | 105841.39 | 318541.39 | 331241.39 | 0 | event_904 |
| 65 | 2025-02-09 | 0 | 331241.39 | 105841.39 | 318541.39 | 331241.39 | 0 | (empty) |
| 66 | 2025-02-10 | 0 | 331241.39 | 105841.39 | 318541.39 | 331241.39 | 0 | (empty) |
| 67 | 2025-02-11 | -4860 | 326381.39 | 100981.39 | 313681.39 | 326381.39 | 0 | event_837 |
| 68 | 2025-02-12 | -2800 | 323581.39 | 98181.39 | 310881.39 | 323581.39 | 0 | event_835 |
| 69 | 2025-02-13 | -10776.07 | 312805.32 | 87405.32 | 300105.32 | 312805.32 | 0 | event_866 |
| 70 | 2025-02-14 | -7877.79 | 304927.53 | 79527.53 | 292227.53 | 304927.53 | 0 | event_836, event_891 |
| 71 | 2025-02-15 | -4645.19 | 300282.34 | 74882.34 | 287582.34 | 300282.34 | 0 | event_838 |
| 72 | 2025-02-16 | 0 | 300282.34 | 74882.34 | 287582.34 | 300282.34 | 0 | (empty) |
| 73 | 2025-02-17 | 0 | 300282.34 | 74882.34 | 287582.34 | 300282.34 | 0 | (empty) |
| 74 | 2025-02-18 | 0 | 300282.34 | 74882.34 | 287582.34 | 300282.34 | 0 | (empty) |
| 75 | 2025-02-19 | 0 | 300282.34 | 74882.34 | 287582.34 | 300282.34 | 0 | (empty) |
| 76 | 2025-02-20 | -10776.07 | 289506.27 | 64106.27 | 276806.27 | 289506.27 | 0 | event_866 |
| 77 | 2025-02-21 | -5982.79 | 283523.48 | 58123.48 | 270823.48 | 283523.48 | 0 | event_891 |
| 78 | 2025-02-22 | -8837.77 | 274685.71 | 49285.71 | 261985.71 | 274685.71 | 0 | event_904 |
| 79 | 2025-02-23 | 0 | 274685.71 | 49285.71 | 261985.71 | 274685.71 | 0 | (empty) |
| 80 | 2025-02-24 | 0 | 274685.71 | 49285.71 | 261985.71 | 274685.71 | 0 | (empty) |
| 81 | 2025-02-25 | 0 | 274685.71 | 49285.71 | 261985.71 | 274685.71 | 0 | (empty) |
| 82 | 2025-02-26 | 0 | 274685.71 | 49285.71 | 261985.71 | 274685.71 | 0 | (empty) |
| 83 | 2025-02-27 | -10776.07 | 263909.64 | 38509.64 | 251209.64 | 263909.64 | 0 | event_866 |
| 84 | 2025-02-28 | -5982.79 | 257926.85 | 32526.85 | 245226.85 | 257926.85 | 0 | event_891 |
| 85 | 2025-03-01 | 0 | 257926.85 | 32526.85 | 245226.85 | 257926.85 | 0 | (empty) |
| 86 | 2025-03-02 | 0 | 257926.85 | 32526.85 | 245226.85 | 257926.85 | 0 | (empty) |
| 87 | 2025-03-03 | -69100 | 188826.85 | -36573.15 | 176126.85 | 188826.85 | 0 | event_840 |
| 88 | 2025-03-04 | 0 | 188826.85 | -36573.15 | 176126.85 | 188826.85 | 0 | (empty) |
| 89 | 2025-03-05 | 0 | 188826.85 | -36573.15 | 176126.85 | 188826.85 | 0 | (empty) |
| 90 | 2025-03-06 | -10776.07 | 178050.78 | -47349.22 | 165350.78 | 178050.78 | 0 | event_866 |

## request_11 â€” user_11 (IDR)

Request: 13110000 on 2025-05-03; deadline 2025-06-12. Opening 63531795; minimum 34140600.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 12510645 | 12319866.62 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | full_payment | full_payment | yes |
| payment_plan | 2025-05-03:13110000 | 2025-05-03:13110000 | yes |
| earliest_date_for_full_payment | 2025-07-15 | 2025-06-15 | NO |
| spending_changes_needed | reduce_to:event_989:665950 | stop:event_949\|reduce_to:event_989:665950 | NO |

Baseline trough: day 11 (2025-05-14), balance 46460466.62, headroom 12319866.62.

Protected: housing|utilities|education. Reduce: dining|entertainment. Stop: cloud_storage.

Salary mode: base_only. Evidence: message_08. Unparsed messages: none.

- message_08 (employer, 2025-04-22T09:30:00Z): Berikut informasi penggajian terbaru dari Greenfield Foods. Gaji pokok yang dikonfirmasi adalah IDR 38760000. Komisi dari transaksi yang masih berjalan belum disetujui. Transaksi yang masih berjalan tidak masuk pembayaran sampai komisinya dinyatakan diperoleh. Ref payroll EMP-0008.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_949 | cloud_storage / Cloud storage plan | 5 / 5 | 168150 | 168150.00 | 168150â€“168150 | 168150 | 2025-05-14, 2025-06-14, 2025-07-14 |
| event_989 | dining / Weekend food delivery | 9 / 6 | 1350022.547777777777777777778 | 1365643.70 | 1018758.07â€“1697463.1 | 1350022.55 | 2025-05-14, 2025-06-04, 2025-06-25, 2025-07-16 |
| event_946 | education / Child education fee | 5 / 5 | 2544100 | 2544100.00 | 2544100â€“2544100 | 2544100 | 2025-05-10, 2025-06-10, 2025-07-10 |
| event_948 | entertainment / Games and recreation | 5 / 5 | 1600926.754 | 1649906.50 | 1404572.9â€“1688239.04 | 1600926.75 | 2025-05-16, 2025-06-16, 2025-07-16 |
| event_967 | groceries / Fresh food shop | 18 / 6 | 1421333.161666666666666666667 | 1400963.33 | 1053064.17â€“1763208.29 | 1421333.16 | 2025-05-08, 2025-05-18, 2025-05-28, 2025-06-07, 2025-06-17, 2025-06-27, 2025-07-07, 2025-07-17, 2025-07-27 |
| event_947 | healthcare / Regular medicine purchase | 5 / 5 | 2943993.422 | 2973572.96 | 2635764.61â€“3165638.3 | 2943993.42 | 2025-05-12, 2025-06-12, 2025-07-12 |
| event_943 | housing / Home association fee | 5 / 5 | 2954500 | 2954500.00 | 2954500â€“2954500 | 2954500 | 2025-05-05, 2025-06-05, 2025-07-05 |
| event_945 | insurance / Vehicle insurance premium | 5 / 5 | 1881000 | 1881000.00 | 1881000â€“1881000 | 1881000 | 2025-05-09, 2025-06-09, 2025-07-09 |
| event_980 | transport / Vehicle charging | 13 / 6 | 1088014.137692307692307692308 | 1185524.72 | 785218.72â€“1307205.52 | 1088014.14 | 2025-05-11, 2025-05-25, 2025-06-08, 2025-06-22, 2025-07-06, 2025-07-20 |
| event_944 | utilities / Municipal utilities | 5 / 5 | 2720215.108 | 2796165.18 | 2488665.63â€“2916312.61 | 2720215.11 | 2025-05-08, 2025-06-08, 2025-07-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-05-05 | -2954500 | event_943 | housing | recurring_expense | Home association fee |
| 2025-05-08 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-05-08 | -2720215.11 | event_944 | utilities | recurring_expense | Municipal utilities |
| 2025-05-09 | -1881000 | event_945 | insurance | recurring_expense | Vehicle insurance premium |
| 2025-05-10 | -2544100 | event_946 | education | recurring_expense | Child education fee |
| 2025-05-11 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-05-12 | -2943993.42 | event_947 | healthcare | recurring_expense | Regular medicine purchase |
| 2025-05-14 | -168150 | event_949 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-05-14 | -1350022.55 | event_989 | dining | recurring_expense | Weekend food delivery |
| 2025-05-15 | 23256000 | event_941 | salary | recurring_income | Base salary |
| 2025-05-16 | -1600926.75 | event_948 | entertainment | recurring_expense | Games and recreation |
| 2025-05-18 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-05-25 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-05-28 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-06-04 | -1350022.55 | event_989 | dining | recurring_expense | Weekend food delivery |
| 2025-06-05 | -2954500 | event_943 | housing | recurring_expense | Home association fee |
| 2025-06-07 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-06-08 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-06-08 | -2720215.11 | event_944 | utilities | recurring_expense | Municipal utilities |
| 2025-06-09 | -1881000 | event_945 | insurance | recurring_expense | Vehicle insurance premium |
| 2025-06-10 | -2544100 | event_946 | education | recurring_expense | Child education fee |
| 2025-06-12 | -2943993.42 | event_947 | healthcare | recurring_expense | Regular medicine purchase |
| 2025-06-14 | -168150 | event_949 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-06-15 | 23256000 | event_941 | salary | recurring_income | Base salary |
| 2025-06-16 | -1600926.75 | event_948 | entertainment | recurring_expense | Games and recreation |
| 2025-06-17 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-06-22 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-06-25 | -1350022.55 | event_989 | dining | recurring_expense | Weekend food delivery |
| 2025-06-27 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-07-05 | -2954500 | event_943 | housing | recurring_expense | Home association fee |
| 2025-07-06 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-07-07 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-07-08 | -2720215.11 | event_944 | utilities | recurring_expense | Municipal utilities |
| 2025-07-09 | -1881000 | event_945 | insurance | recurring_expense | Vehicle insurance premium |
| 2025-07-10 | -2544100 | event_946 | education | recurring_expense | Child education fee |
| 2025-07-12 | -2943993.42 | event_947 | healthcare | recurring_expense | Regular medicine purchase |
| 2025-07-14 | -168150 | event_949 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-07-15 | 23256000 | event_941 | salary | recurring_income | Base salary |
| 2025-07-16 | -1350022.55 | event_989 | dining | recurring_expense | Weekend food delivery |
| 2025-07-16 | -1600926.75 | event_948 | entertainment | recurring_expense | Games and recreation |
| 2025-07-17 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |
| 2025-07-20 | -1088014.14 | event_980 | transport | recurring_expense | Vehicle charging |
| 2025-07-27 | -1421333.16 | event_967 | groceries | recurring_expense | Fresh food shop |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-05-03 | 0 | 63531795 | 29391195 | 51021150 | 50421795 | 13110000 | (empty) |
| 1 | 2025-05-04 | 0 | 63531795 | 29391195 | 51021150 | 50421795 | 0 | (empty) |
| 2 | 2025-05-05 | -2954500 | 60577295 | 26436695 | 48066650 | 47467295 | 0 | event_943 |
| 3 | 2025-05-06 | 0 | 60577295 | 26436695 | 48066650 | 47467295 | 0 | (empty) |
| 4 | 2025-05-07 | 0 | 60577295 | 26436695 | 48066650 | 47467295 | 0 | (empty) |
| 5 | 2025-05-08 | -4141548.27 | 56435746.73 | 22295146.73 | 43925101.73 | 43325746.73 | 0 | event_967, event_944 |
| 6 | 2025-05-09 | -1881000 | 54554746.73 | 20414146.73 | 42044101.73 | 41444746.73 | 0 | event_945 |
| 7 | 2025-05-10 | -2544100 | 52010646.73 | 17870046.73 | 39500001.73 | 38900646.73 | 0 | event_946 |
| 8 | 2025-05-11 | -1088014.14 | 50922632.59 | 16782032.59 | 38411987.59 | 37812632.59 | 0 | event_980 |
| 9 | 2025-05-12 | -2943993.42 | 47978639.17 | 13838039.17 | 35467994.17 | 34868639.17 | 0 | event_947 |
| 10 | 2025-05-13 | 0 | 47978639.17 | 13838039.17 | 35467994.17 | 34868639.17 | 0 | (empty) |
| 11 | 2025-05-14 | -1518172.55 | 46460466.62 | 12319866.62 | 33949821.62 | 34202689.17 | 0 | event_949, event_989 |
| 12 | 2025-05-15 | 23256000 | 69716466.62 | 35575866.62 | 57205821.62 | 57458689.17 | 0 | event_941 |
| 13 | 2025-05-16 | -1600926.75 | 68115539.87 | 33974939.87 | 55604894.87 | 55857762.42 | 0 | event_948 |
| 14 | 2025-05-17 | 0 | 68115539.87 | 33974939.87 | 55604894.87 | 55857762.42 | 0 | (empty) |
| 15 | 2025-05-18 | -1421333.16 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | event_967 |
| 16 | 2025-05-19 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 17 | 2025-05-20 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 18 | 2025-05-21 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 19 | 2025-05-22 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 20 | 2025-05-23 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 21 | 2025-05-24 | 0 | 66694206.71 | 32553606.71 | 54183561.71 | 54436429.26 | 0 | (empty) |
| 22 | 2025-05-25 | -1088014.14 | 65606192.57 | 31465592.57 | 53095547.57 | 53348415.12 | 0 | event_980 |
| 23 | 2025-05-26 | 0 | 65606192.57 | 31465592.57 | 53095547.57 | 53348415.12 | 0 | (empty) |
| 24 | 2025-05-27 | 0 | 65606192.57 | 31465592.57 | 53095547.57 | 53348415.12 | 0 | (empty) |
| 25 | 2025-05-28 | -1421333.16 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | event_967 |
| 26 | 2025-05-29 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 27 | 2025-05-30 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 28 | 2025-05-31 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 29 | 2025-06-01 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 30 | 2025-06-02 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 31 | 2025-06-03 | 0 | 64184859.41 | 30044259.41 | 51674214.41 | 51927081.96 | 0 | (empty) |
| 32 | 2025-06-04 | -1350022.55 | 62834836.86 | 28694236.86 | 50324191.86 | 51261131.96 | 0 | event_989 |
| 33 | 2025-06-05 | -2954500 | 59880336.86 | 25739736.86 | 47369691.86 | 48306631.96 | 0 | event_943 |
| 34 | 2025-06-06 | 0 | 59880336.86 | 25739736.86 | 47369691.86 | 48306631.96 | 0 | (empty) |
| 35 | 2025-06-07 | -1421333.16 | 58459003.7 | 24318403.7 | 45948358.7 | 46885298.8 | 0 | event_967 |
| 36 | 2025-06-08 | -3808229.25 | 54650774.45 | 20510174.45 | 42140129.45 | 43077069.55 | 0 | event_980, event_944 |
| 37 | 2025-06-09 | -1881000 | 52769774.45 | 18629174.45 | 40259129.45 | 41196069.55 | 0 | event_945 |
| 38 | 2025-06-10 | -2544100 | 50225674.45 | 16085074.45 | 37715029.45 | 38651969.55 | 0 | event_946 |
| 39 | 2025-06-11 | 0 | 50225674.45 | 16085074.45 | 37715029.45 | 38651969.55 | 0 | (empty) |
| 40 | 2025-06-12 | -2943993.42 | 47281681.03 | 13141081.03 | 34771036.03 | 35707976.13 | 0 | event_947 |
| 41 | 2025-06-13 | 0 | 47281681.03 | 13141081.03 | 34771036.03 | 35707976.13 | 0 | (empty) |
| 42 | 2025-06-14 | -168150 | 47113531.03 | 12972931.03 | 34602886.03 | 35707976.13 | 0 | event_949 |
| 43 | 2025-06-15 | 23256000 | 70369531.03 | 36228931.03 | 57858886.03 | 58963976.13 | 0 | event_941 |
| 44 | 2025-06-16 | -1600926.75 | 68768604.28 | 34628004.28 | 56257959.28 | 57363049.38 | 0 | event_948 |
| 45 | 2025-06-17 | -1421333.16 | 67347271.12 | 33206671.12 | 54836626.12 | 55941716.22 | 0 | event_967 |
| 46 | 2025-06-18 | 0 | 67347271.12 | 33206671.12 | 54836626.12 | 55941716.22 | 0 | (empty) |
| 47 | 2025-06-19 | 0 | 67347271.12 | 33206671.12 | 54836626.12 | 55941716.22 | 0 | (empty) |
| 48 | 2025-06-20 | 0 | 67347271.12 | 33206671.12 | 54836626.12 | 55941716.22 | 0 | (empty) |
| 49 | 2025-06-21 | 0 | 67347271.12 | 33206671.12 | 54836626.12 | 55941716.22 | 0 | (empty) |
| 50 | 2025-06-22 | -1088014.14 | 66259256.98 | 32118656.98 | 53748611.98 | 54853702.08 | 0 | event_980 |
| 51 | 2025-06-23 | 0 | 66259256.98 | 32118656.98 | 53748611.98 | 54853702.08 | 0 | (empty) |
| 52 | 2025-06-24 | 0 | 66259256.98 | 32118656.98 | 53748611.98 | 54853702.08 | 0 | (empty) |
| 53 | 2025-06-25 | -1350022.55 | 64909234.43 | 30768634.43 | 52398589.43 | 54187752.08 | 0 | event_989 |
| 54 | 2025-06-26 | 0 | 64909234.43 | 30768634.43 | 52398589.43 | 54187752.08 | 0 | (empty) |
| 55 | 2025-06-27 | -1421333.16 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | event_967 |
| 56 | 2025-06-28 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 57 | 2025-06-29 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 58 | 2025-06-30 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 59 | 2025-07-01 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 60 | 2025-07-02 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 61 | 2025-07-03 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 62 | 2025-07-04 | 0 | 63487901.27 | 29347301.27 | 50977256.27 | 52766418.92 | 0 | (empty) |
| 63 | 2025-07-05 | -2954500 | 60533401.27 | 26392801.27 | 48022756.27 | 49811918.92 | 0 | event_943 |
| 64 | 2025-07-06 | -1088014.14 | 59445387.13 | 25304787.13 | 46934742.13 | 48723904.78 | 0 | event_980 |
| 65 | 2025-07-07 | -1421333.16 | 58024053.97 | 23883453.97 | 45513408.97 | 47302571.62 | 0 | event_967 |
| 66 | 2025-07-08 | -2720215.11 | 55303838.86 | 21163238.86 | 42793193.86 | 44582356.51 | 0 | event_944 |
| 67 | 2025-07-09 | -1881000 | 53422838.86 | 19282238.86 | 40912193.86 | 42701356.51 | 0 | event_945 |
| 68 | 2025-07-10 | -2544100 | 50878738.86 | 16738138.86 | 38368093.86 | 40157256.51 | 0 | event_946 |
| 69 | 2025-07-11 | 0 | 50878738.86 | 16738138.86 | 38368093.86 | 40157256.51 | 0 | (empty) |
| 70 | 2025-07-12 | -2943993.42 | 47934745.44 | 13794145.44 | 35424100.44 | 37213263.09 | 0 | event_947 |
| 71 | 2025-07-13 | 0 | 47934745.44 | 13794145.44 | 35424100.44 | 37213263.09 | 0 | (empty) |
| 72 | 2025-07-14 | -168150 | 47766595.44 | 13625995.44 | 35255950.44 | 37213263.09 | 0 | event_949 |
| 73 | 2025-07-15 | 23256000 | 71022595.44 | 36881995.44 | 58511950.44 | 60469263.09 | 0 | event_941 |
| 74 | 2025-07-16 | -2950949.3 | 68071646.14 | 33931046.14 | 55561001.14 | 58202386.34 | 0 | event_989, event_948 |
| 75 | 2025-07-17 | -1421333.16 | 66650312.98 | 32509712.98 | 54139667.98 | 56781053.18 | 0 | event_967 |
| 76 | 2025-07-18 | 0 | 66650312.98 | 32509712.98 | 54139667.98 | 56781053.18 | 0 | (empty) |
| 77 | 2025-07-19 | 0 | 66650312.98 | 32509712.98 | 54139667.98 | 56781053.18 | 0 | (empty) |
| 78 | 2025-07-20 | -1088014.14 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | event_980 |
| 79 | 2025-07-21 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 80 | 2025-07-22 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 81 | 2025-07-23 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 82 | 2025-07-24 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 83 | 2025-07-25 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 84 | 2025-07-26 | 0 | 65562298.84 | 31421698.84 | 53051653.84 | 55693039.04 | 0 | (empty) |
| 85 | 2025-07-27 | -1421333.16 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | event_967 |
| 86 | 2025-07-28 | 0 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | (empty) |
| 87 | 2025-07-29 | 0 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | (empty) |
| 88 | 2025-07-30 | 0 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | (empty) |
| 89 | 2025-07-31 | 0 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | (empty) |
| 90 | 2025-08-01 | 0 | 64140965.68 | 30000365.68 | 51630320.68 | 54271705.88 | 0 | (empty) |

## request_12 â€” user_12 (ZAR)

Request: 65164 on 2026-04-05; deadline 2026-06-20. Opening 193089.89; minimum 43200.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 65164 | 60370.23 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | installments | installments | yes |
| payment_plan | 2026-04-19:22590.19\|2026-05-20:22590.19\|2026-06-20:22590.19 | 2026-04-19:22590.19\|2026-05-20:22590.19\|2026-06-20:22590.19 | yes |
| earliest_date_for_full_payment | 2026-04-05 | (empty) | NO |
| spending_changes_needed | none | reduce_to:event_1054:1072.50\|stop:event_1016 | NO |

Baseline trough: day 87 (2026-07-01), balance 103570.23, headroom 60370.23.

Protected: rent|utilities|groceries. Reduce: dining|shopping. Stop: streaming.

Salary mode: ended. Evidence: message_09. Unparsed messages: none.

- message_09 (employer, 2026-03-25T09:30:00Z): A note from Cobalt Systems about your upcoming pay. The current seasonal contract has ended. No off-season income or renewal has been confirmed. We’ll contact you separately if another shift block or contract is approved. Payroll ref EMP-0009.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1015 | cloud_storage / Shared storage plan | 5 / 5 | 447.7 | 447.70 | 447.7â€“447.7 | 447.7 | 2026-04-11, 2026-05-11, 2026-06-11 |
| event_1054 | dining / Coffee shop | 9 / 6 | 2257.598888888888888888888889 | 2344.45 | 1765.33â€“2608.96 | 2257.6 | 2026-04-18, 2026-05-09, 2026-05-30, 2026-06-20 |
| event_1036 | groceries / Fresh food shop | 18 / 6 | 2134.888333333333333333333333 | 2281.555 | 1539.11â€“2729.09 | 2134.89 | 2026-04-07, 2026-04-17, 2026-04-27, 2026-05-07, 2026-05-17, 2026-05-27, 2026-06-06, 2026-06-16, 2026-06-26 |
| event_1018 | rent / Monthly rent | 6 / 6 | 11792 | 11792.00 | 11792â€“11792 | 11792 | 2026-05-01, 2026-06-01, 2026-07-01 |
| event_1017 | shopping / Monthly shopping spend | 5 / 5 | 1255.886 | 1243.49 | 1169.42â€“1401.99 | 1255.89 | 2026-04-11, 2026-05-11, 2026-06-11 |
| event_1016 | streaming / Family streaming plan | 5 / 5 | 1504.8 | 1504.80 | 1504.8â€“1504.8 | 1504.8 | 2026-04-08, 2026-05-08, 2026-06-08 |
| event_1045 | transport / Parking and tolls | 9 / 6 | 1436.23 | 1355.85 | 1240.84â€“1722.14 | 1436.23 | 2026-04-17, 2026-05-08, 2026-05-29, 2026-06-19 |
| event_1014 | utilities / Water and power payment | 5 / 5 | 3509.724 | 3606.20 | 3103.78â€“3755.96 | 3509.72 | 2026-04-05, 2026-05-05, 2026-06-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-04-05 | -3509.72 | event_1014 | utilities | recurring_expense | Water and power payment |
| 2026-04-07 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-04-08 | -1504.8 | event_1016 | streaming | recurring_expense | Family streaming plan |
| 2026-04-11 | -447.7 | event_1015 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-04-11 | -1255.89 | event_1017 | shopping | recurring_expense | Monthly shopping spend |
| 2026-04-17 | -1436.23 | event_1045 | transport | recurring_expense | Parking and tolls |
| 2026-04-17 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-04-18 | -2257.6 | event_1054 | dining | recurring_expense | Coffee shop |
| 2026-04-27 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-05-01 | -11792 | event_1018 | rent | recurring_expense | Monthly rent |
| 2026-05-05 | -3509.72 | event_1014 | utilities | recurring_expense | Water and power payment |
| 2026-05-07 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-05-08 | -1436.23 | event_1045 | transport | recurring_expense | Parking and tolls |
| 2026-05-08 | -1504.8 | event_1016 | streaming | recurring_expense | Family streaming plan |
| 2026-05-09 | -2257.6 | event_1054 | dining | recurring_expense | Coffee shop |
| 2026-05-11 | -447.7 | event_1015 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-05-11 | -1255.89 | event_1017 | shopping | recurring_expense | Monthly shopping spend |
| 2026-05-17 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-05-27 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-05-29 | -1436.23 | event_1045 | transport | recurring_expense | Parking and tolls |
| 2026-05-30 | -2257.6 | event_1054 | dining | recurring_expense | Coffee shop |
| 2026-06-01 | -11792 | event_1018 | rent | recurring_expense | Monthly rent |
| 2026-06-05 | -3509.72 | event_1014 | utilities | recurring_expense | Water and power payment |
| 2026-06-06 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-06-08 | -1504.8 | event_1016 | streaming | recurring_expense | Family streaming plan |
| 2026-06-11 | -447.7 | event_1015 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-06-11 | -1255.89 | event_1017 | shopping | recurring_expense | Monthly shopping spend |
| 2026-06-16 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-06-19 | -1436.23 | event_1045 | transport | recurring_expense | Parking and tolls |
| 2026-06-20 | -2257.6 | event_1054 | dining | recurring_expense | Coffee shop |
| 2026-06-26 | -2134.89 | event_1036 | groceries | recurring_expense | Fresh food shop |
| 2026-07-01 | -11792 | event_1018 | rent | recurring_expense | Monthly rent |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-04-05 | -3509.72 | 189580.17 | 146380.17 | 124416.17 | 189580.17 | 0 | event_1014 |
| 1 | 2026-04-06 | 0 | 189580.17 | 146380.17 | 124416.17 | 189580.17 | 0 | (empty) |
| 2 | 2026-04-07 | -2134.89 | 187445.28 | 144245.28 | 122281.28 | 187445.28 | 0 | event_1036 |
| 3 | 2026-04-08 | -1504.8 | 185940.48 | 142740.48 | 120776.48 | 187445.28 | 0 | event_1016 |
| 4 | 2026-04-09 | 0 | 185940.48 | 142740.48 | 120776.48 | 187445.28 | 0 | (empty) |
| 5 | 2026-04-10 | 0 | 185940.48 | 142740.48 | 120776.48 | 187445.28 | 0 | (empty) |
| 6 | 2026-04-11 | -1703.59 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | event_1015, event_1017 |
| 7 | 2026-04-12 | 0 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | (empty) |
| 8 | 2026-04-13 | 0 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | (empty) |
| 9 | 2026-04-14 | 0 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | (empty) |
| 10 | 2026-04-15 | 0 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | (empty) |
| 11 | 2026-04-16 | 0 | 184236.89 | 141036.89 | 119072.89 | 185741.69 | 0 | (empty) |
| 12 | 2026-04-17 | -3571.12 | 180665.77 | 137465.77 | 115501.77 | 182170.57 | 0 | event_1045, event_1036 |
| 13 | 2026-04-18 | -2257.6 | 178408.17 | 135208.17 | 113244.17 | 181098.07 | 0 | event_1054 |
| 14 | 2026-04-19 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 22590.19 | (empty) |
| 15 | 2026-04-20 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 16 | 2026-04-21 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 17 | 2026-04-22 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 18 | 2026-04-23 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 19 | 2026-04-24 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 20 | 2026-04-25 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 21 | 2026-04-26 | 0 | 178408.17 | 135208.17 | 113244.17 | 158507.88 | 0 | (empty) |
| 22 | 2026-04-27 | -2134.89 | 176273.28 | 133073.28 | 111109.28 | 156372.99 | 0 | event_1036 |
| 23 | 2026-04-28 | 0 | 176273.28 | 133073.28 | 111109.28 | 156372.99 | 0 | (empty) |
| 24 | 2026-04-29 | 0 | 176273.28 | 133073.28 | 111109.28 | 156372.99 | 0 | (empty) |
| 25 | 2026-04-30 | 0 | 176273.28 | 133073.28 | 111109.28 | 156372.99 | 0 | (empty) |
| 26 | 2026-05-01 | -11792 | 164481.28 | 121281.28 | 99317.28 | 144580.99 | 0 | event_1018 |
| 27 | 2026-05-02 | 0 | 164481.28 | 121281.28 | 99317.28 | 144580.99 | 0 | (empty) |
| 28 | 2026-05-03 | 0 | 164481.28 | 121281.28 | 99317.28 | 144580.99 | 0 | (empty) |
| 29 | 2026-05-04 | 0 | 164481.28 | 121281.28 | 99317.28 | 144580.99 | 0 | (empty) |
| 30 | 2026-05-05 | -3509.72 | 160971.56 | 117771.56 | 95807.56 | 141071.27 | 0 | event_1014 |
| 31 | 2026-05-06 | 0 | 160971.56 | 117771.56 | 95807.56 | 141071.27 | 0 | (empty) |
| 32 | 2026-05-07 | -2134.89 | 158836.67 | 115636.67 | 93672.67 | 138936.38 | 0 | event_1036 |
| 33 | 2026-05-08 | -2941.03 | 155895.64 | 112695.64 | 90731.64 | 137500.15 | 0 | event_1045, event_1016 |
| 34 | 2026-05-09 | -2257.6 | 153638.04 | 110438.04 | 88474.04 | 136427.65 | 0 | event_1054 |
| 35 | 2026-05-10 | 0 | 153638.04 | 110438.04 | 88474.04 | 136427.65 | 0 | (empty) |
| 36 | 2026-05-11 | -1703.59 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | event_1015, event_1017 |
| 37 | 2026-05-12 | 0 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | (empty) |
| 38 | 2026-05-13 | 0 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | (empty) |
| 39 | 2026-05-14 | 0 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | (empty) |
| 40 | 2026-05-15 | 0 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | (empty) |
| 41 | 2026-05-16 | 0 | 151934.45 | 108734.45 | 86770.45 | 134724.06 | 0 | (empty) |
| 42 | 2026-05-17 | -2134.89 | 149799.56 | 106599.56 | 84635.56 | 132589.17 | 0 | event_1036 |
| 43 | 2026-05-18 | 0 | 149799.56 | 106599.56 | 84635.56 | 132589.17 | 0 | (empty) |
| 44 | 2026-05-19 | 0 | 149799.56 | 106599.56 | 84635.56 | 132589.17 | 0 | (empty) |
| 45 | 2026-05-20 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 22590.19 | (empty) |
| 46 | 2026-05-21 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 47 | 2026-05-22 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 48 | 2026-05-23 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 49 | 2026-05-24 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 50 | 2026-05-25 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 51 | 2026-05-26 | 0 | 149799.56 | 106599.56 | 84635.56 | 109998.98 | 0 | (empty) |
| 52 | 2026-05-27 | -2134.89 | 147664.67 | 104464.67 | 82500.67 | 107864.09 | 0 | event_1036 |
| 53 | 2026-05-28 | 0 | 147664.67 | 104464.67 | 82500.67 | 107864.09 | 0 | (empty) |
| 54 | 2026-05-29 | -1436.23 | 146228.44 | 103028.44 | 81064.44 | 106427.86 | 0 | event_1045 |
| 55 | 2026-05-30 | -2257.6 | 143970.84 | 100770.84 | 78806.84 | 105355.36 | 0 | event_1054 |
| 56 | 2026-05-31 | 0 | 143970.84 | 100770.84 | 78806.84 | 105355.36 | 0 | (empty) |
| 57 | 2026-06-01 | -11792 | 132178.84 | 88978.84 | 67014.84 | 93563.36 | 0 | event_1018 |
| 58 | 2026-06-02 | 0 | 132178.84 | 88978.84 | 67014.84 | 93563.36 | 0 | (empty) |
| 59 | 2026-06-03 | 0 | 132178.84 | 88978.84 | 67014.84 | 93563.36 | 0 | (empty) |
| 60 | 2026-06-04 | 0 | 132178.84 | 88978.84 | 67014.84 | 93563.36 | 0 | (empty) |
| 61 | 2026-06-05 | -3509.72 | 128669.12 | 85469.12 | 63505.12 | 90053.64 | 0 | event_1014 |
| 62 | 2026-06-06 | -2134.89 | 126534.23 | 83334.23 | 61370.23 | 87918.75 | 0 | event_1036 |
| 63 | 2026-06-07 | 0 | 126534.23 | 83334.23 | 61370.23 | 87918.75 | 0 | (empty) |
| 64 | 2026-06-08 | -1504.8 | 125029.43 | 81829.43 | 59865.43 | 87918.75 | 0 | event_1016 |
| 65 | 2026-06-09 | 0 | 125029.43 | 81829.43 | 59865.43 | 87918.75 | 0 | (empty) |
| 66 | 2026-06-10 | 0 | 125029.43 | 81829.43 | 59865.43 | 87918.75 | 0 | (empty) |
| 67 | 2026-06-11 | -1703.59 | 123325.84 | 80125.84 | 58161.84 | 86215.16 | 0 | event_1015, event_1017 |
| 68 | 2026-06-12 | 0 | 123325.84 | 80125.84 | 58161.84 | 86215.16 | 0 | (empty) |
| 69 | 2026-06-13 | 0 | 123325.84 | 80125.84 | 58161.84 | 86215.16 | 0 | (empty) |
| 70 | 2026-06-14 | 0 | 123325.84 | 80125.84 | 58161.84 | 86215.16 | 0 | (empty) |
| 71 | 2026-06-15 | 0 | 123325.84 | 80125.84 | 58161.84 | 86215.16 | 0 | (empty) |
| 72 | 2026-06-16 | -2134.89 | 121190.95 | 77990.95 | 56026.95 | 84080.27 | 0 | event_1036 |
| 73 | 2026-06-17 | 0 | 121190.95 | 77990.95 | 56026.95 | 84080.27 | 0 | (empty) |
| 74 | 2026-06-18 | 0 | 121190.95 | 77990.95 | 56026.95 | 84080.27 | 0 | (empty) |
| 75 | 2026-06-19 | -1436.23 | 119754.72 | 76554.72 | 54590.72 | 82644.04 | 0 | event_1045 |
| 76 | 2026-06-20 | -2257.6 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 22590.19 | event_1054 |
| 77 | 2026-06-21 | 0 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 0 | (empty) |
| 78 | 2026-06-22 | 0 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 0 | (empty) |
| 79 | 2026-06-23 | 0 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 0 | (empty) |
| 80 | 2026-06-24 | 0 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 0 | (empty) |
| 81 | 2026-06-25 | 0 | 117497.12 | 74297.12 | 52333.12 | 58981.35 | 0 | (empty) |
| 82 | 2026-06-26 | -2134.89 | 115362.23 | 72162.23 | 50198.23 | 56846.46 | 0 | event_1036 |
| 83 | 2026-06-27 | 0 | 115362.23 | 72162.23 | 50198.23 | 56846.46 | 0 | (empty) |
| 84 | 2026-06-28 | 0 | 115362.23 | 72162.23 | 50198.23 | 56846.46 | 0 | (empty) |
| 85 | 2026-06-29 | 0 | 115362.23 | 72162.23 | 50198.23 | 56846.46 | 0 | (empty) |
| 86 | 2026-06-30 | 0 | 115362.23 | 72162.23 | 50198.23 | 56846.46 | 0 | (empty) |
| 87 | 2026-07-01 | -11792 | 103570.23 | 60370.23 | 38406.23 | 45054.46 | 0 | event_1018 |
| 88 | 2026-07-02 | 0 | 103570.23 | 60370.23 | 38406.23 | 45054.46 | 0 | (empty) |
| 89 | 2026-07-03 | 0 | 103570.23 | 60370.23 | 38406.23 | 45054.46 | 0 | (empty) |
| 90 | 2026-07-04 | 0 | 103570.23 | 60370.23 | 38406.23 | 45054.46 | 0 | (empty) |

## request_13 â€” user_13 (EUR)

Request: 941.6 on 2024-03-07; deadline 2024-05-15. Opening 2789.52; minimum 1300.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 433.4 | 812.13 | NO |
| affordability_status | affordable_later | affordable_later | yes |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2024-05-15:941.60 | 2024-05-15:941.60 | yes |
| earliest_date_for_full_payment | 2024-05-15 | 2024-05-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 68 (2024-05-14), balance 2112.13, headroom 812.13.

Protected: rent|groceries|transport. Reduce: gym. Stop: music_subscription|delivery_membership.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1091 | delivery_membership / Delivery service plan | 5 / 5 | 21 | 21.00 | 21â€“21 | 21 | 2024-03-13, 2024-04-13, 2024-05-13 |
| event_1093 | entertainment / Local event tickets | 5 / 5 | 32.96 | 31.80 | 30.39â€“37.9 | 32.96 | 2024-03-14, 2024-04-14, 2024-05-14 |
| event_1121 | groceries / Bulk pantry shop | 26 / 7 | 99.66038461538461538461538462 | 100.05 | 73.74â€“120.89 | 99.66 | 2024-03-12, 2024-03-19, 2024-03-26, 2024-04-02, 2024-04-09, 2024-04-16, 2024-04-23, 2024-04-30, 2024-05-07, 2024-05-14, 2024-05-21, 2024-05-28, 2024-06-04 |
| event_1092 | gym / Community fitness plan | 5 / 5 | 61 | 61.00 | 61â€“61 | 61 | 2024-03-10, 2024-04-10, 2024-05-10 |
| event_1090 | music_subscription / Music subscription | 5 / 5 | 29 | 29.00 | 29â€“29 | 29 | 2024-03-11, 2024-04-11, 2024-05-11 |
| event_1094 | rent / Shared housing rent | 6 / 6 | 622.6 | 622.60 | 622.6â€“622.6 | 622.6 | 2024-04-02, 2024-05-02, 2024-06-02 |
| event_1147 | transport / Vehicle charging | 26 / 7 | 44.825 | 45.33 | 33.5â€“58.44 | 44.83 | 2024-03-13, 2024-03-20, 2024-03-27, 2024-04-03, 2024-04-10, 2024-04-17, 2024-04-24, 2024-05-01, 2024-05-08, 2024-05-15, 2024-05-22, 2024-05-29, 2024-06-05 |
| event_1095 | utilities / Water and power payment | 6 / 6 | 143.6616666666666666666666667 | 143.545 | 131.53â€“162.77 | 143.66 | 2024-04-06, 2024-05-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-03-10 | -61 | event_1092 | gym | recurring_expense | Community fitness plan |
| 2024-03-11 | -29 | event_1090 | music_subscription | recurring_expense | Music subscription |
| 2024-03-12 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-03-13 | -21 | event_1091 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-03-13 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-03-14 | -32.96 | event_1093 | entertainment | recurring_expense | Local event tickets |
| 2024-03-15 | 1343.54 | event_1161 | salary | recurring_income | Next confirmed salary |
| 2024-03-19 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-03-20 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-03-26 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-03-27 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-04-02 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-04-02 | -622.6 | event_1094 | rent | recurring_expense | Shared housing rent |
| 2024-04-03 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-04-06 | -143.66 | event_1095 | utilities | recurring_expense | Water and power payment |
| 2024-04-09 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-04-10 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-04-10 | -61 | event_1092 | gym | recurring_expense | Community fitness plan |
| 2024-04-11 | -29 | event_1090 | music_subscription | recurring_expense | Music subscription |
| 2024-04-13 | -21 | event_1091 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-04-14 | -32.96 | event_1093 | entertainment | recurring_expense | Local event tickets |
| 2024-04-15 | 1343.54 | event_1161 | salary | recurring_income | Next confirmed salary |
| 2024-04-16 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-04-17 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-04-23 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-04-24 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-04-30 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-05-01 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-05-02 | -622.6 | event_1094 | rent | recurring_expense | Shared housing rent |
| 2024-05-06 | -143.66 | event_1095 | utilities | recurring_expense | Water and power payment |
| 2024-05-07 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-05-08 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-05-10 | -61 | event_1092 | gym | recurring_expense | Community fitness plan |
| 2024-05-11 | -29 | event_1090 | music_subscription | recurring_expense | Music subscription |
| 2024-05-13 | -21 | event_1091 | delivery_membership | recurring_expense | Delivery service plan |
| 2024-05-14 | -32.96 | event_1093 | entertainment | recurring_expense | Local event tickets |
| 2024-05-14 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-05-15 | 1343.54 | event_1161 | salary | recurring_income | Next confirmed salary |
| 2024-05-15 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-05-21 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-05-22 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-05-28 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-05-29 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |
| 2024-06-02 | -622.6 | event_1094 | rent | recurring_expense | Shared housing rent |
| 2024-06-04 | -99.66 | event_1121 | groceries | recurring_expense | Bulk pantry shop |
| 2024-06-05 | -44.83 | event_1147 | transport | recurring_expense | Vehicle charging |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-03-07 | 0 | 2789.52 | 1489.52 | 2356.12 | 2789.52 | 0 | (empty) |
| 1 | 2024-03-08 | 0 | 2789.52 | 1489.52 | 2356.12 | 2789.52 | 0 | (empty) |
| 2 | 2024-03-09 | 0 | 2789.52 | 1489.52 | 2356.12 | 2789.52 | 0 | (empty) |
| 3 | 2024-03-10 | -61 | 2728.52 | 1428.52 | 2295.12 | 2728.52 | 0 | event_1092 |
| 4 | 2024-03-11 | -29 | 2699.52 | 1399.52 | 2266.12 | 2699.52 | 0 | event_1090 |
| 5 | 2024-03-12 | -99.66 | 2599.86 | 1299.86 | 2166.46 | 2599.86 | 0 | event_1121 |
| 6 | 2024-03-13 | -65.83 | 2534.03 | 1234.03 | 2100.63 | 2534.03 | 0 | event_1091, event_1147 |
| 7 | 2024-03-14 | -32.96 | 2501.07 | 1201.07 | 2067.67 | 2501.07 | 0 | event_1093 |
| 8 | 2024-03-15 | 1343.54 | 3844.61 | 2544.61 | 3411.21 | 3844.61 | 0 | event_1161 |
| 9 | 2024-03-16 | 0 | 3844.61 | 2544.61 | 3411.21 | 3844.61 | 0 | (empty) |
| 10 | 2024-03-17 | 0 | 3844.61 | 2544.61 | 3411.21 | 3844.61 | 0 | (empty) |
| 11 | 2024-03-18 | 0 | 3844.61 | 2544.61 | 3411.21 | 3844.61 | 0 | (empty) |
| 12 | 2024-03-19 | -99.66 | 3744.95 | 2444.95 | 3311.55 | 3744.95 | 0 | event_1121 |
| 13 | 2024-03-20 | -44.83 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | event_1147 |
| 14 | 2024-03-21 | 0 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | (empty) |
| 15 | 2024-03-22 | 0 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | (empty) |
| 16 | 2024-03-23 | 0 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | (empty) |
| 17 | 2024-03-24 | 0 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | (empty) |
| 18 | 2024-03-25 | 0 | 3700.12 | 2400.12 | 3266.72 | 3700.12 | 0 | (empty) |
| 19 | 2024-03-26 | -99.66 | 3600.46 | 2300.46 | 3167.06 | 3600.46 | 0 | event_1121 |
| 20 | 2024-03-27 | -44.83 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | event_1147 |
| 21 | 2024-03-28 | 0 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | (empty) |
| 22 | 2024-03-29 | 0 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | (empty) |
| 23 | 2024-03-30 | 0 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | (empty) |
| 24 | 2024-03-31 | 0 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | (empty) |
| 25 | 2024-04-01 | 0 | 3555.63 | 2255.63 | 3122.23 | 3555.63 | 0 | (empty) |
| 26 | 2024-04-02 | -722.26 | 2833.37 | 1533.37 | 2399.97 | 2833.37 | 0 | event_1121, event_1094 |
| 27 | 2024-04-03 | -44.83 | 2788.54 | 1488.54 | 2355.14 | 2788.54 | 0 | event_1147 |
| 28 | 2024-04-04 | 0 | 2788.54 | 1488.54 | 2355.14 | 2788.54 | 0 | (empty) |
| 29 | 2024-04-05 | 0 | 2788.54 | 1488.54 | 2355.14 | 2788.54 | 0 | (empty) |
| 30 | 2024-04-06 | -143.66 | 2644.88 | 1344.88 | 2211.48 | 2644.88 | 0 | event_1095 |
| 31 | 2024-04-07 | 0 | 2644.88 | 1344.88 | 2211.48 | 2644.88 | 0 | (empty) |
| 32 | 2024-04-08 | 0 | 2644.88 | 1344.88 | 2211.48 | 2644.88 | 0 | (empty) |
| 33 | 2024-04-09 | -99.66 | 2545.22 | 1245.22 | 2111.82 | 2545.22 | 0 | event_1121 |
| 34 | 2024-04-10 | -105.83 | 2439.39 | 1139.39 | 2005.99 | 2439.39 | 0 | event_1147, event_1092 |
| 35 | 2024-04-11 | -29 | 2410.39 | 1110.39 | 1976.99 | 2410.39 | 0 | event_1090 |
| 36 | 2024-04-12 | 0 | 2410.39 | 1110.39 | 1976.99 | 2410.39 | 0 | (empty) |
| 37 | 2024-04-13 | -21 | 2389.39 | 1089.39 | 1955.99 | 2389.39 | 0 | event_1091 |
| 38 | 2024-04-14 | -32.96 | 2356.43 | 1056.43 | 1923.03 | 2356.43 | 0 | event_1093 |
| 39 | 2024-04-15 | 1343.54 | 3699.97 | 2399.97 | 3266.57 | 3699.97 | 0 | event_1161 |
| 40 | 2024-04-16 | -99.66 | 3600.31 | 2300.31 | 3166.91 | 3600.31 | 0 | event_1121 |
| 41 | 2024-04-17 | -44.83 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | event_1147 |
| 42 | 2024-04-18 | 0 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | (empty) |
| 43 | 2024-04-19 | 0 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | (empty) |
| 44 | 2024-04-20 | 0 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | (empty) |
| 45 | 2024-04-21 | 0 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | (empty) |
| 46 | 2024-04-22 | 0 | 3555.48 | 2255.48 | 3122.08 | 3555.48 | 0 | (empty) |
| 47 | 2024-04-23 | -99.66 | 3455.82 | 2155.82 | 3022.42 | 3455.82 | 0 | event_1121 |
| 48 | 2024-04-24 | -44.83 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | event_1147 |
| 49 | 2024-04-25 | 0 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | (empty) |
| 50 | 2024-04-26 | 0 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | (empty) |
| 51 | 2024-04-27 | 0 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | (empty) |
| 52 | 2024-04-28 | 0 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | (empty) |
| 53 | 2024-04-29 | 0 | 3410.99 | 2110.99 | 2977.59 | 3410.99 | 0 | (empty) |
| 54 | 2024-04-30 | -99.66 | 3311.33 | 2011.33 | 2877.93 | 3311.33 | 0 | event_1121 |
| 55 | 2024-05-01 | -44.83 | 3266.5 | 1966.5 | 2833.1 | 3266.5 | 0 | event_1147 |
| 56 | 2024-05-02 | -622.6 | 2643.9 | 1343.9 | 2210.5 | 2643.9 | 0 | event_1094 |
| 57 | 2024-05-03 | 0 | 2643.9 | 1343.9 | 2210.5 | 2643.9 | 0 | (empty) |
| 58 | 2024-05-04 | 0 | 2643.9 | 1343.9 | 2210.5 | 2643.9 | 0 | (empty) |
| 59 | 2024-05-05 | 0 | 2643.9 | 1343.9 | 2210.5 | 2643.9 | 0 | (empty) |
| 60 | 2024-05-06 | -143.66 | 2500.24 | 1200.24 | 2066.84 | 2500.24 | 0 | event_1095 |
| 61 | 2024-05-07 | -99.66 | 2400.58 | 1100.58 | 1967.18 | 2400.58 | 0 | event_1121 |
| 62 | 2024-05-08 | -44.83 | 2355.75 | 1055.75 | 1922.35 | 2355.75 | 0 | event_1147 |
| 63 | 2024-05-09 | 0 | 2355.75 | 1055.75 | 1922.35 | 2355.75 | 0 | (empty) |
| 64 | 2024-05-10 | -61 | 2294.75 | 994.75 | 1861.35 | 2294.75 | 0 | event_1092 |
| 65 | 2024-05-11 | -29 | 2265.75 | 965.75 | 1832.35 | 2265.75 | 0 | event_1090 |
| 66 | 2024-05-12 | 0 | 2265.75 | 965.75 | 1832.35 | 2265.75 | 0 | (empty) |
| 67 | 2024-05-13 | -21 | 2244.75 | 944.75 | 1811.35 | 2244.75 | 0 | event_1091 |
| 68 | 2024-05-14 | -132.62 | 2112.13 | 812.13 | 1678.73 | 2112.13 | 0 | event_1093, event_1121 |
| 69 | 2024-05-15 | 1298.71 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 941.6 | event_1161, event_1147 |
| 70 | 2024-05-16 | 0 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 0 | (empty) |
| 71 | 2024-05-17 | 0 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 0 | (empty) |
| 72 | 2024-05-18 | 0 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 0 | (empty) |
| 73 | 2024-05-19 | 0 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 0 | (empty) |
| 74 | 2024-05-20 | 0 | 3410.84 | 2110.84 | 2977.44 | 2469.24 | 0 | (empty) |
| 75 | 2024-05-21 | -99.66 | 3311.18 | 2011.18 | 2877.78 | 2369.58 | 0 | event_1121 |
| 76 | 2024-05-22 | -44.83 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | event_1147 |
| 77 | 2024-05-23 | 0 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | (empty) |
| 78 | 2024-05-24 | 0 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | (empty) |
| 79 | 2024-05-25 | 0 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | (empty) |
| 80 | 2024-05-26 | 0 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | (empty) |
| 81 | 2024-05-27 | 0 | 3266.35 | 1966.35 | 2832.95 | 2324.75 | 0 | (empty) |
| 82 | 2024-05-28 | -99.66 | 3166.69 | 1866.69 | 2733.29 | 2225.09 | 0 | event_1121 |
| 83 | 2024-05-29 | -44.83 | 3121.86 | 1821.86 | 2688.46 | 2180.26 | 0 | event_1147 |
| 84 | 2024-05-30 | 0 | 3121.86 | 1821.86 | 2688.46 | 2180.26 | 0 | (empty) |
| 85 | 2024-05-31 | 0 | 3121.86 | 1821.86 | 2688.46 | 2180.26 | 0 | (empty) |
| 86 | 2024-06-01 | 0 | 3121.86 | 1821.86 | 2688.46 | 2180.26 | 0 | (empty) |
| 87 | 2024-06-02 | -622.6 | 2499.26 | 1199.26 | 2065.86 | 1557.66 | 0 | event_1094 |
| 88 | 2024-06-03 | 0 | 2499.26 | 1199.26 | 2065.86 | 1557.66 | 0 | (empty) |
| 89 | 2024-06-04 | -99.66 | 2399.6 | 1099.6 | 1966.2 | 1458 | 0 | event_1121 |
| 90 | 2024-06-05 | -44.83 | 2354.77 | 1054.77 | 1921.37 | 1413.17 | 0 | event_1147 |

## request_14 â€” user_14 (EUR)

Request: 5414.2 on 2025-08-04; deadline 2025-10-04. Opening 3931.74; minimum 2200.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 597.74 | 616.29 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 10 (2025-08-14), balance 2816.29, headroom 616.29.

Protected: rent|healthcare|family_support|groceries. Reduce: shopping. Stop: cloud_storage.

Salary mode: resumed. Evidence: message_10. Unparsed messages: none.

- message_10 (employer, 2025-07-27T09:30:00Z): Here’s the latest payroll information from HarborWorks. Regular salary of EUR 2717 resumes on 2025-08-15. A new recurring childcare payment begins in the same month. The updated pay and deductions will appear from the next cycle. Payroll ref EMP-0010.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1198 | cloud_storage / Cloud storage plan | 5 / 5 | 14 | 14.00 | 14â€“14 | 14 | 2025-08-13, 2025-09-13, 2025-10-13 |
| event_1195 | debt_repayment / Credit card repayment | 5 / 5 | 350 | 350.00 | 350â€“350 | 350 | 2025-08-12, 2025-09-12, 2025-10-12 |
| event_1197 | family_support / Family support payment | 5 / 5 | 226 | 226.00 | 226â€“226 | 226 | 2025-08-14, 2025-09-14, 2025-10-14 |
| event_1226 | groceries / Bulk pantry shop | 26 / 7 | 104.7973076923076923076923077 | 99.005 | 81.22â€“140.51 | 104.8 | 2025-08-10, 2025-08-17, 2025-08-24, 2025-08-31, 2025-09-07, 2025-09-14, 2025-09-21, 2025-09-28, 2025-10-05, 2025-10-12, 2025-10-19, 2025-10-26, 2025-11-02 |
| event_1196 | healthcare / Family healthcare expense | 5 / 5 | 91.902 | 92.08 | 87.84â€“95.17 | 91.9 | 2025-08-11, 2025-09-11, 2025-10-11 |
| event_1200 | rent / Monthly rent | 6 / 6 | 688.6 | 688.60 | 688.6â€“688.6 | 688.6 | 2025-09-03, 2025-10-03 |
| event_1199 | shopping / Online retail purchases | 5 / 5 | 129.47 | 123.77 | 123.04â€“140.39 | 129.47 | 2025-08-13, 2025-09-13, 2025-10-13 |
| event_1239 | transport / Ride-hailing trip | 13 / 6 | 51.06230769230769230769230769 | 52.26 | 37.65â€“62.3 | 51.06 | 2025-08-11, 2025-08-25, 2025-09-08, 2025-09-22, 2025-10-06, 2025-10-20 |
| event_1194 | utilities / Energy provider bill | 5 / 5 | 148.218 | 146.41 | 141.46â€“156.08 | 148.22 | 2025-08-07, 2025-09-07, 2025-10-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-08-07 | -148.22 | event_1194 | utilities | recurring_expense | Energy provider bill |
| 2025-08-10 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-08-11 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-08-11 | -91.9 | event_1196 | healthcare | recurring_expense | Family healthcare expense |
| 2025-08-12 | -350 | event_1195 | debt_repayment | recurring_expense | Credit card repayment |
| 2025-08-13 | -14 | event_1198 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-08-13 | -129.47 | event_1199 | shopping | recurring_expense | Online retail purchases |
| 2025-08-14 | -226 | event_1197 | family_support | recurring_expense | Family support payment |
| 2025-08-15 | 2717 | event_1192 | salary | recurring_income | Payroll after returning from leave |
| 2025-08-17 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-08-24 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-08-25 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-08-31 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-09-03 | -688.6 | event_1200 | rent | recurring_expense | Monthly rent |
| 2025-09-07 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-09-07 | -148.22 | event_1194 | utilities | recurring_expense | Energy provider bill |
| 2025-09-08 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-09-11 | -91.9 | event_1196 | healthcare | recurring_expense | Family healthcare expense |
| 2025-09-12 | -350 | event_1195 | debt_repayment | recurring_expense | Credit card repayment |
| 2025-09-13 | -14 | event_1198 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-09-13 | -129.47 | event_1199 | shopping | recurring_expense | Online retail purchases |
| 2025-09-14 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-09-14 | -226 | event_1197 | family_support | recurring_expense | Family support payment |
| 2025-09-15 | 2717 | event_1192 | salary | recurring_income | Payroll after returning from leave |
| 2025-09-21 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-09-22 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-09-28 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-10-03 | -688.6 | event_1200 | rent | recurring_expense | Monthly rent |
| 2025-10-05 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-10-06 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-10-07 | -148.22 | event_1194 | utilities | recurring_expense | Energy provider bill |
| 2025-10-11 | -91.9 | event_1196 | healthcare | recurring_expense | Family healthcare expense |
| 2025-10-12 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-10-12 | -350 | event_1195 | debt_repayment | recurring_expense | Credit card repayment |
| 2025-10-13 | -14 | event_1198 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-10-13 | -129.47 | event_1199 | shopping | recurring_expense | Online retail purchases |
| 2025-10-14 | -226 | event_1197 | family_support | recurring_expense | Family support payment |
| 2025-10-15 | 2717 | event_1192 | salary | recurring_income | Payroll after returning from leave |
| 2025-10-19 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-10-20 | -51.06 | event_1239 | transport | recurring_expense | Ride-hailing trip |
| 2025-10-26 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |
| 2025-11-02 | -104.8 | event_1226 | groceries | recurring_expense | Bulk pantry shop |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-08-04 | 0 | 3931.74 | 1731.74 | 3334 | 3931.74 | 0 | (empty) |
| 1 | 2025-08-05 | 0 | 3931.74 | 1731.74 | 3334 | 3931.74 | 0 | (empty) |
| 2 | 2025-08-06 | 0 | 3931.74 | 1731.74 | 3334 | 3931.74 | 0 | (empty) |
| 3 | 2025-08-07 | -148.22 | 3783.52 | 1583.52 | 3185.78 | 3783.52 | 0 | event_1194 |
| 4 | 2025-08-08 | 0 | 3783.52 | 1583.52 | 3185.78 | 3783.52 | 0 | (empty) |
| 5 | 2025-08-09 | 0 | 3783.52 | 1583.52 | 3185.78 | 3783.52 | 0 | (empty) |
| 6 | 2025-08-10 | -104.8 | 3678.72 | 1478.72 | 3080.98 | 3678.72 | 0 | event_1226 |
| 7 | 2025-08-11 | -142.96 | 3535.76 | 1335.76 | 2938.02 | 3535.76 | 0 | event_1239, event_1196 |
| 8 | 2025-08-12 | -350 | 3185.76 | 985.76 | 2588.02 | 3185.76 | 0 | event_1195 |
| 9 | 2025-08-13 | -143.47 | 3042.29 | 842.29 | 2444.55 | 3042.29 | 0 | event_1198, event_1199 |
| 10 | 2025-08-14 | -226 | 2816.29 | 616.29 | 2218.55 | 2816.29 | 0 | event_1197 |
| 11 | 2025-08-15 | 2717 | 5533.29 | 3333.29 | 4935.55 | 5533.29 | 0 | event_1192 |
| 12 | 2025-08-16 | 0 | 5533.29 | 3333.29 | 4935.55 | 5533.29 | 0 | (empty) |
| 13 | 2025-08-17 | -104.8 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | event_1226 |
| 14 | 2025-08-18 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 15 | 2025-08-19 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 16 | 2025-08-20 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 17 | 2025-08-21 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 18 | 2025-08-22 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 19 | 2025-08-23 | 0 | 5428.49 | 3228.49 | 4830.75 | 5428.49 | 0 | (empty) |
| 20 | 2025-08-24 | -104.8 | 5323.69 | 3123.69 | 4725.95 | 5323.69 | 0 | event_1226 |
| 21 | 2025-08-25 | -51.06 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | event_1239 |
| 22 | 2025-08-26 | 0 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | (empty) |
| 23 | 2025-08-27 | 0 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | (empty) |
| 24 | 2025-08-28 | 0 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | (empty) |
| 25 | 2025-08-29 | 0 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | (empty) |
| 26 | 2025-08-30 | 0 | 5272.63 | 3072.63 | 4674.89 | 5272.63 | 0 | (empty) |
| 27 | 2025-08-31 | -104.8 | 5167.83 | 2967.83 | 4570.09 | 5167.83 | 0 | event_1226 |
| 28 | 2025-09-01 | 0 | 5167.83 | 2967.83 | 4570.09 | 5167.83 | 0 | (empty) |
| 29 | 2025-09-02 | 0 | 5167.83 | 2967.83 | 4570.09 | 5167.83 | 0 | (empty) |
| 30 | 2025-09-03 | -688.6 | 4479.23 | 2279.23 | 3881.49 | 4479.23 | 0 | event_1200 |
| 31 | 2025-09-04 | 0 | 4479.23 | 2279.23 | 3881.49 | 4479.23 | 0 | (empty) |
| 32 | 2025-09-05 | 0 | 4479.23 | 2279.23 | 3881.49 | 4479.23 | 0 | (empty) |
| 33 | 2025-09-06 | 0 | 4479.23 | 2279.23 | 3881.49 | 4479.23 | 0 | (empty) |
| 34 | 2025-09-07 | -253.02 | 4226.21 | 2026.21 | 3628.47 | 4226.21 | 0 | event_1226, event_1194 |
| 35 | 2025-09-08 | -51.06 | 4175.15 | 1975.15 | 3577.41 | 4175.15 | 0 | event_1239 |
| 36 | 2025-09-09 | 0 | 4175.15 | 1975.15 | 3577.41 | 4175.15 | 0 | (empty) |
| 37 | 2025-09-10 | 0 | 4175.15 | 1975.15 | 3577.41 | 4175.15 | 0 | (empty) |
| 38 | 2025-09-11 | -91.9 | 4083.25 | 1883.25 | 3485.51 | 4083.25 | 0 | event_1196 |
| 39 | 2025-09-12 | -350 | 3733.25 | 1533.25 | 3135.51 | 3733.25 | 0 | event_1195 |
| 40 | 2025-09-13 | -143.47 | 3589.78 | 1389.78 | 2992.04 | 3589.78 | 0 | event_1198, event_1199 |
| 41 | 2025-09-14 | -330.8 | 3258.98 | 1058.98 | 2661.24 | 3258.98 | 0 | event_1226, event_1197 |
| 42 | 2025-09-15 | 2717 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | event_1192 |
| 43 | 2025-09-16 | 0 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | (empty) |
| 44 | 2025-09-17 | 0 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | (empty) |
| 45 | 2025-09-18 | 0 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | (empty) |
| 46 | 2025-09-19 | 0 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | (empty) |
| 47 | 2025-09-20 | 0 | 5975.98 | 3775.98 | 5378.24 | 5975.98 | 0 | (empty) |
| 48 | 2025-09-21 | -104.8 | 5871.18 | 3671.18 | 5273.44 | 5871.18 | 0 | event_1226 |
| 49 | 2025-09-22 | -51.06 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | event_1239 |
| 50 | 2025-09-23 | 0 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | (empty) |
| 51 | 2025-09-24 | 0 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | (empty) |
| 52 | 2025-09-25 | 0 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | (empty) |
| 53 | 2025-09-26 | 0 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | (empty) |
| 54 | 2025-09-27 | 0 | 5820.12 | 3620.12 | 5222.38 | 5820.12 | 0 | (empty) |
| 55 | 2025-09-28 | -104.8 | 5715.32 | 3515.32 | 5117.58 | 5715.32 | 0 | event_1226 |
| 56 | 2025-09-29 | 0 | 5715.32 | 3515.32 | 5117.58 | 5715.32 | 0 | (empty) |
| 57 | 2025-09-30 | 0 | 5715.32 | 3515.32 | 5117.58 | 5715.32 | 0 | (empty) |
| 58 | 2025-10-01 | 0 | 5715.32 | 3515.32 | 5117.58 | 5715.32 | 0 | (empty) |
| 59 | 2025-10-02 | 0 | 5715.32 | 3515.32 | 5117.58 | 5715.32 | 0 | (empty) |
| 60 | 2025-10-03 | -688.6 | 5026.72 | 2826.72 | 4428.98 | 5026.72 | 0 | event_1200 |
| 61 | 2025-10-04 | 0 | 5026.72 | 2826.72 | 4428.98 | 5026.72 | 0 | (empty) |
| 62 | 2025-10-05 | -104.8 | 4921.92 | 2721.92 | 4324.18 | 4921.92 | 0 | event_1226 |
| 63 | 2025-10-06 | -51.06 | 4870.86 | 2670.86 | 4273.12 | 4870.86 | 0 | event_1239 |
| 64 | 2025-10-07 | -148.22 | 4722.64 | 2522.64 | 4124.9 | 4722.64 | 0 | event_1194 |
| 65 | 2025-10-08 | 0 | 4722.64 | 2522.64 | 4124.9 | 4722.64 | 0 | (empty) |
| 66 | 2025-10-09 | 0 | 4722.64 | 2522.64 | 4124.9 | 4722.64 | 0 | (empty) |
| 67 | 2025-10-10 | 0 | 4722.64 | 2522.64 | 4124.9 | 4722.64 | 0 | (empty) |
| 68 | 2025-10-11 | -91.9 | 4630.74 | 2430.74 | 4033 | 4630.74 | 0 | event_1196 |
| 69 | 2025-10-12 | -454.8 | 4175.94 | 1975.94 | 3578.2 | 4175.94 | 0 | event_1226, event_1195 |
| 70 | 2025-10-13 | -143.47 | 4032.47 | 1832.47 | 3434.73 | 4032.47 | 0 | event_1198, event_1199 |
| 71 | 2025-10-14 | -226 | 3806.47 | 1606.47 | 3208.73 | 3806.47 | 0 | event_1197 |
| 72 | 2025-10-15 | 2717 | 6523.47 | 4323.47 | 5925.73 | 6523.47 | 0 | event_1192 |
| 73 | 2025-10-16 | 0 | 6523.47 | 4323.47 | 5925.73 | 6523.47 | 0 | (empty) |
| 74 | 2025-10-17 | 0 | 6523.47 | 4323.47 | 5925.73 | 6523.47 | 0 | (empty) |
| 75 | 2025-10-18 | 0 | 6523.47 | 4323.47 | 5925.73 | 6523.47 | 0 | (empty) |
| 76 | 2025-10-19 | -104.8 | 6418.67 | 4218.67 | 5820.93 | 6418.67 | 0 | event_1226 |
| 77 | 2025-10-20 | -51.06 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | event_1239 |
| 78 | 2025-10-21 | 0 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | (empty) |
| 79 | 2025-10-22 | 0 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | (empty) |
| 80 | 2025-10-23 | 0 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | (empty) |
| 81 | 2025-10-24 | 0 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | (empty) |
| 82 | 2025-10-25 | 0 | 6367.61 | 4167.61 | 5769.87 | 6367.61 | 0 | (empty) |
| 83 | 2025-10-26 | -104.8 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | event_1226 |
| 84 | 2025-10-27 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 85 | 2025-10-28 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 86 | 2025-10-29 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 87 | 2025-10-30 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 88 | 2025-10-31 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 89 | 2025-11-01 | 0 | 6262.81 | 4062.81 | 5665.07 | 6262.81 | 0 | (empty) |
| 90 | 2025-11-02 | -104.8 | 6158.01 | 3958.01 | 5560.27 | 6158.01 | 0 | event_1226 |

## request_15 â€” user_15 (EUR)

Request: 3685 on 2026-01-06; deadline 2026-02-01. Opening 1770.05; minimum 1200.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 83.05 | 5.08 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 8 (2026-01-14), balance 1205.08, headroom 5.08.

Protected: rent|education|groceries|debt_repayment. Reduce: dining. Stop: .

Salary mode: new_job. Evidence: message_11. Unparsed messages: none.

- message_11 (employer, 2026-01-03T09:30:00Z): A quick update from the payroll team at Riverline Retail. Your first salary will be EUR 1661. The confirmed credit date is 2026-01-15. The money will appear after the bank posts the credit. Payroll ref EMP-0011.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1269 | debt_repayment / Credit card repayment | 5 / 5 | 84 | 84.00 | 84â€“84 | 84 | 2026-01-13, 2026-02-13, 2026-03-13 |
| event_1271 | delivery_membership / Food delivery membership | 5 / 5 | 27 | 27.00 | 27â€“27 | 27 | 2026-01-15, 2026-02-15, 2026-03-15 |
| event_1335 | dining / Bakery and snacks | 13 / 6 | 40.83538461538461538461538462 | 38.56 | 32.17â€“53.58 | 40.84 | 2026-01-10, 2026-01-24, 2026-02-07, 2026-02-21, 2026-03-07, 2026-03-21, 2026-04-04 |
| event_1268 | education / School fee payment | 5 / 5 | 159 | 159.00 | 159â€“159 | 159 | 2026-01-10, 2026-02-10, 2026-03-10 |
| event_1297 | groceries / Local market purchase | 25 / 6 | 60.1084 | 62.21 | 46.76â€“73.5 | 60.11 | 2026-01-06, 2026-01-13, 2026-01-20, 2026-01-27, 2026-02-03, 2026-02-10, 2026-02-17, 2026-02-24, 2026-03-03, 2026-03-10, 2026-03-17, 2026-03-24, 2026-03-31 |
| event_1270 | music_subscription / Music subscription | 5 / 5 | 11 | 11.00 | 11â€“11 | 11 | 2026-01-13, 2026-02-13, 2026-03-13 |
| event_1272 | rent / Landlord standing order | 6 / 6 | 435.6 | 435.60 | 435.6â€“435.6 | 435.6 | 2026-02-04, 2026-03-04, 2026-04-04 |
| event_1322 | transport / Ride-hailing trip | 25 / 6 | 31.7572 | 30.31 | 25.11â€“42.66 | 31.76 | 2026-01-07, 2026-01-14, 2026-01-21, 2026-01-28, 2026-02-04, 2026-02-11, 2026-02-18, 2026-02-25, 2026-03-04, 2026-03-11, 2026-03-18, 2026-03-25, 2026-04-01 |
| event_1267 | utilities / Energy provider bill | 5 / 5 | 86.394 | 85.91 | 84.12â€“90.39 | 86.39 | 2026-01-08, 2026-02-08, 2026-03-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-01-06 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-01-07 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-01-08 | -86.39 | event_1267 | utilities | recurring_expense | Energy provider bill |
| 2026-01-10 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-01-10 | -159 | event_1268 | education | recurring_expense | School fee payment |
| 2026-01-13 | -11 | event_1270 | music_subscription | recurring_expense | Music subscription |
| 2026-01-13 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-01-13 | -84 | event_1269 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-01-14 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-01-15 | 1661 | event_1265 | salary | recurring_income | First-job payroll |
| 2026-01-15 | -27 | event_1271 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-01-20 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-01-21 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-01-24 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-01-27 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-01-28 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-02-03 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-02-04 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-02-04 | -435.6 | event_1272 | rent | recurring_expense | Landlord standing order |
| 2026-02-07 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-02-08 | -86.39 | event_1267 | utilities | recurring_expense | Energy provider bill |
| 2026-02-10 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-02-10 | -159 | event_1268 | education | recurring_expense | School fee payment |
| 2026-02-11 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-02-13 | -11 | event_1270 | music_subscription | recurring_expense | Music subscription |
| 2026-02-13 | -84 | event_1269 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-02-15 | 1661 | event_1265 | salary | recurring_income | First-job payroll |
| 2026-02-15 | -27 | event_1271 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-02-17 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-02-18 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-02-21 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-02-24 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-02-25 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-03-03 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-03-04 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-03-04 | -435.6 | event_1272 | rent | recurring_expense | Landlord standing order |
| 2026-03-07 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-03-08 | -86.39 | event_1267 | utilities | recurring_expense | Energy provider bill |
| 2026-03-10 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-03-10 | -159 | event_1268 | education | recurring_expense | School fee payment |
| 2026-03-11 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-03-13 | -11 | event_1270 | music_subscription | recurring_expense | Music subscription |
| 2026-03-13 | -84 | event_1269 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-03-15 | 1661 | event_1265 | salary | recurring_income | First-job payroll |
| 2026-03-15 | -27 | event_1271 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-03-17 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-03-18 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-03-21 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-03-24 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-03-25 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-03-31 | -60.11 | event_1297 | groceries | recurring_expense | Local market purchase |
| 2026-04-01 | -31.76 | event_1322 | transport | recurring_expense | Ride-hailing trip |
| 2026-04-04 | -40.84 | event_1335 | dining | recurring_expense | Bakery and snacks |
| 2026-04-04 | -435.6 | event_1272 | rent | recurring_expense | Landlord standing order |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-01-06 | -60.11 | 1709.94 | 509.94 | 1626.89 | 1709.94 | 0 | event_1297 |
| 1 | 2026-01-07 | -31.76 | 1678.18 | 478.18 | 1595.13 | 1678.18 | 0 | event_1322 |
| 2 | 2026-01-08 | -86.39 | 1591.79 | 391.79 | 1508.74 | 1591.79 | 0 | event_1267 |
| 3 | 2026-01-09 | 0 | 1591.79 | 391.79 | 1508.74 | 1591.79 | 0 | (empty) |
| 4 | 2026-01-10 | -199.84 | 1391.95 | 191.95 | 1308.9 | 1391.95 | 0 | event_1335, event_1268 |
| 5 | 2026-01-11 | 0 | 1391.95 | 191.95 | 1308.9 | 1391.95 | 0 | (empty) |
| 6 | 2026-01-12 | 0 | 1391.95 | 191.95 | 1308.9 | 1391.95 | 0 | (empty) |
| 7 | 2026-01-13 | -155.11 | 1236.84 | 36.84 | 1153.79 | 1236.84 | 0 | event_1270, event_1297, event_1269 |
| 8 | 2026-01-14 | -31.76 | 1205.08 | 5.08 | 1122.03 | 1205.08 | 0 | event_1322 |
| 9 | 2026-01-15 | 1634 | 2839.08 | 1639.08 | 2756.03 | 2839.08 | 0 | event_1265, event_1271 |
| 10 | 2026-01-16 | 0 | 2839.08 | 1639.08 | 2756.03 | 2839.08 | 0 | (empty) |
| 11 | 2026-01-17 | 0 | 2839.08 | 1639.08 | 2756.03 | 2839.08 | 0 | (empty) |
| 12 | 2026-01-18 | 0 | 2839.08 | 1639.08 | 2756.03 | 2839.08 | 0 | (empty) |
| 13 | 2026-01-19 | 0 | 2839.08 | 1639.08 | 2756.03 | 2839.08 | 0 | (empty) |
| 14 | 2026-01-20 | -60.11 | 2778.97 | 1578.97 | 2695.92 | 2778.97 | 0 | event_1297 |
| 15 | 2026-01-21 | -31.76 | 2747.21 | 1547.21 | 2664.16 | 2747.21 | 0 | event_1322 |
| 16 | 2026-01-22 | 0 | 2747.21 | 1547.21 | 2664.16 | 2747.21 | 0 | (empty) |
| 17 | 2026-01-23 | 0 | 2747.21 | 1547.21 | 2664.16 | 2747.21 | 0 | (empty) |
| 18 | 2026-01-24 | -40.84 | 2706.37 | 1506.37 | 2623.32 | 2706.37 | 0 | event_1335 |
| 19 | 2026-01-25 | 0 | 2706.37 | 1506.37 | 2623.32 | 2706.37 | 0 | (empty) |
| 20 | 2026-01-26 | 0 | 2706.37 | 1506.37 | 2623.32 | 2706.37 | 0 | (empty) |
| 21 | 2026-01-27 | -60.11 | 2646.26 | 1446.26 | 2563.21 | 2646.26 | 0 | event_1297 |
| 22 | 2026-01-28 | -31.76 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | event_1322 |
| 23 | 2026-01-29 | 0 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | (empty) |
| 24 | 2026-01-30 | 0 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | (empty) |
| 25 | 2026-01-31 | 0 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | (empty) |
| 26 | 2026-02-01 | 0 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | (empty) |
| 27 | 2026-02-02 | 0 | 2614.5 | 1414.5 | 2531.45 | 2614.5 | 0 | (empty) |
| 28 | 2026-02-03 | -60.11 | 2554.39 | 1354.39 | 2471.34 | 2554.39 | 0 | event_1297 |
| 29 | 2026-02-04 | -467.36 | 2087.03 | 887.03 | 2003.98 | 2087.03 | 0 | event_1322, event_1272 |
| 30 | 2026-02-05 | 0 | 2087.03 | 887.03 | 2003.98 | 2087.03 | 0 | (empty) |
| 31 | 2026-02-06 | 0 | 2087.03 | 887.03 | 2003.98 | 2087.03 | 0 | (empty) |
| 32 | 2026-02-07 | -40.84 | 2046.19 | 846.19 | 1963.14 | 2046.19 | 0 | event_1335 |
| 33 | 2026-02-08 | -86.39 | 1959.8 | 759.8 | 1876.75 | 1959.8 | 0 | event_1267 |
| 34 | 2026-02-09 | 0 | 1959.8 | 759.8 | 1876.75 | 1959.8 | 0 | (empty) |
| 35 | 2026-02-10 | -219.11 | 1740.69 | 540.69 | 1657.64 | 1740.69 | 0 | event_1297, event_1268 |
| 36 | 2026-02-11 | -31.76 | 1708.93 | 508.93 | 1625.88 | 1708.93 | 0 | event_1322 |
| 37 | 2026-02-12 | 0 | 1708.93 | 508.93 | 1625.88 | 1708.93 | 0 | (empty) |
| 38 | 2026-02-13 | -95 | 1613.93 | 413.93 | 1530.88 | 1613.93 | 0 | event_1270, event_1269 |
| 39 | 2026-02-14 | 0 | 1613.93 | 413.93 | 1530.88 | 1613.93 | 0 | (empty) |
| 40 | 2026-02-15 | 1634 | 3247.93 | 2047.93 | 3164.88 | 3247.93 | 0 | event_1265, event_1271 |
| 41 | 2026-02-16 | 0 | 3247.93 | 2047.93 | 3164.88 | 3247.93 | 0 | (empty) |
| 42 | 2026-02-17 | -60.11 | 3187.82 | 1987.82 | 3104.77 | 3187.82 | 0 | event_1297 |
| 43 | 2026-02-18 | -31.76 | 3156.06 | 1956.06 | 3073.01 | 3156.06 | 0 | event_1322 |
| 44 | 2026-02-19 | 0 | 3156.06 | 1956.06 | 3073.01 | 3156.06 | 0 | (empty) |
| 45 | 2026-02-20 | 0 | 3156.06 | 1956.06 | 3073.01 | 3156.06 | 0 | (empty) |
| 46 | 2026-02-21 | -40.84 | 3115.22 | 1915.22 | 3032.17 | 3115.22 | 0 | event_1335 |
| 47 | 2026-02-22 | 0 | 3115.22 | 1915.22 | 3032.17 | 3115.22 | 0 | (empty) |
| 48 | 2026-02-23 | 0 | 3115.22 | 1915.22 | 3032.17 | 3115.22 | 0 | (empty) |
| 49 | 2026-02-24 | -60.11 | 3055.11 | 1855.11 | 2972.06 | 3055.11 | 0 | event_1297 |
| 50 | 2026-02-25 | -31.76 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | event_1322 |
| 51 | 2026-02-26 | 0 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | (empty) |
| 52 | 2026-02-27 | 0 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | (empty) |
| 53 | 2026-02-28 | 0 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | (empty) |
| 54 | 2026-03-01 | 0 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | (empty) |
| 55 | 2026-03-02 | 0 | 3023.35 | 1823.35 | 2940.3 | 3023.35 | 0 | (empty) |
| 56 | 2026-03-03 | -60.11 | 2963.24 | 1763.24 | 2880.19 | 2963.24 | 0 | event_1297 |
| 57 | 2026-03-04 | -467.36 | 2495.88 | 1295.88 | 2412.83 | 2495.88 | 0 | event_1322, event_1272 |
| 58 | 2026-03-05 | 0 | 2495.88 | 1295.88 | 2412.83 | 2495.88 | 0 | (empty) |
| 59 | 2026-03-06 | 0 | 2495.88 | 1295.88 | 2412.83 | 2495.88 | 0 | (empty) |
| 60 | 2026-03-07 | -40.84 | 2455.04 | 1255.04 | 2371.99 | 2455.04 | 0 | event_1335 |
| 61 | 2026-03-08 | -86.39 | 2368.65 | 1168.65 | 2285.6 | 2368.65 | 0 | event_1267 |
| 62 | 2026-03-09 | 0 | 2368.65 | 1168.65 | 2285.6 | 2368.65 | 0 | (empty) |
| 63 | 2026-03-10 | -219.11 | 2149.54 | 949.54 | 2066.49 | 2149.54 | 0 | event_1297, event_1268 |
| 64 | 2026-03-11 | -31.76 | 2117.78 | 917.78 | 2034.73 | 2117.78 | 0 | event_1322 |
| 65 | 2026-03-12 | 0 | 2117.78 | 917.78 | 2034.73 | 2117.78 | 0 | (empty) |
| 66 | 2026-03-13 | -95 | 2022.78 | 822.78 | 1939.73 | 2022.78 | 0 | event_1270, event_1269 |
| 67 | 2026-03-14 | 0 | 2022.78 | 822.78 | 1939.73 | 2022.78 | 0 | (empty) |
| 68 | 2026-03-15 | 1634 | 3656.78 | 2456.78 | 3573.73 | 3656.78 | 0 | event_1265, event_1271 |
| 69 | 2026-03-16 | 0 | 3656.78 | 2456.78 | 3573.73 | 3656.78 | 0 | (empty) |
| 70 | 2026-03-17 | -60.11 | 3596.67 | 2396.67 | 3513.62 | 3596.67 | 0 | event_1297 |
| 71 | 2026-03-18 | -31.76 | 3564.91 | 2364.91 | 3481.86 | 3564.91 | 0 | event_1322 |
| 72 | 2026-03-19 | 0 | 3564.91 | 2364.91 | 3481.86 | 3564.91 | 0 | (empty) |
| 73 | 2026-03-20 | 0 | 3564.91 | 2364.91 | 3481.86 | 3564.91 | 0 | (empty) |
| 74 | 2026-03-21 | -40.84 | 3524.07 | 2324.07 | 3441.02 | 3524.07 | 0 | event_1335 |
| 75 | 2026-03-22 | 0 | 3524.07 | 2324.07 | 3441.02 | 3524.07 | 0 | (empty) |
| 76 | 2026-03-23 | 0 | 3524.07 | 2324.07 | 3441.02 | 3524.07 | 0 | (empty) |
| 77 | 2026-03-24 | -60.11 | 3463.96 | 2263.96 | 3380.91 | 3463.96 | 0 | event_1297 |
| 78 | 2026-03-25 | -31.76 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | event_1322 |
| 79 | 2026-03-26 | 0 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | (empty) |
| 80 | 2026-03-27 | 0 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | (empty) |
| 81 | 2026-03-28 | 0 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | (empty) |
| 82 | 2026-03-29 | 0 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | (empty) |
| 83 | 2026-03-30 | 0 | 3432.2 | 2232.2 | 3349.15 | 3432.2 | 0 | (empty) |
| 84 | 2026-03-31 | -60.11 | 3372.09 | 2172.09 | 3289.04 | 3372.09 | 0 | event_1297 |
| 85 | 2026-04-01 | -31.76 | 3340.33 | 2140.33 | 3257.28 | 3340.33 | 0 | event_1322 |
| 86 | 2026-04-02 | 0 | 3340.33 | 2140.33 | 3257.28 | 3340.33 | 0 | (empty) |
| 87 | 2026-04-03 | 0 | 3340.33 | 2140.33 | 3257.28 | 3340.33 | 0 | (empty) |
| 88 | 2026-04-04 | -476.44 | 2863.89 | 1663.89 | 2780.84 | 2863.89 | 0 | event_1335, event_1272 |
| 89 | 2026-04-05 | 0 | 2863.89 | 1663.89 | 2780.84 | 2863.89 | 0 | (empty) |
| 90 | 2026-04-06 | 0 | 2863.89 | 1663.89 | 2780.84 | 2863.89 | 0 | (empty) |

## request_16 â€” user_16 (INR)

Request: 122500 on 2023-08-12; deadline 2023-10-11. Opening 362370; minimum 122400.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 122500 | 122500 | yes |
| affordability_status | affordable_now | affordable_now | yes |
| recommended_payment_method | full_payment | full_payment | yes |
| payment_plan | 2023-08-12:122500 | 2023-08-12:122500 | yes |
| earliest_date_for_full_payment | 2023-08-12 | 2023-08-12 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 33 (2023-09-14), balance 272115.53, headroom 149715.53.

Protected: rent|groceries|transport. Reduce: . Stop: .

Salary mode: historical. Evidence: message_12. Unparsed messages: none.

- message_12 (service_provider, 2023-08-01T09:30:00Z): StayLedger wanted to let you know about a change on your account. The renewed lease increases monthly rent by 12%. The new amount will be used for the next rent payment. Case ref SER-0012.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1375 | cloud_storage / Cloud storage plan | 6 / 6 | 1055 | 1055.00 | 1055â€“1055 | 1055 | 2023-09-11, 2023-10-11 |
| event_1373 | debt_repayment / Vehicle loan payment | 6 / 6 | 17750 | 17750.00 | 17750â€“17750 | 17750 | 2023-09-10, 2023-10-10, 2023-11-10 |
| event_1402 | groceries / Neighbourhood grocer | 26 / 7 | 7060.631538461538461538461538 | 6843.69 | 5364.38â€“9111.36 | 7060.63 | 2023-08-16, 2023-08-23, 2023-08-30, 2023-09-06, 2023-09-13, 2023-09-20, 2023-09-27, 2023-10-04, 2023-10-11, 2023-10-18, 2023-10-25, 2023-11-01, 2023-11-08 |
| event_1371 | rent / Monthly rent | 6 / 6 | 57100 | 57100.00 | 57100â€“57100 | 63952 | 2023-09-01, 2023-10-01, 2023-11-01 |
| event_1376 | shopping / Clothing and household items | 6 / 6 | 9179.843333333333333333333333 | 9096.16 | 8414.47â€“10178.56 | 9179.84 | 2023-09-11, 2023-10-11 |
| event_1374 | streaming / Video streaming plan | 6 / 6 | 3510 | 3510.00 | 3510â€“3510 | 3510 | 2023-09-08, 2023-10-08, 2023-11-08 |
| event_1428 | transport / Parking and tolls | 26 / 7 | 4419.413461538461538461538462 | 4432.915 | 3143.71â€“5368.95 | 4419.41 | 2023-08-17, 2023-08-24, 2023-08-31, 2023-09-07, 2023-09-14, 2023-09-21, 2023-09-28, 2023-10-05, 2023-10-12, 2023-10-19, 2023-10-26, 2023-11-02, 2023-11-09 |
| event_1372 | utilities / Energy provider bill | 6 / 6 | 10407.43166666666666666666667 | 10299.645 | 9402.67â€“11512.87 | 10407.43 | 2023-09-05, 2023-10-05, 2023-11-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2023-08-15 | 173000 | event_1364 | salary | recurring_income | Payroll credit |
| 2023-08-16 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-08-16 | -100000 | event_1442 | rent | explicit_event | Outstanding rent balance |
| 2023-08-17 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-08-23 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-08-24 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-08-30 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-08-31 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-09-01 | -63952 | event_1371 | rent | recurring_expense | Monthly rent |
| 2023-09-05 | -10407.43 | event_1372 | utilities | recurring_expense | Energy provider bill |
| 2023-09-06 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-09-07 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-09-08 | -3510 | event_1374 | streaming | recurring_expense | Video streaming plan |
| 2023-09-10 | -17750 | event_1373 | debt_repayment | recurring_expense | Vehicle loan payment |
| 2023-09-11 | -1055 | event_1375 | cloud_storage | recurring_expense | Cloud storage plan |
| 2023-09-11 | -9179.84 | event_1376 | shopping | recurring_expense | Clothing and household items |
| 2023-09-13 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-09-14 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-09-15 | 173000 | event_1364 | salary | recurring_income | Payroll credit |
| 2023-09-20 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-09-21 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-09-27 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-09-28 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-10-01 | -63952 | event_1371 | rent | recurring_expense | Monthly rent |
| 2023-10-04 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-10-05 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-10-05 | -10407.43 | event_1372 | utilities | recurring_expense | Energy provider bill |
| 2023-10-08 | -3510 | event_1374 | streaming | recurring_expense | Video streaming plan |
| 2023-10-10 | -17750 | event_1373 | debt_repayment | recurring_expense | Vehicle loan payment |
| 2023-10-11 | -1055 | event_1375 | cloud_storage | recurring_expense | Cloud storage plan |
| 2023-10-11 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-10-11 | -9179.84 | event_1376 | shopping | recurring_expense | Clothing and household items |
| 2023-10-12 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-10-15 | 173000 | event_1364 | salary | recurring_income | Payroll credit |
| 2023-10-18 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-10-19 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-10-25 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-10-26 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-11-01 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-11-01 | -63952 | event_1371 | rent | recurring_expense | Monthly rent |
| 2023-11-02 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-11-05 | -10407.43 | event_1372 | utilities | recurring_expense | Energy provider bill |
| 2023-11-08 | -3510 | event_1374 | streaming | recurring_expense | Video streaming plan |
| 2023-11-08 | -7060.63 | event_1402 | groceries | recurring_expense | Neighbourhood grocer |
| 2023-11-09 | -4419.41 | event_1428 | transport | recurring_expense | Parking and tolls |
| 2023-11-10 | -17750 | event_1373 | debt_repayment | recurring_expense | Vehicle loan payment |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2023-08-12 | 0 | 362370 | 239970 | 239870 | 239870 | 122500 | (empty) |
| 1 | 2023-08-13 | 0 | 362370 | 239970 | 239870 | 239870 | 0 | (empty) |
| 2 | 2023-08-14 | 0 | 362370 | 239970 | 239870 | 239870 | 0 | (empty) |
| 3 | 2023-08-15 | 173000 | 535370 | 412970 | 412870 | 412870 | 0 | event_1364 |
| 4 | 2023-08-16 | -107060.63 | 428309.37 | 305909.37 | 305809.37 | 305809.37 | 0 | event_1402, event_1442 |
| 5 | 2023-08-17 | -4419.41 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | event_1428 |
| 6 | 2023-08-18 | 0 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | (empty) |
| 7 | 2023-08-19 | 0 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | (empty) |
| 8 | 2023-08-20 | 0 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | (empty) |
| 9 | 2023-08-21 | 0 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | (empty) |
| 10 | 2023-08-22 | 0 | 423889.96 | 301489.96 | 301389.96 | 301389.96 | 0 | (empty) |
| 11 | 2023-08-23 | -7060.63 | 416829.33 | 294429.33 | 294329.33 | 294329.33 | 0 | event_1402 |
| 12 | 2023-08-24 | -4419.41 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | event_1428 |
| 13 | 2023-08-25 | 0 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | (empty) |
| 14 | 2023-08-26 | 0 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | (empty) |
| 15 | 2023-08-27 | 0 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | (empty) |
| 16 | 2023-08-28 | 0 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | (empty) |
| 17 | 2023-08-29 | 0 | 412409.92 | 290009.92 | 289909.92 | 289909.92 | 0 | (empty) |
| 18 | 2023-08-30 | -7060.63 | 405349.29 | 282949.29 | 282849.29 | 282849.29 | 0 | event_1402 |
| 19 | 2023-08-31 | -4419.41 | 400929.88 | 278529.88 | 278429.88 | 278429.88 | 0 | event_1428 |
| 20 | 2023-09-01 | -63952 | 336977.88 | 214577.88 | 214477.88 | 214477.88 | 0 | event_1371 |
| 21 | 2023-09-02 | 0 | 336977.88 | 214577.88 | 214477.88 | 214477.88 | 0 | (empty) |
| 22 | 2023-09-03 | 0 | 336977.88 | 214577.88 | 214477.88 | 214477.88 | 0 | (empty) |
| 23 | 2023-09-04 | 0 | 336977.88 | 214577.88 | 214477.88 | 214477.88 | 0 | (empty) |
| 24 | 2023-09-05 | -10407.43 | 326570.45 | 204170.45 | 204070.45 | 204070.45 | 0 | event_1372 |
| 25 | 2023-09-06 | -7060.63 | 319509.82 | 197109.82 | 197009.82 | 197009.82 | 0 | event_1402 |
| 26 | 2023-09-07 | -4419.41 | 315090.41 | 192690.41 | 192590.41 | 192590.41 | 0 | event_1428 |
| 27 | 2023-09-08 | -3510 | 311580.41 | 189180.41 | 189080.41 | 189080.41 | 0 | event_1374 |
| 28 | 2023-09-09 | 0 | 311580.41 | 189180.41 | 189080.41 | 189080.41 | 0 | (empty) |
| 29 | 2023-09-10 | -17750 | 293830.41 | 171430.41 | 171330.41 | 171330.41 | 0 | event_1373 |
| 30 | 2023-09-11 | -10234.84 | 283595.57 | 161195.57 | 161095.57 | 161095.57 | 0 | event_1375, event_1376 |
| 31 | 2023-09-12 | 0 | 283595.57 | 161195.57 | 161095.57 | 161095.57 | 0 | (empty) |
| 32 | 2023-09-13 | -7060.63 | 276534.94 | 154134.94 | 154034.94 | 154034.94 | 0 | event_1402 |
| 33 | 2023-09-14 | -4419.41 | 272115.53 | 149715.53 | 149615.53 | 149615.53 | 0 | event_1428 |
| 34 | 2023-09-15 | 173000 | 445115.53 | 322715.53 | 322615.53 | 322615.53 | 0 | event_1364 |
| 35 | 2023-09-16 | 0 | 445115.53 | 322715.53 | 322615.53 | 322615.53 | 0 | (empty) |
| 36 | 2023-09-17 | 0 | 445115.53 | 322715.53 | 322615.53 | 322615.53 | 0 | (empty) |
| 37 | 2023-09-18 | 0 | 445115.53 | 322715.53 | 322615.53 | 322615.53 | 0 | (empty) |
| 38 | 2023-09-19 | 0 | 445115.53 | 322715.53 | 322615.53 | 322615.53 | 0 | (empty) |
| 39 | 2023-09-20 | -7060.63 | 438054.9 | 315654.9 | 315554.9 | 315554.9 | 0 | event_1402 |
| 40 | 2023-09-21 | -4419.41 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | event_1428 |
| 41 | 2023-09-22 | 0 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | (empty) |
| 42 | 2023-09-23 | 0 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | (empty) |
| 43 | 2023-09-24 | 0 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | (empty) |
| 44 | 2023-09-25 | 0 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | (empty) |
| 45 | 2023-09-26 | 0 | 433635.49 | 311235.49 | 311135.49 | 311135.49 | 0 | (empty) |
| 46 | 2023-09-27 | -7060.63 | 426574.86 | 304174.86 | 304074.86 | 304074.86 | 0 | event_1402 |
| 47 | 2023-09-28 | -4419.41 | 422155.45 | 299755.45 | 299655.45 | 299655.45 | 0 | event_1428 |
| 48 | 2023-09-29 | 0 | 422155.45 | 299755.45 | 299655.45 | 299655.45 | 0 | (empty) |
| 49 | 2023-09-30 | 0 | 422155.45 | 299755.45 | 299655.45 | 299655.45 | 0 | (empty) |
| 50 | 2023-10-01 | -63952 | 358203.45 | 235803.45 | 235703.45 | 235703.45 | 0 | event_1371 |
| 51 | 2023-10-02 | 0 | 358203.45 | 235803.45 | 235703.45 | 235703.45 | 0 | (empty) |
| 52 | 2023-10-03 | 0 | 358203.45 | 235803.45 | 235703.45 | 235703.45 | 0 | (empty) |
| 53 | 2023-10-04 | -7060.63 | 351142.82 | 228742.82 | 228642.82 | 228642.82 | 0 | event_1402 |
| 54 | 2023-10-05 | -14826.84 | 336315.98 | 213915.98 | 213815.98 | 213815.98 | 0 | event_1428, event_1372 |
| 55 | 2023-10-06 | 0 | 336315.98 | 213915.98 | 213815.98 | 213815.98 | 0 | (empty) |
| 56 | 2023-10-07 | 0 | 336315.98 | 213915.98 | 213815.98 | 213815.98 | 0 | (empty) |
| 57 | 2023-10-08 | -3510 | 332805.98 | 210405.98 | 210305.98 | 210305.98 | 0 | event_1374 |
| 58 | 2023-10-09 | 0 | 332805.98 | 210405.98 | 210305.98 | 210305.98 | 0 | (empty) |
| 59 | 2023-10-10 | -17750 | 315055.98 | 192655.98 | 192555.98 | 192555.98 | 0 | event_1373 |
| 60 | 2023-10-11 | -17295.47 | 297760.51 | 175360.51 | 175260.51 | 175260.51 | 0 | event_1375, event_1402, event_1376 |
| 61 | 2023-10-12 | -4419.41 | 293341.1 | 170941.1 | 170841.1 | 170841.1 | 0 | event_1428 |
| 62 | 2023-10-13 | 0 | 293341.1 | 170941.1 | 170841.1 | 170841.1 | 0 | (empty) |
| 63 | 2023-10-14 | 0 | 293341.1 | 170941.1 | 170841.1 | 170841.1 | 0 | (empty) |
| 64 | 2023-10-15 | 173000 | 466341.1 | 343941.1 | 343841.1 | 343841.1 | 0 | event_1364 |
| 65 | 2023-10-16 | 0 | 466341.1 | 343941.1 | 343841.1 | 343841.1 | 0 | (empty) |
| 66 | 2023-10-17 | 0 | 466341.1 | 343941.1 | 343841.1 | 343841.1 | 0 | (empty) |
| 67 | 2023-10-18 | -7060.63 | 459280.47 | 336880.47 | 336780.47 | 336780.47 | 0 | event_1402 |
| 68 | 2023-10-19 | -4419.41 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | event_1428 |
| 69 | 2023-10-20 | 0 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | (empty) |
| 70 | 2023-10-21 | 0 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | (empty) |
| 71 | 2023-10-22 | 0 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | (empty) |
| 72 | 2023-10-23 | 0 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | (empty) |
| 73 | 2023-10-24 | 0 | 454861.06 | 332461.06 | 332361.06 | 332361.06 | 0 | (empty) |
| 74 | 2023-10-25 | -7060.63 | 447800.43 | 325400.43 | 325300.43 | 325300.43 | 0 | event_1402 |
| 75 | 2023-10-26 | -4419.41 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | event_1428 |
| 76 | 2023-10-27 | 0 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | (empty) |
| 77 | 2023-10-28 | 0 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | (empty) |
| 78 | 2023-10-29 | 0 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | (empty) |
| 79 | 2023-10-30 | 0 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | (empty) |
| 80 | 2023-10-31 | 0 | 443381.02 | 320981.02 | 320881.02 | 320881.02 | 0 | (empty) |
| 81 | 2023-11-01 | -71012.63 | 372368.39 | 249968.39 | 249868.39 | 249868.39 | 0 | event_1402, event_1371 |
| 82 | 2023-11-02 | -4419.41 | 367948.98 | 245548.98 | 245448.98 | 245448.98 | 0 | event_1428 |
| 83 | 2023-11-03 | 0 | 367948.98 | 245548.98 | 245448.98 | 245448.98 | 0 | (empty) |
| 84 | 2023-11-04 | 0 | 367948.98 | 245548.98 | 245448.98 | 245448.98 | 0 | (empty) |
| 85 | 2023-11-05 | -10407.43 | 357541.55 | 235141.55 | 235041.55 | 235041.55 | 0 | event_1372 |
| 86 | 2023-11-06 | 0 | 357541.55 | 235141.55 | 235041.55 | 235041.55 | 0 | (empty) |
| 87 | 2023-11-07 | 0 | 357541.55 | 235141.55 | 235041.55 | 235041.55 | 0 | (empty) |
| 88 | 2023-11-08 | -10570.63 | 346970.92 | 224570.92 | 224470.92 | 224470.92 | 0 | event_1374, event_1402 |
| 89 | 2023-11-09 | -4419.41 | 342551.51 | 220151.51 | 220051.51 | 220051.51 | 0 | event_1428 |
| 90 | 2023-11-10 | -17750 | 324801.51 | 202401.51 | 202301.51 | 202301.51 | 0 | event_1373 |

## request_17 â€” user_17 (INR)

Request: 274600 on 2026-03-01; deadline 2026-05-04. Opening 550379.58; minimum 166100.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 243849.58 | 243023.67 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | installments | installments | yes |
| payment_plan | 2026-03-01:95194.67\|2026-03-31:95194.67\|2026-04-30:95194.67 | 2026-03-01:95194.67\|2026-03-31:95194.67\|2026-04-30:95194.67 | yes |
| earliest_date_for_full_payment | 2026-03-15 | 2026-04-15 | NO |
| spending_changes_needed | none | none | yes |

Baseline trough: day 13 (2026-03-14), balance 409123.67, headroom 243023.67.

Protected: rent|education|groceries|debt_repayment. Reduce: dining. Stop: music_subscription|delivery_membership.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1475 | debt_repayment / Credit card repayment | 5 / 5 | 30200 | 30200.00 | 30200â€“30200 | 30200 | 2026-03-11, 2026-04-11, 2026-05-11 |
| event_1477 | delivery_membership / Food delivery membership | 5 / 5 | 1675 | 1675.00 | 1675â€“1675 | 1675 | 2026-03-13, 2026-04-13, 2026-05-13 |
| event_1542 | dining / Family dinner | 13 / 6 | 5777.677692307692307692307692 | 5641.06 | 4425.44â€“6839.37 | 5777.68 | 2026-03-08, 2026-03-22, 2026-04-05, 2026-04-19, 2026-05-03, 2026-05-17 |
| event_1474 | education / Course tuition | 5 / 5 | 13660 | 13660.00 | 13660â€“13660 | 13660 | 2026-03-08, 2026-04-08, 2026-05-08 |
| event_1503 | groceries / Supermarket basket | 26 / 6 | 9096.698076923076923076923077 | 8677.525 | 6706.54â€“11433.33 | 9096.7 | 2026-03-06, 2026-03-13, 2026-03-20, 2026-03-27, 2026-04-03, 2026-04-10, 2026-04-17, 2026-04-24, 2026-05-01, 2026-05-08, 2026-05-15, 2026-05-22, 2026-05-29 |
| event_1476 | music_subscription / Music subscription | 5 / 5 | 2055 | 2055.00 | 2055â€“2055 | 2055 | 2026-03-11, 2026-04-11, 2026-05-11 |
| event_1472 | rent / Apartment rent transfer | 5 / 5 | 49600 | 49600.00 | 49600â€“49600 | 49600 | 2026-03-02, 2026-04-02, 2026-05-02 |
| event_1529 | transport / Rail pass | 26 / 6 | 5278.039615384615384615384615 | 5403.945 | 3902.91â€“6420.35 | 5278.04 | 2026-03-07, 2026-03-14, 2026-03-21, 2026-03-28, 2026-04-04, 2026-04-11, 2026-04-18, 2026-04-25, 2026-05-02, 2026-05-09, 2026-05-16, 2026-05-23, 2026-05-30 |
| event_1473 | utilities / Municipal utilities | 5 / 5 | 9538.746 | 9530.77 | 8487.15â€“10246.53 | 9538.75 | 2026-03-06, 2026-04-06, 2026-05-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-03-02 | -49600 | event_1472 | rent | recurring_expense | Apartment rent transfer |
| 2026-03-06 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-03-06 | -9538.75 | event_1473 | utilities | recurring_expense | Municipal utilities |
| 2026-03-07 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-03-08 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-03-08 | -13660 | event_1474 | education | recurring_expense | Course tuition |
| 2026-03-11 | -2055 | event_1476 | music_subscription | recurring_expense | Music subscription |
| 2026-03-11 | -30200 | event_1475 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-03-13 | -1675 | event_1477 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-03-13 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-03-14 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-03-15 | 206000 | event_1546 | salary | recurring_income | Next confirmed salary |
| 2026-03-20 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-03-21 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-03-22 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-03-27 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-03-28 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-04-02 | -49600 | event_1472 | rent | recurring_expense | Apartment rent transfer |
| 2026-04-03 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-04-04 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-04-05 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-04-06 | -9538.75 | event_1473 | utilities | recurring_expense | Municipal utilities |
| 2026-04-08 | -13660 | event_1474 | education | recurring_expense | Course tuition |
| 2026-04-10 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-04-11 | -2055 | event_1476 | music_subscription | recurring_expense | Music subscription |
| 2026-04-11 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-04-11 | -30200 | event_1475 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-04-13 | -1675 | event_1477 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-04-15 | 206000 | event_1546 | salary | recurring_income | Next confirmed salary |
| 2026-04-17 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-04-18 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-04-19 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-04-24 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-04-25 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-05-01 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-05-02 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-05-02 | -49600 | event_1472 | rent | recurring_expense | Apartment rent transfer |
| 2026-05-03 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-05-06 | -9538.75 | event_1473 | utilities | recurring_expense | Municipal utilities |
| 2026-05-08 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-05-08 | -13660 | event_1474 | education | recurring_expense | Course tuition |
| 2026-05-09 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-05-11 | -2055 | event_1476 | music_subscription | recurring_expense | Music subscription |
| 2026-05-11 | -30200 | event_1475 | debt_repayment | recurring_expense | Credit card repayment |
| 2026-05-13 | -1675 | event_1477 | delivery_membership | recurring_expense | Food delivery membership |
| 2026-05-15 | 206000 | event_1546 | salary | recurring_income | Next confirmed salary |
| 2026-05-15 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-05-16 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-05-17 | -5777.68 | event_1542 | dining | recurring_expense | Family dinner |
| 2026-05-22 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-05-23 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |
| 2026-05-29 | -9096.7 | event_1503 | groceries | recurring_expense | Supermarket basket |
| 2026-05-30 | -5278.04 | event_1529 | transport | recurring_expense | Rail pass |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-03-01 | 0 | 550379.58 | 384279.58 | 306530 | 455184.91 | 95194.67 | (empty) |
| 1 | 2026-03-02 | -49600 | 500779.58 | 334679.58 | 256930 | 405584.91 | 0 | event_1472 |
| 2 | 2026-03-03 | 0 | 500779.58 | 334679.58 | 256930 | 405584.91 | 0 | (empty) |
| 3 | 2026-03-04 | 0 | 500779.58 | 334679.58 | 256930 | 405584.91 | 0 | (empty) |
| 4 | 2026-03-05 | 0 | 500779.58 | 334679.58 | 256930 | 405584.91 | 0 | (empty) |
| 5 | 2026-03-06 | -18635.45 | 482144.13 | 316044.13 | 238294.55 | 386949.46 | 0 | event_1503, event_1473 |
| 6 | 2026-03-07 | -5278.04 | 476866.09 | 310766.09 | 233016.51 | 381671.42 | 0 | event_1529 |
| 7 | 2026-03-08 | -19437.68 | 457428.41 | 291328.41 | 213578.83 | 362233.74 | 0 | event_1542, event_1474 |
| 8 | 2026-03-09 | 0 | 457428.41 | 291328.41 | 213578.83 | 362233.74 | 0 | (empty) |
| 9 | 2026-03-10 | 0 | 457428.41 | 291328.41 | 213578.83 | 362233.74 | 0 | (empty) |
| 10 | 2026-03-11 | -32255 | 425173.41 | 259073.41 | 181323.83 | 329978.74 | 0 | event_1476, event_1475 |
| 11 | 2026-03-12 | 0 | 425173.41 | 259073.41 | 181323.83 | 329978.74 | 0 | (empty) |
| 12 | 2026-03-13 | -10771.7 | 414401.71 | 248301.71 | 170552.13 | 319207.04 | 0 | event_1477, event_1503 |
| 13 | 2026-03-14 | -5278.04 | 409123.67 | 243023.67 | 165274.09 | 313929 | 0 | event_1529 |
| 14 | 2026-03-15 | 206000 | 615123.67 | 449023.67 | 371274.09 | 519929 | 0 | event_1546 |
| 15 | 2026-03-16 | 0 | 615123.67 | 449023.67 | 371274.09 | 519929 | 0 | (empty) |
| 16 | 2026-03-17 | 0 | 615123.67 | 449023.67 | 371274.09 | 519929 | 0 | (empty) |
| 17 | 2026-03-18 | 0 | 615123.67 | 449023.67 | 371274.09 | 519929 | 0 | (empty) |
| 18 | 2026-03-19 | 0 | 615123.67 | 449023.67 | 371274.09 | 519929 | 0 | (empty) |
| 19 | 2026-03-20 | -9096.7 | 606026.97 | 439926.97 | 362177.39 | 510832.3 | 0 | event_1503 |
| 20 | 2026-03-21 | -5278.04 | 600748.93 | 434648.93 | 356899.35 | 505554.26 | 0 | event_1529 |
| 21 | 2026-03-22 | -5777.68 | 594971.25 | 428871.25 | 351121.67 | 499776.58 | 0 | event_1542 |
| 22 | 2026-03-23 | 0 | 594971.25 | 428871.25 | 351121.67 | 499776.58 | 0 | (empty) |
| 23 | 2026-03-24 | 0 | 594971.25 | 428871.25 | 351121.67 | 499776.58 | 0 | (empty) |
| 24 | 2026-03-25 | 0 | 594971.25 | 428871.25 | 351121.67 | 499776.58 | 0 | (empty) |
| 25 | 2026-03-26 | 0 | 594971.25 | 428871.25 | 351121.67 | 499776.58 | 0 | (empty) |
| 26 | 2026-03-27 | -9096.7 | 585874.55 | 419774.55 | 342024.97 | 490679.88 | 0 | event_1503 |
| 27 | 2026-03-28 | -5278.04 | 580596.51 | 414496.51 | 336746.93 | 485401.84 | 0 | event_1529 |
| 28 | 2026-03-29 | 0 | 580596.51 | 414496.51 | 336746.93 | 485401.84 | 0 | (empty) |
| 29 | 2026-03-30 | 0 | 580596.51 | 414496.51 | 336746.93 | 485401.84 | 0 | (empty) |
| 30 | 2026-03-31 | 0 | 580596.51 | 414496.51 | 336746.93 | 390207.17 | 95194.67 | (empty) |
| 31 | 2026-04-01 | 0 | 580596.51 | 414496.51 | 336746.93 | 390207.17 | 0 | (empty) |
| 32 | 2026-04-02 | -49600 | 530996.51 | 364896.51 | 287146.93 | 340607.17 | 0 | event_1472 |
| 33 | 2026-04-03 | -9096.7 | 521899.81 | 355799.81 | 278050.23 | 331510.47 | 0 | event_1503 |
| 34 | 2026-04-04 | -5278.04 | 516621.77 | 350521.77 | 272772.19 | 326232.43 | 0 | event_1529 |
| 35 | 2026-04-05 | -5777.68 | 510844.09 | 344744.09 | 266994.51 | 320454.75 | 0 | event_1542 |
| 36 | 2026-04-06 | -9538.75 | 501305.34 | 335205.34 | 257455.76 | 310916 | 0 | event_1473 |
| 37 | 2026-04-07 | 0 | 501305.34 | 335205.34 | 257455.76 | 310916 | 0 | (empty) |
| 38 | 2026-04-08 | -13660 | 487645.34 | 321545.34 | 243795.76 | 297256 | 0 | event_1474 |
| 39 | 2026-04-09 | 0 | 487645.34 | 321545.34 | 243795.76 | 297256 | 0 | (empty) |
| 40 | 2026-04-10 | -9096.7 | 478548.64 | 312448.64 | 234699.06 | 288159.3 | 0 | event_1503 |
| 41 | 2026-04-11 | -37533.04 | 441015.6 | 274915.6 | 197166.02 | 250626.26 | 0 | event_1476, event_1529, event_1475 |
| 42 | 2026-04-12 | 0 | 441015.6 | 274915.6 | 197166.02 | 250626.26 | 0 | (empty) |
| 43 | 2026-04-13 | -1675 | 439340.6 | 273240.6 | 195491.02 | 248951.26 | 0 | event_1477 |
| 44 | 2026-04-14 | 0 | 439340.6 | 273240.6 | 195491.02 | 248951.26 | 0 | (empty) |
| 45 | 2026-04-15 | 206000 | 645340.6 | 479240.6 | 401491.02 | 454951.26 | 0 | event_1546 |
| 46 | 2026-04-16 | 0 | 645340.6 | 479240.6 | 401491.02 | 454951.26 | 0 | (empty) |
| 47 | 2026-04-17 | -9096.7 | 636243.9 | 470143.9 | 392394.32 | 445854.56 | 0 | event_1503 |
| 48 | 2026-04-18 | -5278.04 | 630965.86 | 464865.86 | 387116.28 | 440576.52 | 0 | event_1529 |
| 49 | 2026-04-19 | -5777.68 | 625188.18 | 459088.18 | 381338.6 | 434798.84 | 0 | event_1542 |
| 50 | 2026-04-20 | 0 | 625188.18 | 459088.18 | 381338.6 | 434798.84 | 0 | (empty) |
| 51 | 2026-04-21 | 0 | 625188.18 | 459088.18 | 381338.6 | 434798.84 | 0 | (empty) |
| 52 | 2026-04-22 | 0 | 625188.18 | 459088.18 | 381338.6 | 434798.84 | 0 | (empty) |
| 53 | 2026-04-23 | 0 | 625188.18 | 459088.18 | 381338.6 | 434798.84 | 0 | (empty) |
| 54 | 2026-04-24 | -9096.7 | 616091.48 | 449991.48 | 372241.9 | 425702.14 | 0 | event_1503 |
| 55 | 2026-04-25 | -5278.04 | 610813.44 | 444713.44 | 366963.86 | 420424.1 | 0 | event_1529 |
| 56 | 2026-04-26 | 0 | 610813.44 | 444713.44 | 366963.86 | 420424.1 | 0 | (empty) |
| 57 | 2026-04-27 | 0 | 610813.44 | 444713.44 | 366963.86 | 420424.1 | 0 | (empty) |
| 58 | 2026-04-28 | 0 | 610813.44 | 444713.44 | 366963.86 | 420424.1 | 0 | (empty) |
| 59 | 2026-04-29 | 0 | 610813.44 | 444713.44 | 366963.86 | 420424.1 | 0 | (empty) |
| 60 | 2026-04-30 | 0 | 610813.44 | 444713.44 | 366963.86 | 325229.43 | 95194.67 | (empty) |
| 61 | 2026-05-01 | -9096.7 | 601716.74 | 435616.74 | 357867.16 | 316132.73 | 0 | event_1503 |
| 62 | 2026-05-02 | -54878.04 | 546838.7 | 380738.7 | 302989.12 | 261254.69 | 0 | event_1529, event_1472 |
| 63 | 2026-05-03 | -5777.68 | 541061.02 | 374961.02 | 297211.44 | 255477.01 | 0 | event_1542 |
| 64 | 2026-05-04 | 0 | 541061.02 | 374961.02 | 297211.44 | 255477.01 | 0 | (empty) |
| 65 | 2026-05-05 | 0 | 541061.02 | 374961.02 | 297211.44 | 255477.01 | 0 | (empty) |
| 66 | 2026-05-06 | -9538.75 | 531522.27 | 365422.27 | 287672.69 | 245938.26 | 0 | event_1473 |
| 67 | 2026-05-07 | 0 | 531522.27 | 365422.27 | 287672.69 | 245938.26 | 0 | (empty) |
| 68 | 2026-05-08 | -22756.7 | 508765.57 | 342665.57 | 264915.99 | 223181.56 | 0 | event_1503, event_1474 |
| 69 | 2026-05-09 | -5278.04 | 503487.53 | 337387.53 | 259637.95 | 217903.52 | 0 | event_1529 |
| 70 | 2026-05-10 | 0 | 503487.53 | 337387.53 | 259637.95 | 217903.52 | 0 | (empty) |
| 71 | 2026-05-11 | -32255 | 471232.53 | 305132.53 | 227382.95 | 185648.52 | 0 | event_1476, event_1475 |
| 72 | 2026-05-12 | 0 | 471232.53 | 305132.53 | 227382.95 | 185648.52 | 0 | (empty) |
| 73 | 2026-05-13 | -1675 | 469557.53 | 303457.53 | 225707.95 | 183973.52 | 0 | event_1477 |
| 74 | 2026-05-14 | 0 | 469557.53 | 303457.53 | 225707.95 | 183973.52 | 0 | (empty) |
| 75 | 2026-05-15 | 196903.3 | 666460.83 | 500360.83 | 422611.25 | 380876.82 | 0 | event_1546, event_1503 |
| 76 | 2026-05-16 | -5278.04 | 661182.79 | 495082.79 | 417333.21 | 375598.78 | 0 | event_1529 |
| 77 | 2026-05-17 | -5777.68 | 655405.11 | 489305.11 | 411555.53 | 369821.1 | 0 | event_1542 |
| 78 | 2026-05-18 | 0 | 655405.11 | 489305.11 | 411555.53 | 369821.1 | 0 | (empty) |
| 79 | 2026-05-19 | 0 | 655405.11 | 489305.11 | 411555.53 | 369821.1 | 0 | (empty) |
| 80 | 2026-05-20 | 0 | 655405.11 | 489305.11 | 411555.53 | 369821.1 | 0 | (empty) |
| 81 | 2026-05-21 | 0 | 655405.11 | 489305.11 | 411555.53 | 369821.1 | 0 | (empty) |
| 82 | 2026-05-22 | -9096.7 | 646308.41 | 480208.41 | 402458.83 | 360724.4 | 0 | event_1503 |
| 83 | 2026-05-23 | -5278.04 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | event_1529 |
| 84 | 2026-05-24 | 0 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | (empty) |
| 85 | 2026-05-25 | 0 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | (empty) |
| 86 | 2026-05-26 | 0 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | (empty) |
| 87 | 2026-05-27 | 0 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | (empty) |
| 88 | 2026-05-28 | 0 | 641030.37 | 474930.37 | 397180.79 | 355446.36 | 0 | (empty) |
| 89 | 2026-05-29 | -9096.7 | 631933.67 | 465833.67 | 388084.09 | 346349.66 | 0 | event_1503 |
| 90 | 2026-05-30 | -5278.04 | 626655.63 | 460555.63 | 382806.05 | 341071.62 | 0 | event_1529 |

## request_18 â€” user_18 (EUR)

Request: 3246.1 on 2026-07-07; deadline 2026-09-15. Opening 2486; minimum 1400.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 462 | 546.05 | NO |
| affordability_status | affordable_later | affordable_later | yes |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2026-09-15:3246.10 | 2026-09-15:3246.10 | yes |
| earliest_date_for_full_payment | 2026-09-15 | 2026-09-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 7 (2026-07-14), balance 1946.05, headroom 546.05.

Protected: housing|healthcare|utilities. Reduce: dining|streaming. Stop: streaming.

Salary mode: historical. Evidence: none. Unparsed messages: message_13.

- message_13 (bank, 2026-07-01T09:30:00Z): There’s an update from Summit Bank on your recent account activity. The matching debit and credit came from a transfer between your two accounts. Both accounts are registered under the same account holder. Both entries will remain visible in your transaction history. Txn ref BAN-0013.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1621 | dining / Takeaway order | 13 / 7 | 85.63461538461538461538461538 | 82.67 | 62.87â€“108.96 | 85.63 | 2026-07-15, 2026-07-29, 2026-08-12, 2026-08-26, 2026-09-09, 2026-09-23 |
| event_1595 | groceries / Supermarket basket | 18 / 7 | 93.42111111111111111111111111 | 95.325 | 64.84â€“115 | 93.42 | 2026-07-11, 2026-07-21, 2026-07-31, 2026-08-10, 2026-08-20, 2026-08-30, 2026-09-09, 2026-09-19, 2026-09-29 |
| event_1575 | healthcare / Clinic payment | 5 / 5 | 155.412 | 152.41 | 147.96â€“164.1 | 155.41 | 2026-07-11, 2026-08-11, 2026-09-11 |
| event_1577 | housing / Building maintenance payment | 6 / 6 | 167 | 167.00 | 167â€“167 | 167 | 2026-08-04, 2026-09-04, 2026-10-04 |
| event_1574 | insurance / Household insurance | 5 / 5 | 68 | 68.00 | 68â€“68 | 68 | 2026-07-08, 2026-08-08, 2026-09-08 |
| event_1576 | streaming / Family streaming plan | 5 / 5 | 68 | 68.00 | 68â€“68 | 68 | 2026-07-10, 2026-08-10, 2026-09-10 |
| event_1608 | transport / Metro and bus fares | 13 / 6 | 43.85230769230769230769230769 | 43.81 | 34.87â€“54.53 | 43.85 | 2026-07-14, 2026-07-28, 2026-08-11, 2026-08-25, 2026-09-08, 2026-09-22 |
| event_1573 | utilities / Energy provider bill | 5 / 5 | 111.266 | 107.43 | 100.59â€“125.4 | 111.27 | 2026-07-07, 2026-08-07, 2026-09-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-07-07 | -111.27 | event_1573 | utilities | recurring_expense | Energy provider bill |
| 2026-07-08 | -68 | event_1574 | insurance | recurring_expense | Household insurance |
| 2026-07-10 | -68 | event_1576 | streaming | recurring_expense | Family streaming plan |
| 2026-07-11 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-07-11 | -155.41 | event_1575 | healthcare | recurring_expense | Clinic payment |
| 2026-07-14 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-07-15 | 2310 | event_1571 | salary | recurring_income | Payroll credit |
| 2026-07-15 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-07-21 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-07-28 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-07-29 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-07-31 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-08-04 | -167 | event_1577 | housing | recurring_expense | Building maintenance payment |
| 2026-08-07 | -111.27 | event_1573 | utilities | recurring_expense | Energy provider bill |
| 2026-08-08 | -68 | event_1574 | insurance | recurring_expense | Household insurance |
| 2026-08-10 | -68 | event_1576 | streaming | recurring_expense | Family streaming plan |
| 2026-08-10 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-08-11 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-08-11 | -155.41 | event_1575 | healthcare | recurring_expense | Clinic payment |
| 2026-08-12 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-08-15 | 2310 | event_1571 | salary | recurring_income | Payroll credit |
| 2026-08-20 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-08-25 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-08-26 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-08-30 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-09-04 | -167 | event_1577 | housing | recurring_expense | Building maintenance payment |
| 2026-09-07 | -111.27 | event_1573 | utilities | recurring_expense | Energy provider bill |
| 2026-09-08 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-09-08 | -68 | event_1574 | insurance | recurring_expense | Household insurance |
| 2026-09-09 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-09-09 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-09-10 | -68 | event_1576 | streaming | recurring_expense | Family streaming plan |
| 2026-09-11 | -155.41 | event_1575 | healthcare | recurring_expense | Clinic payment |
| 2026-09-15 | 2310 | event_1571 | salary | recurring_income | Payroll credit |
| 2026-09-19 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-09-22 | -43.85 | event_1608 | transport | recurring_expense | Metro and bus fares |
| 2026-09-23 | -85.63 | event_1621 | dining | recurring_expense | Takeaway order |
| 2026-09-29 | -93.42 | event_1595 | groceries | recurring_expense | Supermarket basket |
| 2026-10-04 | -167 | event_1577 | housing | recurring_expense | Building maintenance payment |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-07-07 | -111.27 | 2374.73 | 974.73 | 1912.73 | 2374.73 | 0 | event_1573 |
| 1 | 2026-07-08 | -68 | 2306.73 | 906.73 | 1844.73 | 2306.73 | 0 | event_1574 |
| 2 | 2026-07-09 | 0 | 2306.73 | 906.73 | 1844.73 | 2306.73 | 0 | (empty) |
| 3 | 2026-07-10 | -68 | 2238.73 | 838.73 | 1776.73 | 2238.73 | 0 | event_1576 |
| 4 | 2026-07-11 | -248.83 | 1989.9 | 589.9 | 1527.9 | 1989.9 | 0 | event_1595, event_1575 |
| 5 | 2026-07-12 | 0 | 1989.9 | 589.9 | 1527.9 | 1989.9 | 0 | (empty) |
| 6 | 2026-07-13 | 0 | 1989.9 | 589.9 | 1527.9 | 1989.9 | 0 | (empty) |
| 7 | 2026-07-14 | -43.85 | 1946.05 | 546.05 | 1484.05 | 1946.05 | 0 | event_1608 |
| 8 | 2026-07-15 | 2224.37 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | event_1571, event_1621 |
| 9 | 2026-07-16 | 0 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | (empty) |
| 10 | 2026-07-17 | 0 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | (empty) |
| 11 | 2026-07-18 | 0 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | (empty) |
| 12 | 2026-07-19 | 0 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | (empty) |
| 13 | 2026-07-20 | 0 | 4170.42 | 2770.42 | 3708.42 | 4170.42 | 0 | (empty) |
| 14 | 2026-07-21 | -93.42 | 4077 | 2677 | 3615 | 4077 | 0 | event_1595 |
| 15 | 2026-07-22 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 16 | 2026-07-23 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 17 | 2026-07-24 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 18 | 2026-07-25 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 19 | 2026-07-26 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 20 | 2026-07-27 | 0 | 4077 | 2677 | 3615 | 4077 | 0 | (empty) |
| 21 | 2026-07-28 | -43.85 | 4033.15 | 2633.15 | 3571.15 | 4033.15 | 0 | event_1608 |
| 22 | 2026-07-29 | -85.63 | 3947.52 | 2547.52 | 3485.52 | 3947.52 | 0 | event_1621 |
| 23 | 2026-07-30 | 0 | 3947.52 | 2547.52 | 3485.52 | 3947.52 | 0 | (empty) |
| 24 | 2026-07-31 | -93.42 | 3854.1 | 2454.1 | 3392.1 | 3854.1 | 0 | event_1595 |
| 25 | 2026-08-01 | 0 | 3854.1 | 2454.1 | 3392.1 | 3854.1 | 0 | (empty) |
| 26 | 2026-08-02 | 0 | 3854.1 | 2454.1 | 3392.1 | 3854.1 | 0 | (empty) |
| 27 | 2026-08-03 | 0 | 3854.1 | 2454.1 | 3392.1 | 3854.1 | 0 | (empty) |
| 28 | 2026-08-04 | -167 | 3687.1 | 2287.1 | 3225.1 | 3687.1 | 0 | event_1577 |
| 29 | 2026-08-05 | 0 | 3687.1 | 2287.1 | 3225.1 | 3687.1 | 0 | (empty) |
| 30 | 2026-08-06 | 0 | 3687.1 | 2287.1 | 3225.1 | 3687.1 | 0 | (empty) |
| 31 | 2026-08-07 | -111.27 | 3575.83 | 2175.83 | 3113.83 | 3575.83 | 0 | event_1573 |
| 32 | 2026-08-08 | -68 | 3507.83 | 2107.83 | 3045.83 | 3507.83 | 0 | event_1574 |
| 33 | 2026-08-09 | 0 | 3507.83 | 2107.83 | 3045.83 | 3507.83 | 0 | (empty) |
| 34 | 2026-08-10 | -161.42 | 3346.41 | 1946.41 | 2884.41 | 3346.41 | 0 | event_1576, event_1595 |
| 35 | 2026-08-11 | -199.26 | 3147.15 | 1747.15 | 2685.15 | 3147.15 | 0 | event_1608, event_1575 |
| 36 | 2026-08-12 | -85.63 | 3061.52 | 1661.52 | 2599.52 | 3061.52 | 0 | event_1621 |
| 37 | 2026-08-13 | 0 | 3061.52 | 1661.52 | 2599.52 | 3061.52 | 0 | (empty) |
| 38 | 2026-08-14 | 0 | 3061.52 | 1661.52 | 2599.52 | 3061.52 | 0 | (empty) |
| 39 | 2026-08-15 | 2310 | 5371.52 | 3971.52 | 4909.52 | 5371.52 | 0 | event_1571 |
| 40 | 2026-08-16 | 0 | 5371.52 | 3971.52 | 4909.52 | 5371.52 | 0 | (empty) |
| 41 | 2026-08-17 | 0 | 5371.52 | 3971.52 | 4909.52 | 5371.52 | 0 | (empty) |
| 42 | 2026-08-18 | 0 | 5371.52 | 3971.52 | 4909.52 | 5371.52 | 0 | (empty) |
| 43 | 2026-08-19 | 0 | 5371.52 | 3971.52 | 4909.52 | 5371.52 | 0 | (empty) |
| 44 | 2026-08-20 | -93.42 | 5278.1 | 3878.1 | 4816.1 | 5278.1 | 0 | event_1595 |
| 45 | 2026-08-21 | 0 | 5278.1 | 3878.1 | 4816.1 | 5278.1 | 0 | (empty) |
| 46 | 2026-08-22 | 0 | 5278.1 | 3878.1 | 4816.1 | 5278.1 | 0 | (empty) |
| 47 | 2026-08-23 | 0 | 5278.1 | 3878.1 | 4816.1 | 5278.1 | 0 | (empty) |
| 48 | 2026-08-24 | 0 | 5278.1 | 3878.1 | 4816.1 | 5278.1 | 0 | (empty) |
| 49 | 2026-08-25 | -43.85 | 5234.25 | 3834.25 | 4772.25 | 5234.25 | 0 | event_1608 |
| 50 | 2026-08-26 | -85.63 | 5148.62 | 3748.62 | 4686.62 | 5148.62 | 0 | event_1621 |
| 51 | 2026-08-27 | 0 | 5148.62 | 3748.62 | 4686.62 | 5148.62 | 0 | (empty) |
| 52 | 2026-08-28 | 0 | 5148.62 | 3748.62 | 4686.62 | 5148.62 | 0 | (empty) |
| 53 | 2026-08-29 | 0 | 5148.62 | 3748.62 | 4686.62 | 5148.62 | 0 | (empty) |
| 54 | 2026-08-30 | -93.42 | 5055.2 | 3655.2 | 4593.2 | 5055.2 | 0 | event_1595 |
| 55 | 2026-08-31 | 0 | 5055.2 | 3655.2 | 4593.2 | 5055.2 | 0 | (empty) |
| 56 | 2026-09-01 | 0 | 5055.2 | 3655.2 | 4593.2 | 5055.2 | 0 | (empty) |
| 57 | 2026-09-02 | 0 | 5055.2 | 3655.2 | 4593.2 | 5055.2 | 0 | (empty) |
| 58 | 2026-09-03 | 0 | 5055.2 | 3655.2 | 4593.2 | 5055.2 | 0 | (empty) |
| 59 | 2026-09-04 | -167 | 4888.2 | 3488.2 | 4426.2 | 4888.2 | 0 | event_1577 |
| 60 | 2026-09-05 | 0 | 4888.2 | 3488.2 | 4426.2 | 4888.2 | 0 | (empty) |
| 61 | 2026-09-06 | 0 | 4888.2 | 3488.2 | 4426.2 | 4888.2 | 0 | (empty) |
| 62 | 2026-09-07 | -111.27 | 4776.93 | 3376.93 | 4314.93 | 4776.93 | 0 | event_1573 |
| 63 | 2026-09-08 | -111.85 | 4665.08 | 3265.08 | 4203.08 | 4665.08 | 0 | event_1608, event_1574 |
| 64 | 2026-09-09 | -179.05 | 4486.03 | 3086.03 | 4024.03 | 4486.03 | 0 | event_1621, event_1595 |
| 65 | 2026-09-10 | -68 | 4418.03 | 3018.03 | 3956.03 | 4418.03 | 0 | event_1576 |
| 66 | 2026-09-11 | -155.41 | 4262.62 | 2862.62 | 3800.62 | 4262.62 | 0 | event_1575 |
| 67 | 2026-09-12 | 0 | 4262.62 | 2862.62 | 3800.62 | 4262.62 | 0 | (empty) |
| 68 | 2026-09-13 | 0 | 4262.62 | 2862.62 | 3800.62 | 4262.62 | 0 | (empty) |
| 69 | 2026-09-14 | 0 | 4262.62 | 2862.62 | 3800.62 | 4262.62 | 0 | (empty) |
| 70 | 2026-09-15 | 2310 | 6572.62 | 5172.62 | 6110.62 | 3326.52 | 3246.1 | event_1571 |
| 71 | 2026-09-16 | 0 | 6572.62 | 5172.62 | 6110.62 | 3326.52 | 0 | (empty) |
| 72 | 2026-09-17 | 0 | 6572.62 | 5172.62 | 6110.62 | 3326.52 | 0 | (empty) |
| 73 | 2026-09-18 | 0 | 6572.62 | 5172.62 | 6110.62 | 3326.52 | 0 | (empty) |
| 74 | 2026-09-19 | -93.42 | 6479.2 | 5079.2 | 6017.2 | 3233.1 | 0 | event_1595 |
| 75 | 2026-09-20 | 0 | 6479.2 | 5079.2 | 6017.2 | 3233.1 | 0 | (empty) |
| 76 | 2026-09-21 | 0 | 6479.2 | 5079.2 | 6017.2 | 3233.1 | 0 | (empty) |
| 77 | 2026-09-22 | -43.85 | 6435.35 | 5035.35 | 5973.35 | 3189.25 | 0 | event_1608 |
| 78 | 2026-09-23 | -85.63 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | event_1621 |
| 79 | 2026-09-24 | 0 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | (empty) |
| 80 | 2026-09-25 | 0 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | (empty) |
| 81 | 2026-09-26 | 0 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | (empty) |
| 82 | 2026-09-27 | 0 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | (empty) |
| 83 | 2026-09-28 | 0 | 6349.72 | 4949.72 | 5887.72 | 3103.62 | 0 | (empty) |
| 84 | 2026-09-29 | -93.42 | 6256.3 | 4856.3 | 5794.3 | 3010.2 | 0 | event_1595 |
| 85 | 2026-09-30 | 0 | 6256.3 | 4856.3 | 5794.3 | 3010.2 | 0 | (empty) |
| 86 | 2026-10-01 | 0 | 6256.3 | 4856.3 | 5794.3 | 3010.2 | 0 | (empty) |
| 87 | 2026-10-02 | 0 | 6256.3 | 4856.3 | 5794.3 | 3010.2 | 0 | (empty) |
| 88 | 2026-10-03 | 0 | 6256.3 | 4856.3 | 5794.3 | 3010.2 | 0 | (empty) |
| 89 | 2026-10-04 | -167 | 6089.3 | 4689.3 | 5627.3 | 2843.2 | 0 | event_1577 |
| 90 | 2026-10-05 | 0 | 6089.3 | 4689.3 | 5627.3 | 2843.2 | 0 | (empty) |

## request_19 â€” user_19 (INR)

Request: 39660 on 2024-09-04; deadline 2024-10-04. Opening 199545; minimum 92800.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 28820 | 25176.15 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | partial_payment | partial_payment | yes |
| payment_plan | 2024-09-04:28820\|2024-09-15:10840 | 2024-09-04:25176.15\|2024-09-15:14483.85 | NO |
| earliest_date_for_full_payment | 2024-09-15 | 2024-09-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 10 (2024-09-14), balance 117976.15, headroom 25176.15.

Protected: rent|healthcare|family_support|groceries. Reduce: shopping. Stop: cloud_storage.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1660 | cloud_storage / Online backup subscription | 5 / 5 | 395 | 395.00 | 395â€“395 | 395 | 2024-09-14, 2024-10-14, 2024-11-14 |
| event_1657 | debt_repayment / Loan repayment | 5 / 5 | 11850 | 11850.00 | 11850â€“11850 | 11850 | 2024-09-13, 2024-10-13, 2024-11-13 |
| event_1659 | family_support / Childcare contribution | 5 / 5 | 12650 | 12650.00 | 12650â€“12650 | 12650 | 2024-09-15, 2024-10-15, 2024-11-15 |
| event_1686 | groceries / Local market purchase | 25 / 6 | 4772.822 | 4744.13 | 3460.53â€“6070.85 | 4772.82 | 2024-09-04, 2024-09-11, 2024-09-18, 2024-09-25, 2024-10-02, 2024-10-09, 2024-10-16, 2024-10-23, 2024-10-30, 2024-11-06, 2024-11-13, 2024-11-20, 2024-11-27 |
| event_1658 | healthcare / Clinic payment | 5 / 5 | 8808.574 | 8645.36 | 8335.2â€“9619.88 | 8808.57 | 2024-09-12, 2024-10-12, 2024-11-12 |
| event_1655 | rent / Residential rent payment | 5 / 5 | 36100 | 36100.00 | 36100â€“36100 | 36100 | 2024-09-04, 2024-10-04, 2024-11-04 |
| event_1661 | shopping / Clothing and household items | 5 / 5 | 5833.868 | 5772.78 | 5431.12â€“6302.66 | 5833.87 | 2024-09-14, 2024-10-14, 2024-11-14 |
| event_1699 | transport / Fuel refill | 13 / 6 | 3080.13 | 3054.24 | 2462.29â€“3849.5 | 3080.13 | 2024-09-12, 2024-09-26, 2024-10-10, 2024-10-24, 2024-11-07, 2024-11-21 |
| event_1656 | utilities / Municipal utilities | 5 / 5 | 5955.636 | 6029.90 | 5525.82â€“6141.28 | 5955.64 | 2024-09-08, 2024-10-08, 2024-11-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-09-04 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-09-04 | -36100 | event_1655 | rent | recurring_expense | Residential rent payment |
| 2024-09-08 | -5955.64 | event_1656 | utilities | recurring_expense | Municipal utilities |
| 2024-09-11 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-09-12 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-09-12 | -8808.57 | event_1658 | healthcare | recurring_expense | Clinic payment |
| 2024-09-13 | -11850 | event_1657 | debt_repayment | recurring_expense | Loan repayment |
| 2024-09-14 | -395 | event_1660 | cloud_storage | recurring_expense | Online backup subscription |
| 2024-09-14 | -5833.87 | event_1661 | shopping | recurring_expense | Clothing and household items |
| 2024-09-15 | 131000 | event_1654 | salary | recurring_income | Payroll credit |
| 2024-09-15 | -12650 | event_1659 | family_support | recurring_expense | Childcare contribution |
| 2024-09-18 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-09-25 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-09-26 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-10-02 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-10-04 | -36100 | event_1655 | rent | recurring_expense | Residential rent payment |
| 2024-10-08 | -5955.64 | event_1656 | utilities | recurring_expense | Municipal utilities |
| 2024-10-09 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-10-10 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-10-12 | -8808.57 | event_1658 | healthcare | recurring_expense | Clinic payment |
| 2024-10-13 | -11850 | event_1657 | debt_repayment | recurring_expense | Loan repayment |
| 2024-10-14 | -395 | event_1660 | cloud_storage | recurring_expense | Online backup subscription |
| 2024-10-14 | -5833.87 | event_1661 | shopping | recurring_expense | Clothing and household items |
| 2024-10-15 | 131000 | event_1654 | salary | recurring_income | Payroll credit |
| 2024-10-15 | -12650 | event_1659 | family_support | recurring_expense | Childcare contribution |
| 2024-10-16 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-10-23 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-10-24 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-10-30 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-11-04 | -36100 | event_1655 | rent | recurring_expense | Residential rent payment |
| 2024-11-06 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-11-07 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-11-08 | -5955.64 | event_1656 | utilities | recurring_expense | Municipal utilities |
| 2024-11-12 | -8808.57 | event_1658 | healthcare | recurring_expense | Clinic payment |
| 2024-11-13 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-11-13 | -11850 | event_1657 | debt_repayment | recurring_expense | Loan repayment |
| 2024-11-14 | -395 | event_1660 | cloud_storage | recurring_expense | Online backup subscription |
| 2024-11-14 | -5833.87 | event_1661 | shopping | recurring_expense | Clothing and household items |
| 2024-11-15 | 131000 | event_1654 | salary | recurring_income | Payroll credit |
| 2024-11-15 | -12650 | event_1659 | family_support | recurring_expense | Childcare contribution |
| 2024-11-20 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |
| 2024-11-21 | -3080.13 | event_1699 | transport | recurring_expense | Fuel refill |
| 2024-11-27 | -4772.82 | event_1686 | groceries | recurring_expense | Local market purchase |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-09-04 | -40872.82 | 158672.18 | 65872.18 | 129852.18 | 133496.03 | 25176.15 | event_1686, event_1655 |
| 1 | 2024-09-05 | 0 | 158672.18 | 65872.18 | 129852.18 | 133496.03 | 0 | (empty) |
| 2 | 2024-09-06 | 0 | 158672.18 | 65872.18 | 129852.18 | 133496.03 | 0 | (empty) |
| 3 | 2024-09-07 | 0 | 158672.18 | 65872.18 | 129852.18 | 133496.03 | 0 | (empty) |
| 4 | 2024-09-08 | -5955.64 | 152716.54 | 59916.54 | 123896.54 | 127540.39 | 0 | event_1656 |
| 5 | 2024-09-09 | 0 | 152716.54 | 59916.54 | 123896.54 | 127540.39 | 0 | (empty) |
| 6 | 2024-09-10 | 0 | 152716.54 | 59916.54 | 123896.54 | 127540.39 | 0 | (empty) |
| 7 | 2024-09-11 | -4772.82 | 147943.72 | 55143.72 | 119123.72 | 122767.57 | 0 | event_1686 |
| 8 | 2024-09-12 | -11888.7 | 136055.02 | 43255.02 | 107235.02 | 110878.87 | 0 | event_1699, event_1658 |
| 9 | 2024-09-13 | -11850 | 124205.02 | 31405.02 | 95385.02 | 99028.87 | 0 | event_1657 |
| 10 | 2024-09-14 | -6228.87 | 117976.15 | 25176.15 | 89156.15 | 92800 | 0 | event_1660, event_1661 |
| 11 | 2024-09-15 | 118350 | 236326.15 | 143526.15 | 207506.15 | 196666.15 | 14483.85 | event_1654, event_1659 |
| 12 | 2024-09-16 | 0 | 236326.15 | 143526.15 | 207506.15 | 196666.15 | 0 | (empty) |
| 13 | 2024-09-17 | 0 | 236326.15 | 143526.15 | 207506.15 | 196666.15 | 0 | (empty) |
| 14 | 2024-09-18 | -4772.82 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | event_1686 |
| 15 | 2024-09-19 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 16 | 2024-09-20 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 17 | 2024-09-21 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 18 | 2024-09-22 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 19 | 2024-09-23 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 20 | 2024-09-24 | 0 | 231553.33 | 138753.33 | 202733.33 | 191893.33 | 0 | (empty) |
| 21 | 2024-09-25 | -4772.82 | 226780.51 | 133980.51 | 197960.51 | 187120.51 | 0 | event_1686 |
| 22 | 2024-09-26 | -3080.13 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | event_1699 |
| 23 | 2024-09-27 | 0 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | (empty) |
| 24 | 2024-09-28 | 0 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | (empty) |
| 25 | 2024-09-29 | 0 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | (empty) |
| 26 | 2024-09-30 | 0 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | (empty) |
| 27 | 2024-10-01 | 0 | 223700.38 | 130900.38 | 194880.38 | 184040.38 | 0 | (empty) |
| 28 | 2024-10-02 | -4772.82 | 218927.56 | 126127.56 | 190107.56 | 179267.56 | 0 | event_1686 |
| 29 | 2024-10-03 | 0 | 218927.56 | 126127.56 | 190107.56 | 179267.56 | 0 | (empty) |
| 30 | 2024-10-04 | -36100 | 182827.56 | 90027.56 | 154007.56 | 143167.56 | 0 | event_1655 |
| 31 | 2024-10-05 | 0 | 182827.56 | 90027.56 | 154007.56 | 143167.56 | 0 | (empty) |
| 32 | 2024-10-06 | 0 | 182827.56 | 90027.56 | 154007.56 | 143167.56 | 0 | (empty) |
| 33 | 2024-10-07 | 0 | 182827.56 | 90027.56 | 154007.56 | 143167.56 | 0 | (empty) |
| 34 | 2024-10-08 | -5955.64 | 176871.92 | 84071.92 | 148051.92 | 137211.92 | 0 | event_1656 |
| 35 | 2024-10-09 | -4772.82 | 172099.1 | 79299.1 | 143279.1 | 132439.1 | 0 | event_1686 |
| 36 | 2024-10-10 | -3080.13 | 169018.97 | 76218.97 | 140198.97 | 129358.97 | 0 | event_1699 |
| 37 | 2024-10-11 | 0 | 169018.97 | 76218.97 | 140198.97 | 129358.97 | 0 | (empty) |
| 38 | 2024-10-12 | -8808.57 | 160210.4 | 67410.4 | 131390.4 | 120550.4 | 0 | event_1658 |
| 39 | 2024-10-13 | -11850 | 148360.4 | 55560.4 | 119540.4 | 108700.4 | 0 | event_1657 |
| 40 | 2024-10-14 | -6228.87 | 142131.53 | 49331.53 | 113311.53 | 102471.53 | 0 | event_1660, event_1661 |
| 41 | 2024-10-15 | 118350 | 260481.53 | 167681.53 | 231661.53 | 220821.53 | 0 | event_1654, event_1659 |
| 42 | 2024-10-16 | -4772.82 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | event_1686 |
| 43 | 2024-10-17 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 44 | 2024-10-18 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 45 | 2024-10-19 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 46 | 2024-10-20 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 47 | 2024-10-21 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 48 | 2024-10-22 | 0 | 255708.71 | 162908.71 | 226888.71 | 216048.71 | 0 | (empty) |
| 49 | 2024-10-23 | -4772.82 | 250935.89 | 158135.89 | 222115.89 | 211275.89 | 0 | event_1686 |
| 50 | 2024-10-24 | -3080.13 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | event_1699 |
| 51 | 2024-10-25 | 0 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | (empty) |
| 52 | 2024-10-26 | 0 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | (empty) |
| 53 | 2024-10-27 | 0 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | (empty) |
| 54 | 2024-10-28 | 0 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | (empty) |
| 55 | 2024-10-29 | 0 | 247855.76 | 155055.76 | 219035.76 | 208195.76 | 0 | (empty) |
| 56 | 2024-10-30 | -4772.82 | 243082.94 | 150282.94 | 214262.94 | 203422.94 | 0 | event_1686 |
| 57 | 2024-10-31 | 0 | 243082.94 | 150282.94 | 214262.94 | 203422.94 | 0 | (empty) |
| 58 | 2024-11-01 | 0 | 243082.94 | 150282.94 | 214262.94 | 203422.94 | 0 | (empty) |
| 59 | 2024-11-02 | 0 | 243082.94 | 150282.94 | 214262.94 | 203422.94 | 0 | (empty) |
| 60 | 2024-11-03 | 0 | 243082.94 | 150282.94 | 214262.94 | 203422.94 | 0 | (empty) |
| 61 | 2024-11-04 | -36100 | 206982.94 | 114182.94 | 178162.94 | 167322.94 | 0 | event_1655 |
| 62 | 2024-11-05 | 0 | 206982.94 | 114182.94 | 178162.94 | 167322.94 | 0 | (empty) |
| 63 | 2024-11-06 | -4772.82 | 202210.12 | 109410.12 | 173390.12 | 162550.12 | 0 | event_1686 |
| 64 | 2024-11-07 | -3080.13 | 199129.99 | 106329.99 | 170309.99 | 159469.99 | 0 | event_1699 |
| 65 | 2024-11-08 | -5955.64 | 193174.35 | 100374.35 | 164354.35 | 153514.35 | 0 | event_1656 |
| 66 | 2024-11-09 | 0 | 193174.35 | 100374.35 | 164354.35 | 153514.35 | 0 | (empty) |
| 67 | 2024-11-10 | 0 | 193174.35 | 100374.35 | 164354.35 | 153514.35 | 0 | (empty) |
| 68 | 2024-11-11 | 0 | 193174.35 | 100374.35 | 164354.35 | 153514.35 | 0 | (empty) |
| 69 | 2024-11-12 | -8808.57 | 184365.78 | 91565.78 | 155545.78 | 144705.78 | 0 | event_1658 |
| 70 | 2024-11-13 | -16622.82 | 167742.96 | 74942.96 | 138922.96 | 128082.96 | 0 | event_1686, event_1657 |
| 71 | 2024-11-14 | -6228.87 | 161514.09 | 68714.09 | 132694.09 | 121854.09 | 0 | event_1660, event_1661 |
| 72 | 2024-11-15 | 118350 | 279864.09 | 187064.09 | 251044.09 | 240204.09 | 0 | event_1654, event_1659 |
| 73 | 2024-11-16 | 0 | 279864.09 | 187064.09 | 251044.09 | 240204.09 | 0 | (empty) |
| 74 | 2024-11-17 | 0 | 279864.09 | 187064.09 | 251044.09 | 240204.09 | 0 | (empty) |
| 75 | 2024-11-18 | 0 | 279864.09 | 187064.09 | 251044.09 | 240204.09 | 0 | (empty) |
| 76 | 2024-11-19 | 0 | 279864.09 | 187064.09 | 251044.09 | 240204.09 | 0 | (empty) |
| 77 | 2024-11-20 | -4772.82 | 275091.27 | 182291.27 | 246271.27 | 235431.27 | 0 | event_1686 |
| 78 | 2024-11-21 | -3080.13 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | event_1699 |
| 79 | 2024-11-22 | 0 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | (empty) |
| 80 | 2024-11-23 | 0 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | (empty) |
| 81 | 2024-11-24 | 0 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | (empty) |
| 82 | 2024-11-25 | 0 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | (empty) |
| 83 | 2024-11-26 | 0 | 272011.14 | 179211.14 | 243191.14 | 232351.14 | 0 | (empty) |
| 84 | 2024-11-27 | -4772.82 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | event_1686 |
| 85 | 2024-11-28 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |
| 86 | 2024-11-29 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |
| 87 | 2024-11-30 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |
| 88 | 2024-12-01 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |
| 89 | 2024-12-02 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |
| 90 | 2024-12-03 | 0 | 267238.32 | 174438.32 | 238418.32 | 227578.32 | 0 | (empty) |

## request_20 â€” user_20 (INR)

Request: 303700 on 2026-02-07; deadline 2026-02-22. Opening 102609.05; minimum 64500.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 5400 | 8969.68 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 6 (2026-02-13), balance 73469.68, headroom 8969.68.

Protected: housing|utilities|education. Reduce: dining|entertainment. Stop: cloud_storage.

Salary mode: historical. Evidence: message_14. Unparsed messages: none.

- message_14 (merchant, 2026-02-06T09:30:00Z): CartLane has new information about your payment or refund. Your refund has been initiated but has not reached your account yet. We’ll send another update when the credit is completed. Order ref MER-0014.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1740 | cloud_storage / Shared storage plan | 5 / 5 | 365 | 365.00 | 365â€“365 | 365 | 2026-02-11, 2026-03-11, 2026-04-11 |
| event_1783 | dining / Bakery and snacks | 9 / 6 | 3423.791111111111111111111111 | 3352.75 | 2629.91â€“4308.23 | 3423.79 | 2026-02-20, 2026-03-13, 2026-04-03, 2026-04-24 |
| event_1737 | education / School fee payment | 5 / 5 | 8740 | 8740.00 | 8740â€“8740 | 8740 | 2026-02-07, 2026-03-07, 2026-04-07, 2026-05-07 |
| event_1739 | entertainment / Cinema and events | 5 / 5 | 2148.272 | 2115.92 | 1949.86â€“2298.76 | 2148.27 | 2026-02-13, 2026-03-13, 2026-04-13 |
| event_1761 | groceries / Household groceries | 18 / 6 | 3700.527222222222222222222222 | 3713.325 | 2812.26â€“4719.22 | 3700.53 | 2026-02-09, 2026-02-19, 2026-03-01, 2026-03-11, 2026-03-21, 2026-03-31, 2026-04-10, 2026-04-20, 2026-04-30 |
| event_1738 | healthcare / Family healthcare expense | 5 / 5 | 6336.846 | 6505.49 | 5907.73â€“6654.33 | 6336.85 | 2026-02-09, 2026-03-09, 2026-04-09 |
| event_1741 | housing / Home association fee | 6 / 6 | 7950 | 7950.00 | 7950â€“7950 | 7950 | 2026-03-02, 2026-04-02, 2026-05-02 |
| event_1743 | insurance / Household insurance | 6 / 6 | 3290 | 3290.00 | 3290â€“3290 | 3290 | 2026-03-06, 2026-04-06, 2026-05-06 |
| event_1774 | transport / Metro and bus fares | 13 / 6 | 2674.673846153846153846153846 | 2632.00 | 2046.25â€“3243.84 | 2674.67 | 2026-02-12, 2026-02-26, 2026-03-12, 2026-03-26, 2026-04-09, 2026-04-23, 2026-05-07 |
| event_1742 | utilities / Municipal utilities | 6 / 6 | 7665.158333333333333333333333 | 7777.08 | 6848.62â€“8058.75 | 7665.16 | 2026-03-05, 2026-04-05, 2026-05-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-02-07 | -8740 | event_1737 | education | recurring_expense | School fee payment |
| 2026-02-08 | -4470 | event_1787 | shopping | explicit_event | Pending online order charge |
| 2026-02-09 | -704.05 | event_1786 | utilities | explicit_event | Outstanding telecom bill |
| 2026-02-09 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-02-09 | -6336.85 | event_1738 | healthcare | recurring_expense | Family healthcare expense |
| 2026-02-11 | -365 | event_1740 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-02-12 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-02-13 | -2148.27 | event_1739 | entertainment | recurring_expense | Cinema and events |
| 2026-02-15 | 108000 | event_1733 | salary | recurring_income | Payroll credit |
| 2026-02-19 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-02-20 | -3423.79 | event_1783 | dining | recurring_expense | Bakery and snacks |
| 2026-02-26 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-03-01 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-03-02 | -7950 | event_1741 | housing | recurring_expense | Home association fee |
| 2026-03-05 | -7665.16 | event_1742 | utilities | recurring_expense | Municipal utilities |
| 2026-03-06 | -3290 | event_1743 | insurance | recurring_expense | Household insurance |
| 2026-03-07 | -8740 | event_1737 | education | recurring_expense | School fee payment |
| 2026-03-09 | -6336.85 | event_1738 | healthcare | recurring_expense | Family healthcare expense |
| 2026-03-11 | -365 | event_1740 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-03-11 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-03-12 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-03-13 | -2148.27 | event_1739 | entertainment | recurring_expense | Cinema and events |
| 2026-03-13 | -3423.79 | event_1783 | dining | recurring_expense | Bakery and snacks |
| 2026-03-15 | 108000 | event_1733 | salary | recurring_income | Payroll credit |
| 2026-03-21 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-03-26 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-03-31 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-04-02 | -7950 | event_1741 | housing | recurring_expense | Home association fee |
| 2026-04-03 | -3423.79 | event_1783 | dining | recurring_expense | Bakery and snacks |
| 2026-04-05 | -7665.16 | event_1742 | utilities | recurring_expense | Municipal utilities |
| 2026-04-06 | -3290 | event_1743 | insurance | recurring_expense | Household insurance |
| 2026-04-07 | -8740 | event_1737 | education | recurring_expense | School fee payment |
| 2026-04-09 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-04-09 | -6336.85 | event_1738 | healthcare | recurring_expense | Family healthcare expense |
| 2026-04-10 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-04-11 | -365 | event_1740 | cloud_storage | recurring_expense | Shared storage plan |
| 2026-04-13 | -2148.27 | event_1739 | entertainment | recurring_expense | Cinema and events |
| 2026-04-15 | 108000 | event_1733 | salary | recurring_income | Payroll credit |
| 2026-04-20 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-04-23 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-04-24 | -3423.79 | event_1783 | dining | recurring_expense | Bakery and snacks |
| 2026-04-30 | -3700.53 | event_1761 | groceries | recurring_expense | Household groceries |
| 2026-05-02 | -7950 | event_1741 | housing | recurring_expense | Home association fee |
| 2026-05-05 | -7665.16 | event_1742 | utilities | recurring_expense | Municipal utilities |
| 2026-05-06 | -3290 | event_1743 | insurance | recurring_expense | Household insurance |
| 2026-05-07 | -2674.67 | event_1774 | transport | recurring_expense | Metro and bus fares |
| 2026-05-07 | -8740 | event_1737 | education | recurring_expense | School fee payment |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-02-07 | -8740 | 93869.05 | 29369.05 | 88469.05 | 93869.05 | 0 | event_1737 |
| 1 | 2026-02-08 | -4470 | 89399.05 | 24899.05 | 83999.05 | 89399.05 | 0 | event_1787 |
| 2 | 2026-02-09 | -10741.43 | 78657.62 | 14157.62 | 73257.62 | 78657.62 | 0 | event_1786, event_1761, event_1738 |
| 3 | 2026-02-10 | 0 | 78657.62 | 14157.62 | 73257.62 | 78657.62 | 0 | (empty) |
| 4 | 2026-02-11 | -365 | 78292.62 | 13792.62 | 72892.62 | 78292.62 | 0 | event_1740 |
| 5 | 2026-02-12 | -2674.67 | 75617.95 | 11117.95 | 70217.95 | 75617.95 | 0 | event_1774 |
| 6 | 2026-02-13 | -2148.27 | 73469.68 | 8969.68 | 68069.68 | 73469.68 | 0 | event_1739 |
| 7 | 2026-02-14 | 0 | 73469.68 | 8969.68 | 68069.68 | 73469.68 | 0 | (empty) |
| 8 | 2026-02-15 | 108000 | 181469.68 | 116969.68 | 176069.68 | 181469.68 | 0 | event_1733 |
| 9 | 2026-02-16 | 0 | 181469.68 | 116969.68 | 176069.68 | 181469.68 | 0 | (empty) |
| 10 | 2026-02-17 | 0 | 181469.68 | 116969.68 | 176069.68 | 181469.68 | 0 | (empty) |
| 11 | 2026-02-18 | 0 | 181469.68 | 116969.68 | 176069.68 | 181469.68 | 0 | (empty) |
| 12 | 2026-02-19 | -3700.53 | 177769.15 | 113269.15 | 172369.15 | 177769.15 | 0 | event_1761 |
| 13 | 2026-02-20 | -3423.79 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | event_1783 |
| 14 | 2026-02-21 | 0 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | (empty) |
| 15 | 2026-02-22 | 0 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | (empty) |
| 16 | 2026-02-23 | 0 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | (empty) |
| 17 | 2026-02-24 | 0 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | (empty) |
| 18 | 2026-02-25 | 0 | 174345.36 | 109845.36 | 168945.36 | 174345.36 | 0 | (empty) |
| 19 | 2026-02-26 | -2674.67 | 171670.69 | 107170.69 | 166270.69 | 171670.69 | 0 | event_1774 |
| 20 | 2026-02-27 | 0 | 171670.69 | 107170.69 | 166270.69 | 171670.69 | 0 | (empty) |
| 21 | 2026-02-28 | 0 | 171670.69 | 107170.69 | 166270.69 | 171670.69 | 0 | (empty) |
| 22 | 2026-03-01 | -3700.53 | 167970.16 | 103470.16 | 162570.16 | 167970.16 | 0 | event_1761 |
| 23 | 2026-03-02 | -7950 | 160020.16 | 95520.16 | 154620.16 | 160020.16 | 0 | event_1741 |
| 24 | 2026-03-03 | 0 | 160020.16 | 95520.16 | 154620.16 | 160020.16 | 0 | (empty) |
| 25 | 2026-03-04 | 0 | 160020.16 | 95520.16 | 154620.16 | 160020.16 | 0 | (empty) |
| 26 | 2026-03-05 | -7665.16 | 152355 | 87855 | 146955 | 152355 | 0 | event_1742 |
| 27 | 2026-03-06 | -3290 | 149065 | 84565 | 143665 | 149065 | 0 | event_1743 |
| 28 | 2026-03-07 | -8740 | 140325 | 75825 | 134925 | 140325 | 0 | event_1737 |
| 29 | 2026-03-08 | 0 | 140325 | 75825 | 134925 | 140325 | 0 | (empty) |
| 30 | 2026-03-09 | -6336.85 | 133988.15 | 69488.15 | 128588.15 | 133988.15 | 0 | event_1738 |
| 31 | 2026-03-10 | 0 | 133988.15 | 69488.15 | 128588.15 | 133988.15 | 0 | (empty) |
| 32 | 2026-03-11 | -4065.53 | 129922.62 | 65422.62 | 124522.62 | 129922.62 | 0 | event_1740, event_1761 |
| 33 | 2026-03-12 | -2674.67 | 127247.95 | 62747.95 | 121847.95 | 127247.95 | 0 | event_1774 |
| 34 | 2026-03-13 | -5572.06 | 121675.89 | 57175.89 | 116275.89 | 121675.89 | 0 | event_1739, event_1783 |
| 35 | 2026-03-14 | 0 | 121675.89 | 57175.89 | 116275.89 | 121675.89 | 0 | (empty) |
| 36 | 2026-03-15 | 108000 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | event_1733 |
| 37 | 2026-03-16 | 0 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | (empty) |
| 38 | 2026-03-17 | 0 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | (empty) |
| 39 | 2026-03-18 | 0 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | (empty) |
| 40 | 2026-03-19 | 0 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | (empty) |
| 41 | 2026-03-20 | 0 | 229675.89 | 165175.89 | 224275.89 | 229675.89 | 0 | (empty) |
| 42 | 2026-03-21 | -3700.53 | 225975.36 | 161475.36 | 220575.36 | 225975.36 | 0 | event_1761 |
| 43 | 2026-03-22 | 0 | 225975.36 | 161475.36 | 220575.36 | 225975.36 | 0 | (empty) |
| 44 | 2026-03-23 | 0 | 225975.36 | 161475.36 | 220575.36 | 225975.36 | 0 | (empty) |
| 45 | 2026-03-24 | 0 | 225975.36 | 161475.36 | 220575.36 | 225975.36 | 0 | (empty) |
| 46 | 2026-03-25 | 0 | 225975.36 | 161475.36 | 220575.36 | 225975.36 | 0 | (empty) |
| 47 | 2026-03-26 | -2674.67 | 223300.69 | 158800.69 | 217900.69 | 223300.69 | 0 | event_1774 |
| 48 | 2026-03-27 | 0 | 223300.69 | 158800.69 | 217900.69 | 223300.69 | 0 | (empty) |
| 49 | 2026-03-28 | 0 | 223300.69 | 158800.69 | 217900.69 | 223300.69 | 0 | (empty) |
| 50 | 2026-03-29 | 0 | 223300.69 | 158800.69 | 217900.69 | 223300.69 | 0 | (empty) |
| 51 | 2026-03-30 | 0 | 223300.69 | 158800.69 | 217900.69 | 223300.69 | 0 | (empty) |
| 52 | 2026-03-31 | -3700.53 | 219600.16 | 155100.16 | 214200.16 | 219600.16 | 0 | event_1761 |
| 53 | 2026-04-01 | 0 | 219600.16 | 155100.16 | 214200.16 | 219600.16 | 0 | (empty) |
| 54 | 2026-04-02 | -7950 | 211650.16 | 147150.16 | 206250.16 | 211650.16 | 0 | event_1741 |
| 55 | 2026-04-03 | -3423.79 | 208226.37 | 143726.37 | 202826.37 | 208226.37 | 0 | event_1783 |
| 56 | 2026-04-04 | 0 | 208226.37 | 143726.37 | 202826.37 | 208226.37 | 0 | (empty) |
| 57 | 2026-04-05 | -7665.16 | 200561.21 | 136061.21 | 195161.21 | 200561.21 | 0 | event_1742 |
| 58 | 2026-04-06 | -3290 | 197271.21 | 132771.21 | 191871.21 | 197271.21 | 0 | event_1743 |
| 59 | 2026-04-07 | -8740 | 188531.21 | 124031.21 | 183131.21 | 188531.21 | 0 | event_1737 |
| 60 | 2026-04-08 | 0 | 188531.21 | 124031.21 | 183131.21 | 188531.21 | 0 | (empty) |
| 61 | 2026-04-09 | -9011.52 | 179519.69 | 115019.69 | 174119.69 | 179519.69 | 0 | event_1774, event_1738 |
| 62 | 2026-04-10 | -3700.53 | 175819.16 | 111319.16 | 170419.16 | 175819.16 | 0 | event_1761 |
| 63 | 2026-04-11 | -365 | 175454.16 | 110954.16 | 170054.16 | 175454.16 | 0 | event_1740 |
| 64 | 2026-04-12 | 0 | 175454.16 | 110954.16 | 170054.16 | 175454.16 | 0 | (empty) |
| 65 | 2026-04-13 | -2148.27 | 173305.89 | 108805.89 | 167905.89 | 173305.89 | 0 | event_1739 |
| 66 | 2026-04-14 | 0 | 173305.89 | 108805.89 | 167905.89 | 173305.89 | 0 | (empty) |
| 67 | 2026-04-15 | 108000 | 281305.89 | 216805.89 | 275905.89 | 281305.89 | 0 | event_1733 |
| 68 | 2026-04-16 | 0 | 281305.89 | 216805.89 | 275905.89 | 281305.89 | 0 | (empty) |
| 69 | 2026-04-17 | 0 | 281305.89 | 216805.89 | 275905.89 | 281305.89 | 0 | (empty) |
| 70 | 2026-04-18 | 0 | 281305.89 | 216805.89 | 275905.89 | 281305.89 | 0 | (empty) |
| 71 | 2026-04-19 | 0 | 281305.89 | 216805.89 | 275905.89 | 281305.89 | 0 | (empty) |
| 72 | 2026-04-20 | -3700.53 | 277605.36 | 213105.36 | 272205.36 | 277605.36 | 0 | event_1761 |
| 73 | 2026-04-21 | 0 | 277605.36 | 213105.36 | 272205.36 | 277605.36 | 0 | (empty) |
| 74 | 2026-04-22 | 0 | 277605.36 | 213105.36 | 272205.36 | 277605.36 | 0 | (empty) |
| 75 | 2026-04-23 | -2674.67 | 274930.69 | 210430.69 | 269530.69 | 274930.69 | 0 | event_1774 |
| 76 | 2026-04-24 | -3423.79 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | event_1783 |
| 77 | 2026-04-25 | 0 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | (empty) |
| 78 | 2026-04-26 | 0 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | (empty) |
| 79 | 2026-04-27 | 0 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | (empty) |
| 80 | 2026-04-28 | 0 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | (empty) |
| 81 | 2026-04-29 | 0 | 271506.9 | 207006.9 | 266106.9 | 271506.9 | 0 | (empty) |
| 82 | 2026-04-30 | -3700.53 | 267806.37 | 203306.37 | 262406.37 | 267806.37 | 0 | event_1761 |
| 83 | 2026-05-01 | 0 | 267806.37 | 203306.37 | 262406.37 | 267806.37 | 0 | (empty) |
| 84 | 2026-05-02 | -7950 | 259856.37 | 195356.37 | 254456.37 | 259856.37 | 0 | event_1741 |
| 85 | 2026-05-03 | 0 | 259856.37 | 195356.37 | 254456.37 | 259856.37 | 0 | (empty) |
| 86 | 2026-05-04 | 0 | 259856.37 | 195356.37 | 254456.37 | 259856.37 | 0 | (empty) |
| 87 | 2026-05-05 | -7665.16 | 252191.21 | 187691.21 | 246791.21 | 252191.21 | 0 | event_1742 |
| 88 | 2026-05-06 | -3290 | 248901.21 | 184401.21 | 243501.21 | 248901.21 | 0 | event_1743 |
| 89 | 2026-05-07 | -11414.67 | 237486.54 | 172986.54 | 232086.54 | 237486.54 | 0 | event_1774, event_1737 |
| 90 | 2026-05-08 | 0 | 237486.54 | 172986.54 | 232086.54 | 237486.54 | 0 | (empty) |

## request_21 â€” user_21 (USD)

Request: 1574.4 on 2026-04-03; deadline 2026-04-14. Opening 3911.35; minimum 1800.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 1543.35 | 1574.4 | NO |
| affordability_status | affordable_with_plan | affordable_now | NO |
| recommended_payment_method | full_payment | full_payment | yes |
| payment_plan | 2026-04-03:1574.40 | 2026-04-03:1574.40 | yes |
| earliest_date_for_full_payment | 2026-04-15 | 2026-04-03 | NO |
| spending_changes_needed | stop:event_1815\|reduce_to:event_1816:23.50 | none | NO |

Baseline trough: day 9 (2026-04-12), balance 3473.13, headroom 1673.13.

Protected: rent|utilities|groceries. Reduce: dining|streaming|shopping. Stop: streaming|cloud_storage.

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1815 | cloud_storage / Online backup subscription | 5 / 5 | 11 | 11.00 | 11â€“11 | 11 | 2026-04-12, 2026-05-12, 2026-06-12 |
| event_1854 | dining / Neighbourhood restaurant | 9 / 6 | 83.43555555555555555555555556 | 85.96 | 60.18â€“100.63 | 83.44 | 2026-04-17, 2026-05-08, 2026-05-29, 2026-06-19 |
| event_1836 | groceries / Local market purchase | 18 / 6 | 83.62833333333333333333333333 | 81.85 | 65.93â€“104.23 | 83.63 | 2026-04-06, 2026-04-16, 2026-04-26, 2026-05-06, 2026-05-16, 2026-05-26, 2026-06-05, 2026-06-15, 2026-06-25 |
| event_1818 | rent / Residential rent payment | 6 / 6 | 718.8 | 718.80 | 718.8â€“718.8 | 718.8 | 2026-05-02, 2026-06-02, 2026-07-02 |
| event_1817 | shopping / Monthly shopping spend | 5 / 5 | 122.414 | 120.74 | 115.71â€“133.38 | 122.41 | 2026-04-12, 2026-05-12, 2026-06-12 |
| event_1816 | streaming / Streaming subscription | 5 / 5 | 47 | 47.00 | 47â€“47 | 47 | 2026-04-09, 2026-05-09, 2026-06-09 |
| event_1845 | transport / Rail pass | 9 / 6 | 41.20333333333333333333333333 | 38.96 | 33.38â€“51.42 | 41.2 | 2026-04-16, 2026-05-07, 2026-05-28, 2026-06-18 |
| event_1814 | utilities / Municipal utilities | 5 / 5 | 121.176 | 122.18 | 115.31â€“124.08 | 121.18 | 2026-04-06, 2026-05-06, 2026-06-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-04-05 | -53 | event_1857 | transport | explicit_event | Pending fuel authorization |
| 2026-04-06 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-04-06 | -121.18 | event_1814 | utilities | recurring_expense | Municipal utilities |
| 2026-04-09 | -47 | event_1816 | streaming | recurring_expense | Streaming subscription |
| 2026-04-12 | -11 | event_1815 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-04-12 | -122.41 | event_1817 | shopping | recurring_expense | Monthly shopping spend |
| 2026-04-15 | 2256 | event_1858 | salary | recurring_income | Next confirmed salary |
| 2026-04-16 | -41.2 | event_1845 | transport | recurring_expense | Rail pass |
| 2026-04-16 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-04-17 | -83.44 | event_1854 | dining | recurring_expense | Neighbourhood restaurant |
| 2026-04-26 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-05-02 | -718.8 | event_1818 | rent | recurring_expense | Residential rent payment |
| 2026-05-06 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-05-06 | -121.18 | event_1814 | utilities | recurring_expense | Municipal utilities |
| 2026-05-07 | -41.2 | event_1845 | transport | recurring_expense | Rail pass |
| 2026-05-08 | -83.44 | event_1854 | dining | recurring_expense | Neighbourhood restaurant |
| 2026-05-09 | -47 | event_1816 | streaming | recurring_expense | Streaming subscription |
| 2026-05-12 | -11 | event_1815 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-05-12 | -122.41 | event_1817 | shopping | recurring_expense | Monthly shopping spend |
| 2026-05-15 | 2256 | event_1858 | salary | recurring_income | Next confirmed salary |
| 2026-05-16 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-05-26 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-05-28 | -41.2 | event_1845 | transport | recurring_expense | Rail pass |
| 2026-05-29 | -83.44 | event_1854 | dining | recurring_expense | Neighbourhood restaurant |
| 2026-06-02 | -718.8 | event_1818 | rent | recurring_expense | Residential rent payment |
| 2026-06-05 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-06-06 | -121.18 | event_1814 | utilities | recurring_expense | Municipal utilities |
| 2026-06-09 | -47 | event_1816 | streaming | recurring_expense | Streaming subscription |
| 2026-06-12 | -11 | event_1815 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-06-12 | -122.41 | event_1817 | shopping | recurring_expense | Monthly shopping spend |
| 2026-06-15 | 2256 | event_1858 | salary | recurring_income | Next confirmed salary |
| 2026-06-15 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-06-18 | -41.2 | event_1845 | transport | recurring_expense | Rail pass |
| 2026-06-19 | -83.44 | event_1854 | dining | recurring_expense | Neighbourhood restaurant |
| 2026-06-25 | -83.63 | event_1836 | groceries | recurring_expense | Local market purchase |
| 2026-07-02 | -718.8 | event_1818 | rent | recurring_expense | Residential rent payment |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-04-03 | 0 | 3911.35 | 2111.35 | 2368 | 2336.95 | 1574.4 | (empty) |
| 1 | 2026-04-04 | 0 | 3911.35 | 2111.35 | 2368 | 2336.95 | 0 | (empty) |
| 2 | 2026-04-05 | -53 | 3858.35 | 2058.35 | 2315 | 2283.95 | 0 | event_1857 |
| 3 | 2026-04-06 | -204.81 | 3653.54 | 1853.54 | 2110.19 | 2079.14 | 0 | event_1836, event_1814 |
| 4 | 2026-04-07 | 0 | 3653.54 | 1853.54 | 2110.19 | 2079.14 | 0 | (empty) |
| 5 | 2026-04-08 | 0 | 3653.54 | 1853.54 | 2110.19 | 2079.14 | 0 | (empty) |
| 6 | 2026-04-09 | -47 | 3606.54 | 1806.54 | 2063.19 | 2032.14 | 0 | event_1816 |
| 7 | 2026-04-10 | 0 | 3606.54 | 1806.54 | 2063.19 | 2032.14 | 0 | (empty) |
| 8 | 2026-04-11 | 0 | 3606.54 | 1806.54 | 2063.19 | 2032.14 | 0 | (empty) |
| 9 | 2026-04-12 | -133.41 | 3473.13 | 1673.13 | 1929.78 | 1898.73 | 0 | event_1815, event_1817 |
| 10 | 2026-04-13 | 0 | 3473.13 | 1673.13 | 1929.78 | 1898.73 | 0 | (empty) |
| 11 | 2026-04-14 | 0 | 3473.13 | 1673.13 | 1929.78 | 1898.73 | 0 | (empty) |
| 12 | 2026-04-15 | 2256 | 5729.13 | 3929.13 | 4185.78 | 4154.73 | 0 | event_1858 |
| 13 | 2026-04-16 | -124.83 | 5604.3 | 3804.3 | 4060.95 | 4029.9 | 0 | event_1845, event_1836 |
| 14 | 2026-04-17 | -83.44 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | event_1854 |
| 15 | 2026-04-18 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 16 | 2026-04-19 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 17 | 2026-04-20 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 18 | 2026-04-21 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 19 | 2026-04-22 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 20 | 2026-04-23 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 21 | 2026-04-24 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 22 | 2026-04-25 | 0 | 5520.86 | 3720.86 | 3977.51 | 3946.46 | 0 | (empty) |
| 23 | 2026-04-26 | -83.63 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | event_1836 |
| 24 | 2026-04-27 | 0 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | (empty) |
| 25 | 2026-04-28 | 0 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | (empty) |
| 26 | 2026-04-29 | 0 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | (empty) |
| 27 | 2026-04-30 | 0 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | (empty) |
| 28 | 2026-05-01 | 0 | 5437.23 | 3637.23 | 3893.88 | 3862.83 | 0 | (empty) |
| 29 | 2026-05-02 | -718.8 | 4718.43 | 2918.43 | 3175.08 | 3144.03 | 0 | event_1818 |
| 30 | 2026-05-03 | 0 | 4718.43 | 2918.43 | 3175.08 | 3144.03 | 0 | (empty) |
| 31 | 2026-05-04 | 0 | 4718.43 | 2918.43 | 3175.08 | 3144.03 | 0 | (empty) |
| 32 | 2026-05-05 | 0 | 4718.43 | 2918.43 | 3175.08 | 3144.03 | 0 | (empty) |
| 33 | 2026-05-06 | -204.81 | 4513.62 | 2713.62 | 2970.27 | 2939.22 | 0 | event_1836, event_1814 |
| 34 | 2026-05-07 | -41.2 | 4472.42 | 2672.42 | 2929.07 | 2898.02 | 0 | event_1845 |
| 35 | 2026-05-08 | -83.44 | 4388.98 | 2588.98 | 2845.63 | 2814.58 | 0 | event_1854 |
| 36 | 2026-05-09 | -47 | 4341.98 | 2541.98 | 2798.63 | 2767.58 | 0 | event_1816 |
| 37 | 2026-05-10 | 0 | 4341.98 | 2541.98 | 2798.63 | 2767.58 | 0 | (empty) |
| 38 | 2026-05-11 | 0 | 4341.98 | 2541.98 | 2798.63 | 2767.58 | 0 | (empty) |
| 39 | 2026-05-12 | -133.41 | 4208.57 | 2408.57 | 2665.22 | 2634.17 | 0 | event_1815, event_1817 |
| 40 | 2026-05-13 | 0 | 4208.57 | 2408.57 | 2665.22 | 2634.17 | 0 | (empty) |
| 41 | 2026-05-14 | 0 | 4208.57 | 2408.57 | 2665.22 | 2634.17 | 0 | (empty) |
| 42 | 2026-05-15 | 2256 | 6464.57 | 4664.57 | 4921.22 | 4890.17 | 0 | event_1858 |
| 43 | 2026-05-16 | -83.63 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | event_1836 |
| 44 | 2026-05-17 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 45 | 2026-05-18 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 46 | 2026-05-19 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 47 | 2026-05-20 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 48 | 2026-05-21 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 49 | 2026-05-22 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 50 | 2026-05-23 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 51 | 2026-05-24 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 52 | 2026-05-25 | 0 | 6380.94 | 4580.94 | 4837.59 | 4806.54 | 0 | (empty) |
| 53 | 2026-05-26 | -83.63 | 6297.31 | 4497.31 | 4753.96 | 4722.91 | 0 | event_1836 |
| 54 | 2026-05-27 | 0 | 6297.31 | 4497.31 | 4753.96 | 4722.91 | 0 | (empty) |
| 55 | 2026-05-28 | -41.2 | 6256.11 | 4456.11 | 4712.76 | 4681.71 | 0 | event_1845 |
| 56 | 2026-05-29 | -83.44 | 6172.67 | 4372.67 | 4629.32 | 4598.27 | 0 | event_1854 |
| 57 | 2026-05-30 | 0 | 6172.67 | 4372.67 | 4629.32 | 4598.27 | 0 | (empty) |
| 58 | 2026-05-31 | 0 | 6172.67 | 4372.67 | 4629.32 | 4598.27 | 0 | (empty) |
| 59 | 2026-06-01 | 0 | 6172.67 | 4372.67 | 4629.32 | 4598.27 | 0 | (empty) |
| 60 | 2026-06-02 | -718.8 | 5453.87 | 3653.87 | 3910.52 | 3879.47 | 0 | event_1818 |
| 61 | 2026-06-03 | 0 | 5453.87 | 3653.87 | 3910.52 | 3879.47 | 0 | (empty) |
| 62 | 2026-06-04 | 0 | 5453.87 | 3653.87 | 3910.52 | 3879.47 | 0 | (empty) |
| 63 | 2026-06-05 | -83.63 | 5370.24 | 3570.24 | 3826.89 | 3795.84 | 0 | event_1836 |
| 64 | 2026-06-06 | -121.18 | 5249.06 | 3449.06 | 3705.71 | 3674.66 | 0 | event_1814 |
| 65 | 2026-06-07 | 0 | 5249.06 | 3449.06 | 3705.71 | 3674.66 | 0 | (empty) |
| 66 | 2026-06-08 | 0 | 5249.06 | 3449.06 | 3705.71 | 3674.66 | 0 | (empty) |
| 67 | 2026-06-09 | -47 | 5202.06 | 3402.06 | 3658.71 | 3627.66 | 0 | event_1816 |
| 68 | 2026-06-10 | 0 | 5202.06 | 3402.06 | 3658.71 | 3627.66 | 0 | (empty) |
| 69 | 2026-06-11 | 0 | 5202.06 | 3402.06 | 3658.71 | 3627.66 | 0 | (empty) |
| 70 | 2026-06-12 | -133.41 | 5068.65 | 3268.65 | 3525.3 | 3494.25 | 0 | event_1815, event_1817 |
| 71 | 2026-06-13 | 0 | 5068.65 | 3268.65 | 3525.3 | 3494.25 | 0 | (empty) |
| 72 | 2026-06-14 | 0 | 5068.65 | 3268.65 | 3525.3 | 3494.25 | 0 | (empty) |
| 73 | 2026-06-15 | 2172.37 | 7241.02 | 5441.02 | 5697.67 | 5666.62 | 0 | event_1858, event_1836 |
| 74 | 2026-06-16 | 0 | 7241.02 | 5441.02 | 5697.67 | 5666.62 | 0 | (empty) |
| 75 | 2026-06-17 | 0 | 7241.02 | 5441.02 | 5697.67 | 5666.62 | 0 | (empty) |
| 76 | 2026-06-18 | -41.2 | 7199.82 | 5399.82 | 5656.47 | 5625.42 | 0 | event_1845 |
| 77 | 2026-06-19 | -83.44 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | event_1854 |
| 78 | 2026-06-20 | 0 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | (empty) |
| 79 | 2026-06-21 | 0 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | (empty) |
| 80 | 2026-06-22 | 0 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | (empty) |
| 81 | 2026-06-23 | 0 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | (empty) |
| 82 | 2026-06-24 | 0 | 7116.38 | 5316.38 | 5573.03 | 5541.98 | 0 | (empty) |
| 83 | 2026-06-25 | -83.63 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | event_1836 |
| 84 | 2026-06-26 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 85 | 2026-06-27 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 86 | 2026-06-28 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 87 | 2026-06-29 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 88 | 2026-06-30 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 89 | 2026-07-01 | 0 | 7032.75 | 5232.75 | 5489.4 | 5458.35 | 0 | (empty) |
| 90 | 2026-07-02 | -718.8 | 6313.95 | 4513.95 | 4770.6 | 4739.55 | 0 | event_1818 |

## request_22 â€” user_22 (EUR)

Request: 731.5 on 2024-12-05; deadline 2025-02-10. Opening 1132.46; minimum 500.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 475.46 | 480.69 | NO |
| affordability_status | affordable_with_plan | affordable_with_plan | yes |
| recommended_payment_method | installments | installments | yes |
| payment_plan | 2024-12-08:253.59\|2025-01-05:253.59\|2025-02-02:253.59 | 2024-12-08:253.59\|2025-01-05:253.59\|2025-02-02:253.59 | yes |
| earliest_date_for_full_payment | 2025-01-15 | 2025-01-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 9 (2024-12-14), balance 980.69, headroom 480.69.

Protected: rent|groceries|transport. Reduce: . Stop: gym|music_subscription.

Salary mode: historical. Evidence: message_15. Unparsed messages: none.

- message_15 (financial_service, 2024-12-02T09:30:00Z): Here’s the latest account information from ClearFund. Your portfolio’s displayed market value has increased substantially. No units have been sold and no cash proceeds have been generated. The displayed value will continue to move with market prices. Account ref FIN-0015.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_1891 | delivery_membership / Food delivery membership | 5 / 5 | 5 | 5.00 | 5â€“5 | 5 | 2024-12-14, 2025-01-14, 2025-02-14 |
| event_1893 | entertainment / Weekend entertainment | 5 / 5 | 20.866 | 20.43 | 18.94â€“23.29 | 20.87 | 2024-12-15, 2025-01-15, 2025-02-15 |
| event_1920 | groceries / Fresh food shop | 26 / 7 | 23.95384615384615384615384615 | 23.43 | 18.35â€“29.81 | 23.95 | 2024-12-11, 2024-12-18, 2024-12-25, 2025-01-01, 2025-01-08, 2025-01-15, 2025-01-22, 2025-01-29, 2025-02-05, 2025-02-12, 2025-02-19, 2025-02-26, 2025-03-05 |
| event_1892 | gym / Gym membership | 5 / 5 | 17 | 17.00 | 17â€“17 | 17 | 2024-12-11, 2025-01-11, 2025-02-11 |
| event_1890 | music_subscription / Music service subscription | 5 / 5 | 6 | 6.00 | 6â€“6 | 6 | 2024-12-12, 2025-01-12, 2025-02-12 |
| event_1894 | rent / Apartment rent transfer | 6 / 6 | 178.2 | 178.20 | 178.2â€“178.2 | 178.2 | 2025-01-03, 2025-02-03, 2025-03-03 |
| event_1945 | transport / Metro and bus fares | 25 / 6 | 13.1328 | 12.70 | 9.7â€“16.34 | 13.13 | 2024-12-05, 2024-12-12, 2024-12-19, 2024-12-26, 2025-01-02, 2025-01-09, 2025-01-16, 2025-01-23, 2025-01-30, 2025-02-06, 2025-02-13, 2025-02-20, 2025-02-27 |
| event_1889 | utilities / Electricity and water bill | 5 / 5 | 30.56 | 31.52 | 27.34â€“33.73 | 30.56 | 2024-12-07, 2025-01-07, 2025-02-07 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-12-05 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2024-12-07 | -30.56 | event_1889 | utilities | recurring_expense | Electricity and water bill |
| 2024-12-08 | -43 | event_1961 | shopping | explicit_event | Pending merchant debit |
| 2024-12-11 | -17 | event_1892 | gym | recurring_expense | Gym membership |
| 2024-12-11 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2024-12-12 | -6 | event_1890 | music_subscription | recurring_expense | Music service subscription |
| 2024-12-12 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2024-12-14 | -5 | event_1891 | delivery_membership | recurring_expense | Food delivery membership |
| 2024-12-15 | 616 | event_1887 | salary | recurring_income | Payroll credit |
| 2024-12-15 | -20.87 | event_1893 | entertainment | recurring_expense | Weekend entertainment |
| 2024-12-18 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2024-12-19 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2024-12-25 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2024-12-26 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-01-01 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-01-02 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-01-03 | -178.2 | event_1894 | rent | recurring_expense | Apartment rent transfer |
| 2025-01-07 | -30.56 | event_1889 | utilities | recurring_expense | Electricity and water bill |
| 2025-01-08 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-01-09 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-01-11 | -17 | event_1892 | gym | recurring_expense | Gym membership |
| 2025-01-12 | -6 | event_1890 | music_subscription | recurring_expense | Music service subscription |
| 2025-01-14 | -5 | event_1891 | delivery_membership | recurring_expense | Food delivery membership |
| 2025-01-15 | 616 | event_1887 | salary | recurring_income | Payroll credit |
| 2025-01-15 | -20.87 | event_1893 | entertainment | recurring_expense | Weekend entertainment |
| 2025-01-15 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-01-16 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-01-22 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-01-23 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-01-29 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-01-30 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-02-03 | -178.2 | event_1894 | rent | recurring_expense | Apartment rent transfer |
| 2025-02-05 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-02-06 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-02-07 | -30.56 | event_1889 | utilities | recurring_expense | Electricity and water bill |
| 2025-02-11 | -17 | event_1892 | gym | recurring_expense | Gym membership |
| 2025-02-12 | -6 | event_1890 | music_subscription | recurring_expense | Music service subscription |
| 2025-02-12 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-02-13 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-02-14 | -5 | event_1891 | delivery_membership | recurring_expense | Food delivery membership |
| 2025-02-15 | 616 | event_1887 | salary | recurring_income | Payroll credit |
| 2025-02-15 | -20.87 | event_1893 | entertainment | recurring_expense | Weekend entertainment |
| 2025-02-19 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-02-20 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-02-26 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |
| 2025-02-27 | -13.13 | event_1945 | transport | recurring_expense | Metro and bus fares |
| 2025-03-03 | -178.2 | event_1894 | rent | recurring_expense | Apartment rent transfer |
| 2025-03-05 | -23.95 | event_1920 | groceries | recurring_expense | Fresh food shop |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-12-05 | -13.13 | 1119.33 | 619.33 | 643.87 | 1119.33 | 0 | event_1945 |
| 1 | 2024-12-06 | 0 | 1119.33 | 619.33 | 643.87 | 1119.33 | 0 | (empty) |
| 2 | 2024-12-07 | -30.56 | 1088.77 | 588.77 | 613.31 | 1088.77 | 0 | event_1889 |
| 3 | 2024-12-08 | -43 | 1045.77 | 545.77 | 570.31 | 792.18 | 253.59 | event_1961 |
| 4 | 2024-12-09 | 0 | 1045.77 | 545.77 | 570.31 | 792.18 | 0 | (empty) |
| 5 | 2024-12-10 | 0 | 1045.77 | 545.77 | 570.31 | 792.18 | 0 | (empty) |
| 6 | 2024-12-11 | -40.95 | 1004.82 | 504.82 | 529.36 | 751.23 | 0 | event_1892, event_1920 |
| 7 | 2024-12-12 | -19.13 | 985.69 | 485.69 | 510.23 | 732.1 | 0 | event_1890, event_1945 |
| 8 | 2024-12-13 | 0 | 985.69 | 485.69 | 510.23 | 732.1 | 0 | (empty) |
| 9 | 2024-12-14 | -5 | 980.69 | 480.69 | 505.23 | 727.1 | 0 | event_1891 |
| 10 | 2024-12-15 | 595.13 | 1575.82 | 1075.82 | 1100.36 | 1322.23 | 0 | event_1887, event_1893 |
| 11 | 2024-12-16 | 0 | 1575.82 | 1075.82 | 1100.36 | 1322.23 | 0 | (empty) |
| 12 | 2024-12-17 | 0 | 1575.82 | 1075.82 | 1100.36 | 1322.23 | 0 | (empty) |
| 13 | 2024-12-18 | -23.95 | 1551.87 | 1051.87 | 1076.41 | 1298.28 | 0 | event_1920 |
| 14 | 2024-12-19 | -13.13 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | event_1945 |
| 15 | 2024-12-20 | 0 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | (empty) |
| 16 | 2024-12-21 | 0 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | (empty) |
| 17 | 2024-12-22 | 0 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | (empty) |
| 18 | 2024-12-23 | 0 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | (empty) |
| 19 | 2024-12-24 | 0 | 1538.74 | 1038.74 | 1063.28 | 1285.15 | 0 | (empty) |
| 20 | 2024-12-25 | -23.95 | 1514.79 | 1014.79 | 1039.33 | 1261.2 | 0 | event_1920 |
| 21 | 2024-12-26 | -13.13 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | event_1945 |
| 22 | 2024-12-27 | 0 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | (empty) |
| 23 | 2024-12-28 | 0 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | (empty) |
| 24 | 2024-12-29 | 0 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | (empty) |
| 25 | 2024-12-30 | 0 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | (empty) |
| 26 | 2024-12-31 | 0 | 1501.66 | 1001.66 | 1026.2 | 1248.07 | 0 | (empty) |
| 27 | 2025-01-01 | -23.95 | 1477.71 | 977.71 | 1002.25 | 1224.12 | 0 | event_1920 |
| 28 | 2025-01-02 | -13.13 | 1464.58 | 964.58 | 989.12 | 1210.99 | 0 | event_1945 |
| 29 | 2025-01-03 | -178.2 | 1286.38 | 786.38 | 810.92 | 1032.79 | 0 | event_1894 |
| 30 | 2025-01-04 | 0 | 1286.38 | 786.38 | 810.92 | 1032.79 | 0 | (empty) |
| 31 | 2025-01-05 | 0 | 1286.38 | 786.38 | 810.92 | 779.2 | 253.59 | (empty) |
| 32 | 2025-01-06 | 0 | 1286.38 | 786.38 | 810.92 | 779.2 | 0 | (empty) |
| 33 | 2025-01-07 | -30.56 | 1255.82 | 755.82 | 780.36 | 748.64 | 0 | event_1889 |
| 34 | 2025-01-08 | -23.95 | 1231.87 | 731.87 | 756.41 | 724.69 | 0 | event_1920 |
| 35 | 2025-01-09 | -13.13 | 1218.74 | 718.74 | 743.28 | 711.56 | 0 | event_1945 |
| 36 | 2025-01-10 | 0 | 1218.74 | 718.74 | 743.28 | 711.56 | 0 | (empty) |
| 37 | 2025-01-11 | -17 | 1201.74 | 701.74 | 726.28 | 694.56 | 0 | event_1892 |
| 38 | 2025-01-12 | -6 | 1195.74 | 695.74 | 720.28 | 688.56 | 0 | event_1890 |
| 39 | 2025-01-13 | 0 | 1195.74 | 695.74 | 720.28 | 688.56 | 0 | (empty) |
| 40 | 2025-01-14 | -5 | 1190.74 | 690.74 | 715.28 | 683.56 | 0 | event_1891 |
| 41 | 2025-01-15 | 571.18 | 1761.92 | 1261.92 | 1286.46 | 1254.74 | 0 | event_1887, event_1893, event_1920 |
| 42 | 2025-01-16 | -13.13 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | event_1945 |
| 43 | 2025-01-17 | 0 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | (empty) |
| 44 | 2025-01-18 | 0 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | (empty) |
| 45 | 2025-01-19 | 0 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | (empty) |
| 46 | 2025-01-20 | 0 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | (empty) |
| 47 | 2025-01-21 | 0 | 1748.79 | 1248.79 | 1273.33 | 1241.61 | 0 | (empty) |
| 48 | 2025-01-22 | -23.95 | 1724.84 | 1224.84 | 1249.38 | 1217.66 | 0 | event_1920 |
| 49 | 2025-01-23 | -13.13 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | event_1945 |
| 50 | 2025-01-24 | 0 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | (empty) |
| 51 | 2025-01-25 | 0 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | (empty) |
| 52 | 2025-01-26 | 0 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | (empty) |
| 53 | 2025-01-27 | 0 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | (empty) |
| 54 | 2025-01-28 | 0 | 1711.71 | 1211.71 | 1236.25 | 1204.53 | 0 | (empty) |
| 55 | 2025-01-29 | -23.95 | 1687.76 | 1187.76 | 1212.3 | 1180.58 | 0 | event_1920 |
| 56 | 2025-01-30 | -13.13 | 1674.63 | 1174.63 | 1199.17 | 1167.45 | 0 | event_1945 |
| 57 | 2025-01-31 | 0 | 1674.63 | 1174.63 | 1199.17 | 1167.45 | 0 | (empty) |
| 58 | 2025-02-01 | 0 | 1674.63 | 1174.63 | 1199.17 | 1167.45 | 0 | (empty) |
| 59 | 2025-02-02 | 0 | 1674.63 | 1174.63 | 1199.17 | 913.86 | 253.59 | (empty) |
| 60 | 2025-02-03 | -178.2 | 1496.43 | 996.43 | 1020.97 | 735.66 | 0 | event_1894 |
| 61 | 2025-02-04 | 0 | 1496.43 | 996.43 | 1020.97 | 735.66 | 0 | (empty) |
| 62 | 2025-02-05 | -23.95 | 1472.48 | 972.48 | 997.02 | 711.71 | 0 | event_1920 |
| 63 | 2025-02-06 | -13.13 | 1459.35 | 959.35 | 983.89 | 698.58 | 0 | event_1945 |
| 64 | 2025-02-07 | -30.56 | 1428.79 | 928.79 | 953.33 | 668.02 | 0 | event_1889 |
| 65 | 2025-02-08 | 0 | 1428.79 | 928.79 | 953.33 | 668.02 | 0 | (empty) |
| 66 | 2025-02-09 | 0 | 1428.79 | 928.79 | 953.33 | 668.02 | 0 | (empty) |
| 67 | 2025-02-10 | 0 | 1428.79 | 928.79 | 953.33 | 668.02 | 0 | (empty) |
| 68 | 2025-02-11 | -17 | 1411.79 | 911.79 | 936.33 | 651.02 | 0 | event_1892 |
| 69 | 2025-02-12 | -29.95 | 1381.84 | 881.84 | 906.38 | 621.07 | 0 | event_1890, event_1920 |
| 70 | 2025-02-13 | -13.13 | 1368.71 | 868.71 | 893.25 | 607.94 | 0 | event_1945 |
| 71 | 2025-02-14 | -5 | 1363.71 | 863.71 | 888.25 | 602.94 | 0 | event_1891 |
| 72 | 2025-02-15 | 595.13 | 1958.84 | 1458.84 | 1483.38 | 1198.07 | 0 | event_1887, event_1893 |
| 73 | 2025-02-16 | 0 | 1958.84 | 1458.84 | 1483.38 | 1198.07 | 0 | (empty) |
| 74 | 2025-02-17 | 0 | 1958.84 | 1458.84 | 1483.38 | 1198.07 | 0 | (empty) |
| 75 | 2025-02-18 | 0 | 1958.84 | 1458.84 | 1483.38 | 1198.07 | 0 | (empty) |
| 76 | 2025-02-19 | -23.95 | 1934.89 | 1434.89 | 1459.43 | 1174.12 | 0 | event_1920 |
| 77 | 2025-02-20 | -13.13 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | event_1945 |
| 78 | 2025-02-21 | 0 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | (empty) |
| 79 | 2025-02-22 | 0 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | (empty) |
| 80 | 2025-02-23 | 0 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | (empty) |
| 81 | 2025-02-24 | 0 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | (empty) |
| 82 | 2025-02-25 | 0 | 1921.76 | 1421.76 | 1446.3 | 1160.99 | 0 | (empty) |
| 83 | 2025-02-26 | -23.95 | 1897.81 | 1397.81 | 1422.35 | 1137.04 | 0 | event_1920 |
| 84 | 2025-02-27 | -13.13 | 1884.68 | 1384.68 | 1409.22 | 1123.91 | 0 | event_1945 |
| 85 | 2025-02-28 | 0 | 1884.68 | 1384.68 | 1409.22 | 1123.91 | 0 | (empty) |
| 86 | 2025-03-01 | 0 | 1884.68 | 1384.68 | 1409.22 | 1123.91 | 0 | (empty) |
| 87 | 2025-03-02 | 0 | 1884.68 | 1384.68 | 1409.22 | 1123.91 | 0 | (empty) |
| 88 | 2025-03-03 | -178.2 | 1706.48 | 1206.48 | 1231.02 | 945.71 | 0 | event_1894 |
| 89 | 2025-03-04 | 0 | 1706.48 | 1206.48 | 1231.02 | 945.71 | 0 | (empty) |
| 90 | 2025-03-05 | -23.95 | 1682.53 | 1182.53 | 1207.07 | 921.76 | 0 | event_1920 |

## request_23 â€” user_23 (ZAR)

Request: 38016 on 2025-05-07; deadline 2025-07-15. Opening 51957.9; minimum 27000.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 9152 | 8360.17 | NO |
| affordability_status | affordable_later | affordable_later | yes |
| recommended_payment_method | wait | wait | yes |
| payment_plan | 2025-07-15:38016 | 2025-07-15:38016 | yes |
| earliest_date_for_full_payment | 2025-07-15 | 2025-07-15 | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 7 (2025-05-14), balance 35360.17, headroom 8360.17.

Protected: rent|healthcare|family_support|groceries. Reduce: shopping. Stop: cloud_storage.

Salary mode: historical. Evidence: none. Unparsed messages: message_16.

- message_16 (financial_service, 2025-04-26T09:30:00Z): Here’s the latest account information from DrawPay. Your prize claim has been verified and is still in payment processing. The payment has not been credited to your account yet. We’ll confirm again if and when the money is actually credited. Account ref FIN-0016.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_2000 | cloud_storage / Cloud storage plan | 5 / 5 | 295.9 | 295.90 | 295.9â€“295.9 | 295.9 | 2025-05-14, 2025-06-14, 2025-07-14 |
| event_1997 | debt_repayment / Education loan instalment | 5 / 5 | 5852 | 5852.00 | 5852â€“5852 | 5852 | 2025-05-13, 2025-06-13, 2025-07-13 |
| event_1999 | family_support / Childcare contribution | 5 / 5 | 4270.2 | 4270.20 | 4270.2â€“4270.2 | 4270.2 | 2025-05-15, 2025-06-15, 2025-07-15 |
| event_2027 | groceries / Neighbourhood grocer | 25 / 6 | 1732.476 | 1706.85 | 1257.56â€“2207.92 | 1732.48 | 2025-05-07, 2025-05-14, 2025-05-21, 2025-05-28, 2025-06-04, 2025-06-11, 2025-06-18, 2025-06-25, 2025-07-02, 2025-07-09, 2025-07-16, 2025-07-23, 2025-07-30 |
| event_1998 | healthcare / Clinic payment | 5 / 5 | 1361.55 | 1341.05 | 1317.68â€“1439.91 | 1361.55 | 2025-05-12, 2025-06-12, 2025-07-12 |
| event_2002 | rent / Shared housing rent | 6 / 6 | 15312 | 15312.00 | 15312â€“15312 | 15312 | 2025-06-04, 2025-07-04, 2025-08-04 |
| event_2001 | shopping / Personal shopping | 5 / 5 | 1315.734 | 1281.33 | 1232.23â€“1396.33 | 1315.73 | 2025-05-14, 2025-06-14, 2025-07-14 |
| event_2040 | transport / Metro and bus fares | 13 / 7 | 888.4353846153846153846153846 | 896.02 | 682.68â€“1121.5 | 888.44 | 2025-05-15, 2025-05-29, 2025-06-12, 2025-06-26, 2025-07-10, 2025-07-24 |
| event_1996 | utilities / Electricity bill | 5 / 5 | 2754.386 | 2813.94 | 2484.32â€“2915.67 | 2754.39 | 2025-05-08, 2025-06-08, 2025-07-08 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2025-05-07 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-05-08 | -2754.39 | event_1996 | utilities | recurring_expense | Electricity bill |
| 2025-05-11 | -1553.2 | event_2042 | healthcare | explicit_event | Pending pharmacy card charge |
| 2025-05-12 | -1361.55 | event_1998 | healthcare | recurring_expense | Clinic payment |
| 2025-05-13 | -5852 | event_1997 | debt_repayment | recurring_expense | Education loan instalment |
| 2025-05-14 | -295.9 | event_2000 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-05-14 | -1315.73 | event_2001 | shopping | recurring_expense | Personal shopping |
| 2025-05-14 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-05-15 | 45760 | event_1994 | salary | recurring_income | Payroll credit |
| 2025-05-15 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-05-15 | -4270.2 | event_1999 | family_support | recurring_expense | Childcare contribution |
| 2025-05-21 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-05-28 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-05-29 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-06-04 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-06-04 | -15312 | event_2002 | rent | recurring_expense | Shared housing rent |
| 2025-06-08 | -2754.39 | event_1996 | utilities | recurring_expense | Electricity bill |
| 2025-06-11 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-06-12 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-06-12 | -1361.55 | event_1998 | healthcare | recurring_expense | Clinic payment |
| 2025-06-13 | -5852 | event_1997 | debt_repayment | recurring_expense | Education loan instalment |
| 2025-06-14 | -295.9 | event_2000 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-06-14 | -1315.73 | event_2001 | shopping | recurring_expense | Personal shopping |
| 2025-06-15 | 45760 | event_1994 | salary | recurring_income | Payroll credit |
| 2025-06-15 | -4270.2 | event_1999 | family_support | recurring_expense | Childcare contribution |
| 2025-06-18 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-06-25 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-06-26 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-07-02 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-07-04 | -15312 | event_2002 | rent | recurring_expense | Shared housing rent |
| 2025-07-08 | -2754.39 | event_1996 | utilities | recurring_expense | Electricity bill |
| 2025-07-09 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-07-10 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-07-12 | -1361.55 | event_1998 | healthcare | recurring_expense | Clinic payment |
| 2025-07-13 | -5852 | event_1997 | debt_repayment | recurring_expense | Education loan instalment |
| 2025-07-14 | -295.9 | event_2000 | cloud_storage | recurring_expense | Cloud storage plan |
| 2025-07-14 | -1315.73 | event_2001 | shopping | recurring_expense | Personal shopping |
| 2025-07-15 | 45760 | event_1994 | salary | recurring_income | Payroll credit |
| 2025-07-15 | -4270.2 | event_1999 | family_support | recurring_expense | Childcare contribution |
| 2025-07-16 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-07-23 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-07-24 | -888.44 | event_2040 | transport | recurring_expense | Metro and bus fares |
| 2025-07-30 | -1732.48 | event_2027 | groceries | recurring_expense | Neighbourhood grocer |
| 2025-08-04 | -15312 | event_2002 | rent | recurring_expense | Shared housing rent |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2025-05-07 | -1732.48 | 50225.42 | 23225.42 | 41073.42 | 50225.42 | 0 | event_2027 |
| 1 | 2025-05-08 | -2754.39 | 47471.03 | 20471.03 | 38319.03 | 47471.03 | 0 | event_1996 |
| 2 | 2025-05-09 | 0 | 47471.03 | 20471.03 | 38319.03 | 47471.03 | 0 | (empty) |
| 3 | 2025-05-10 | 0 | 47471.03 | 20471.03 | 38319.03 | 47471.03 | 0 | (empty) |
| 4 | 2025-05-11 | -1553.2 | 45917.83 | 18917.83 | 36765.83 | 45917.83 | 0 | event_2042 |
| 5 | 2025-05-12 | -1361.55 | 44556.28 | 17556.28 | 35404.28 | 44556.28 | 0 | event_1998 |
| 6 | 2025-05-13 | -5852 | 38704.28 | 11704.28 | 29552.28 | 38704.28 | 0 | event_1997 |
| 7 | 2025-05-14 | -3344.11 | 35360.17 | 8360.17 | 26208.17 | 35360.17 | 0 | event_2000, event_2001, event_2027 |
| 8 | 2025-05-15 | 40601.36 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | event_1994, event_2040, event_1999 |
| 9 | 2025-05-16 | 0 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | (empty) |
| 10 | 2025-05-17 | 0 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | (empty) |
| 11 | 2025-05-18 | 0 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | (empty) |
| 12 | 2025-05-19 | 0 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | (empty) |
| 13 | 2025-05-20 | 0 | 75961.53 | 48961.53 | 66809.53 | 75961.53 | 0 | (empty) |
| 14 | 2025-05-21 | -1732.48 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | event_2027 |
| 15 | 2025-05-22 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 16 | 2025-05-23 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 17 | 2025-05-24 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 18 | 2025-05-25 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 19 | 2025-05-26 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 20 | 2025-05-27 | 0 | 74229.05 | 47229.05 | 65077.05 | 74229.05 | 0 | (empty) |
| 21 | 2025-05-28 | -1732.48 | 72496.57 | 45496.57 | 63344.57 | 72496.57 | 0 | event_2027 |
| 22 | 2025-05-29 | -888.44 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | event_2040 |
| 23 | 2025-05-30 | 0 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | (empty) |
| 24 | 2025-05-31 | 0 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | (empty) |
| 25 | 2025-06-01 | 0 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | (empty) |
| 26 | 2025-06-02 | 0 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | (empty) |
| 27 | 2025-06-03 | 0 | 71608.13 | 44608.13 | 62456.13 | 71608.13 | 0 | (empty) |
| 28 | 2025-06-04 | -17044.48 | 54563.65 | 27563.65 | 45411.65 | 54563.65 | 0 | event_2027, event_2002 |
| 29 | 2025-06-05 | 0 | 54563.65 | 27563.65 | 45411.65 | 54563.65 | 0 | (empty) |
| 30 | 2025-06-06 | 0 | 54563.65 | 27563.65 | 45411.65 | 54563.65 | 0 | (empty) |
| 31 | 2025-06-07 | 0 | 54563.65 | 27563.65 | 45411.65 | 54563.65 | 0 | (empty) |
| 32 | 2025-06-08 | -2754.39 | 51809.26 | 24809.26 | 42657.26 | 51809.26 | 0 | event_1996 |
| 33 | 2025-06-09 | 0 | 51809.26 | 24809.26 | 42657.26 | 51809.26 | 0 | (empty) |
| 34 | 2025-06-10 | 0 | 51809.26 | 24809.26 | 42657.26 | 51809.26 | 0 | (empty) |
| 35 | 2025-06-11 | -1732.48 | 50076.78 | 23076.78 | 40924.78 | 50076.78 | 0 | event_2027 |
| 36 | 2025-06-12 | -2249.99 | 47826.79 | 20826.79 | 38674.79 | 47826.79 | 0 | event_2040, event_1998 |
| 37 | 2025-06-13 | -5852 | 41974.79 | 14974.79 | 32822.79 | 41974.79 | 0 | event_1997 |
| 38 | 2025-06-14 | -1611.63 | 40363.16 | 13363.16 | 31211.16 | 40363.16 | 0 | event_2000, event_2001 |
| 39 | 2025-06-15 | 41489.8 | 81852.96 | 54852.96 | 72700.96 | 81852.96 | 0 | event_1994, event_1999 |
| 40 | 2025-06-16 | 0 | 81852.96 | 54852.96 | 72700.96 | 81852.96 | 0 | (empty) |
| 41 | 2025-06-17 | 0 | 81852.96 | 54852.96 | 72700.96 | 81852.96 | 0 | (empty) |
| 42 | 2025-06-18 | -1732.48 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | event_2027 |
| 43 | 2025-06-19 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 44 | 2025-06-20 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 45 | 2025-06-21 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 46 | 2025-06-22 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 47 | 2025-06-23 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 48 | 2025-06-24 | 0 | 80120.48 | 53120.48 | 70968.48 | 80120.48 | 0 | (empty) |
| 49 | 2025-06-25 | -1732.48 | 78388 | 51388 | 69236 | 78388 | 0 | event_2027 |
| 50 | 2025-06-26 | -888.44 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | event_2040 |
| 51 | 2025-06-27 | 0 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | (empty) |
| 52 | 2025-06-28 | 0 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | (empty) |
| 53 | 2025-06-29 | 0 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | (empty) |
| 54 | 2025-06-30 | 0 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | (empty) |
| 55 | 2025-07-01 | 0 | 77499.56 | 50499.56 | 68347.56 | 77499.56 | 0 | (empty) |
| 56 | 2025-07-02 | -1732.48 | 75767.08 | 48767.08 | 66615.08 | 75767.08 | 0 | event_2027 |
| 57 | 2025-07-03 | 0 | 75767.08 | 48767.08 | 66615.08 | 75767.08 | 0 | (empty) |
| 58 | 2025-07-04 | -15312 | 60455.08 | 33455.08 | 51303.08 | 60455.08 | 0 | event_2002 |
| 59 | 2025-07-05 | 0 | 60455.08 | 33455.08 | 51303.08 | 60455.08 | 0 | (empty) |
| 60 | 2025-07-06 | 0 | 60455.08 | 33455.08 | 51303.08 | 60455.08 | 0 | (empty) |
| 61 | 2025-07-07 | 0 | 60455.08 | 33455.08 | 51303.08 | 60455.08 | 0 | (empty) |
| 62 | 2025-07-08 | -2754.39 | 57700.69 | 30700.69 | 48548.69 | 57700.69 | 0 | event_1996 |
| 63 | 2025-07-09 | -1732.48 | 55968.21 | 28968.21 | 46816.21 | 55968.21 | 0 | event_2027 |
| 64 | 2025-07-10 | -888.44 | 55079.77 | 28079.77 | 45927.77 | 55079.77 | 0 | event_2040 |
| 65 | 2025-07-11 | 0 | 55079.77 | 28079.77 | 45927.77 | 55079.77 | 0 | (empty) |
| 66 | 2025-07-12 | -1361.55 | 53718.22 | 26718.22 | 44566.22 | 53718.22 | 0 | event_1998 |
| 67 | 2025-07-13 | -5852 | 47866.22 | 20866.22 | 38714.22 | 47866.22 | 0 | event_1997 |
| 68 | 2025-07-14 | -1611.63 | 46254.59 | 19254.59 | 37102.59 | 46254.59 | 0 | event_2000, event_2001 |
| 69 | 2025-07-15 | 41489.8 | 87744.39 | 60744.39 | 78592.39 | 49728.39 | 38016 | event_1994, event_1999 |
| 70 | 2025-07-16 | -1732.48 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | event_2027 |
| 71 | 2025-07-17 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 72 | 2025-07-18 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 73 | 2025-07-19 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 74 | 2025-07-20 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 75 | 2025-07-21 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 76 | 2025-07-22 | 0 | 86011.91 | 59011.91 | 76859.91 | 47995.91 | 0 | (empty) |
| 77 | 2025-07-23 | -1732.48 | 84279.43 | 57279.43 | 75127.43 | 46263.43 | 0 | event_2027 |
| 78 | 2025-07-24 | -888.44 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | event_2040 |
| 79 | 2025-07-25 | 0 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | (empty) |
| 80 | 2025-07-26 | 0 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | (empty) |
| 81 | 2025-07-27 | 0 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | (empty) |
| 82 | 2025-07-28 | 0 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | (empty) |
| 83 | 2025-07-29 | 0 | 83390.99 | 56390.99 | 74238.99 | 45374.99 | 0 | (empty) |
| 84 | 2025-07-30 | -1732.48 | 81658.51 | 54658.51 | 72506.51 | 43642.51 | 0 | event_2027 |
| 85 | 2025-07-31 | 0 | 81658.51 | 54658.51 | 72506.51 | 43642.51 | 0 | (empty) |
| 86 | 2025-08-01 | 0 | 81658.51 | 54658.51 | 72506.51 | 43642.51 | 0 | (empty) |
| 87 | 2025-08-02 | 0 | 81658.51 | 54658.51 | 72506.51 | 43642.51 | 0 | (empty) |
| 88 | 2025-08-03 | 0 | 81658.51 | 54658.51 | 72506.51 | 43642.51 | 0 | (empty) |
| 89 | 2025-08-04 | -15312 | 66346.51 | 39346.51 | 57194.51 | 28330.51 | 0 | event_2002 |
| 90 | 2025-08-05 | 0 | 66346.51 | 39346.51 | 57194.51 | 28330.51 | 0 | (empty) |

## request_24 â€” user_24 (INR)

Request: 109600 on 2026-01-04; deadline 2026-02-08. Opening 85045; minimum 51000.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 13420 | 13539.29 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 9 (2026-01-13), balance 64539.29, headroom 13539.29.

Protected: rent|insurance|transport. Reduce: dining|streaming. Stop: streaming|cloud_storage.

Salary mode: historical. Evidence: message_17. Unparsed messages: none.

- message_17 (financial_service, 2025-12-29T09:30:00Z): Here’s the latest account information from PrizeTrack. The prize proceeds have reached your account after withholding. The claim is now closed and there are no further scheduled payments. There won’t be another payment unless a separate prize is confirmed. Account ref FIN-0017.

### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_2079 | cloud_storage / Online backup subscription | 5 / 5 | 355 | 355.00 | 355â€“355 | 355 | 2026-01-11, 2026-02-11, 2026-03-11 |
| event_2163 | dining / Takeaway order | 26 / 7 | 1854.036153846153846153846154 | 1902.53 | 1291.44â€“2288.09 | 1854.04 | 2026-01-10, 2026-01-17, 2026-01-24, 2026-01-31, 2026-02-07, 2026-02-14, 2026-02-21, 2026-02-28, 2026-03-07, 2026-03-14, 2026-03-21, 2026-03-28, 2026-04-04 |
| event_2082 | entertainment / Local event tickets | 5 / 5 | 1930.696 | 1896.25 | 1845.75â€“2124.72 | 1930.7 | 2026-01-13, 2026-02-13, 2026-03-13 |
| event_2101 | groceries / Local market purchase | 18 / 6 | 2290.434444444444444444444444 | 2248.73 | 1824.41â€“2958.79 | 2290.43 | 2026-01-06, 2026-01-16, 2026-01-26, 2026-02-05, 2026-02-15, 2026-02-25, 2026-03-07, 2026-03-17, 2026-03-27 |
| event_2078 | insurance / Insurance policy payment | 5 / 5 | 2510 | 2510.00 | 2510â€“2510 | 2510 | 2026-01-06, 2026-02-06, 2026-03-06 |
| event_2083 | rent / Landlord standing order | 6 / 6 | 18600 | 18600.00 | 18600â€“18600 | 18600 | 2026-02-01, 2026-03-01, 2026-04-01 |
| event_2081 | shopping / Monthly shopping spend | 5 / 5 | 2513.652 | 2514.90 | 2398.76â€“2680.78 | 2513.65 | 2026-01-11, 2026-02-11, 2026-03-11 |
| event_2080 | streaming / Family streaming plan | 5 / 5 | 1200 | 1200.00 | 1200â€“1200 | 1200 | 2026-01-08, 2026-02-08, 2026-03-08 |
| event_2137 | transport / Rail pass | 36 / 7 | 1358.991666666666666666666667 | 1330.325 | 1021.64â€“1760.99 | 1358.99 | 2026-01-07, 2026-01-12, 2026-01-17, 2026-01-22, 2026-01-27, 2026-02-01, 2026-02-06, 2026-02-11, 2026-02-16, 2026-02-21, 2026-02-26, 2026-03-03, 2026-03-08, 2026-03-13, 2026-03-18, 2026-03-23, 2026-03-28, 2026-04-02 |
| event_2077 | utilities / Household utility payment | 5 / 5 | 3303.908 | 3335.41 | 3049.81â€“3490.5 | 3303.91 | 2026-01-05, 2026-02-05, 2026-03-05 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2026-01-05 | -3303.91 | event_2077 | utilities | recurring_expense | Household utility payment |
| 2026-01-06 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-01-06 | -2510 | event_2078 | insurance | recurring_expense | Insurance policy payment |
| 2026-01-07 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-01-08 | -1200 | event_2080 | streaming | recurring_expense | Family streaming plan |
| 2026-01-10 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-01-11 | -355 | event_2079 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-01-11 | -1830 | event_2166 | insurance | explicit_event | Scheduled insurance payment |
| 2026-01-11 | -2513.65 | event_2081 | shopping | recurring_expense | Monthly shopping spend |
| 2026-01-12 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-01-13 | -1930.7 | event_2082 | entertainment | recurring_expense | Local event tickets |
| 2026-01-15 | 61000 | event_2075 | salary | recurring_income | Payroll credit |
| 2026-01-16 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-01-17 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-01-17 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-01-22 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-01-24 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-01-26 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-01-27 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-01-31 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-02-01 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-01 | -18600 | event_2083 | rent | recurring_expense | Landlord standing order |
| 2026-02-05 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-02-05 | -3303.91 | event_2077 | utilities | recurring_expense | Household utility payment |
| 2026-02-06 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-06 | -2510 | event_2078 | insurance | recurring_expense | Insurance policy payment |
| 2026-02-07 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-02-08 | -1200 | event_2080 | streaming | recurring_expense | Family streaming plan |
| 2026-02-11 | -355 | event_2079 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-02-11 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-11 | -2513.65 | event_2081 | shopping | recurring_expense | Monthly shopping spend |
| 2026-02-13 | -1930.7 | event_2082 | entertainment | recurring_expense | Local event tickets |
| 2026-02-14 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-02-15 | 61000 | event_2075 | salary | recurring_income | Payroll credit |
| 2026-02-15 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-02-16 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-21 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-21 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-02-25 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-02-26 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-02-28 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-03-01 | -18600 | event_2083 | rent | recurring_expense | Landlord standing order |
| 2026-03-03 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-05 | -3303.91 | event_2077 | utilities | recurring_expense | Household utility payment |
| 2026-03-06 | -2510 | event_2078 | insurance | recurring_expense | Insurance policy payment |
| 2026-03-07 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-03-07 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-03-08 | -1200 | event_2080 | streaming | recurring_expense | Family streaming plan |
| 2026-03-08 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-11 | -355 | event_2079 | cloud_storage | recurring_expense | Online backup subscription |
| 2026-03-11 | -2513.65 | event_2081 | shopping | recurring_expense | Monthly shopping spend |
| 2026-03-13 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-13 | -1930.7 | event_2082 | entertainment | recurring_expense | Local event tickets |
| 2026-03-14 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-03-15 | 61000 | event_2075 | salary | recurring_income | Payroll credit |
| 2026-03-17 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-03-18 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-21 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-03-23 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-27 | -2290.43 | event_2101 | groceries | recurring_expense | Local market purchase |
| 2026-03-28 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-03-28 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |
| 2026-04-01 | -18600 | event_2083 | rent | recurring_expense | Landlord standing order |
| 2026-04-02 | -1358.99 | event_2137 | transport | recurring_expense | Rail pass |
| 2026-04-04 | -1854.04 | event_2163 | dining | recurring_expense | Takeaway order |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-01-04 | 0 | 85045 | 34045 | 71625 | 85045 | 0 | (empty) |
| 1 | 2026-01-05 | -3303.91 | 81741.09 | 30741.09 | 68321.09 | 81741.09 | 0 | event_2077 |
| 2 | 2026-01-06 | -4800.43 | 76940.66 | 25940.66 | 63520.66 | 76940.66 | 0 | event_2101, event_2078 |
| 3 | 2026-01-07 | -1358.99 | 75581.67 | 24581.67 | 62161.67 | 75581.67 | 0 | event_2137 |
| 4 | 2026-01-08 | -1200 | 74381.67 | 23381.67 | 60961.67 | 74381.67 | 0 | event_2080 |
| 5 | 2026-01-09 | 0 | 74381.67 | 23381.67 | 60961.67 | 74381.67 | 0 | (empty) |
| 6 | 2026-01-10 | -1854.04 | 72527.63 | 21527.63 | 59107.63 | 72527.63 | 0 | event_2163 |
| 7 | 2026-01-11 | -4698.65 | 67828.98 | 16828.98 | 54408.98 | 67828.98 | 0 | event_2079, event_2166, event_2081 |
| 8 | 2026-01-12 | -1358.99 | 66469.99 | 15469.99 | 53049.99 | 66469.99 | 0 | event_2137 |
| 9 | 2026-01-13 | -1930.7 | 64539.29 | 13539.29 | 51119.29 | 64539.29 | 0 | event_2082 |
| 10 | 2026-01-14 | 0 | 64539.29 | 13539.29 | 51119.29 | 64539.29 | 0 | (empty) |
| 11 | 2026-01-15 | 61000 | 125539.29 | 74539.29 | 112119.29 | 125539.29 | 0 | event_2075 |
| 12 | 2026-01-16 | -2290.43 | 123248.86 | 72248.86 | 109828.86 | 123248.86 | 0 | event_2101 |
| 13 | 2026-01-17 | -3213.03 | 120035.83 | 69035.83 | 106615.83 | 120035.83 | 0 | event_2137, event_2163 |
| 14 | 2026-01-18 | 0 | 120035.83 | 69035.83 | 106615.83 | 120035.83 | 0 | (empty) |
| 15 | 2026-01-19 | 0 | 120035.83 | 69035.83 | 106615.83 | 120035.83 | 0 | (empty) |
| 16 | 2026-01-20 | 0 | 120035.83 | 69035.83 | 106615.83 | 120035.83 | 0 | (empty) |
| 17 | 2026-01-21 | 0 | 120035.83 | 69035.83 | 106615.83 | 120035.83 | 0 | (empty) |
| 18 | 2026-01-22 | -1358.99 | 118676.84 | 67676.84 | 105256.84 | 118676.84 | 0 | event_2137 |
| 19 | 2026-01-23 | 0 | 118676.84 | 67676.84 | 105256.84 | 118676.84 | 0 | (empty) |
| 20 | 2026-01-24 | -1854.04 | 116822.8 | 65822.8 | 103402.8 | 116822.8 | 0 | event_2163 |
| 21 | 2026-01-25 | 0 | 116822.8 | 65822.8 | 103402.8 | 116822.8 | 0 | (empty) |
| 22 | 2026-01-26 | -2290.43 | 114532.37 | 63532.37 | 101112.37 | 114532.37 | 0 | event_2101 |
| 23 | 2026-01-27 | -1358.99 | 113173.38 | 62173.38 | 99753.38 | 113173.38 | 0 | event_2137 |
| 24 | 2026-01-28 | 0 | 113173.38 | 62173.38 | 99753.38 | 113173.38 | 0 | (empty) |
| 25 | 2026-01-29 | 0 | 113173.38 | 62173.38 | 99753.38 | 113173.38 | 0 | (empty) |
| 26 | 2026-01-30 | 0 | 113173.38 | 62173.38 | 99753.38 | 113173.38 | 0 | (empty) |
| 27 | 2026-01-31 | -1854.04 | 111319.34 | 60319.34 | 97899.34 | 111319.34 | 0 | event_2163 |
| 28 | 2026-02-01 | -19958.99 | 91360.35 | 40360.35 | 77940.35 | 91360.35 | 0 | event_2137, event_2083 |
| 29 | 2026-02-02 | 0 | 91360.35 | 40360.35 | 77940.35 | 91360.35 | 0 | (empty) |
| 30 | 2026-02-03 | 0 | 91360.35 | 40360.35 | 77940.35 | 91360.35 | 0 | (empty) |
| 31 | 2026-02-04 | 0 | 91360.35 | 40360.35 | 77940.35 | 91360.35 | 0 | (empty) |
| 32 | 2026-02-05 | -5594.34 | 85766.01 | 34766.01 | 72346.01 | 85766.01 | 0 | event_2101, event_2077 |
| 33 | 2026-02-06 | -3868.99 | 81897.02 | 30897.02 | 68477.02 | 81897.02 | 0 | event_2137, event_2078 |
| 34 | 2026-02-07 | -1854.04 | 80042.98 | 29042.98 | 66622.98 | 80042.98 | 0 | event_2163 |
| 35 | 2026-02-08 | -1200 | 78842.98 | 27842.98 | 65422.98 | 78842.98 | 0 | event_2080 |
| 36 | 2026-02-09 | 0 | 78842.98 | 27842.98 | 65422.98 | 78842.98 | 0 | (empty) |
| 37 | 2026-02-10 | 0 | 78842.98 | 27842.98 | 65422.98 | 78842.98 | 0 | (empty) |
| 38 | 2026-02-11 | -4227.64 | 74615.34 | 23615.34 | 61195.34 | 74615.34 | 0 | event_2079, event_2137, event_2081 |
| 39 | 2026-02-12 | 0 | 74615.34 | 23615.34 | 61195.34 | 74615.34 | 0 | (empty) |
| 40 | 2026-02-13 | -1930.7 | 72684.64 | 21684.64 | 59264.64 | 72684.64 | 0 | event_2082 |
| 41 | 2026-02-14 | -1854.04 | 70830.6 | 19830.6 | 57410.6 | 70830.6 | 0 | event_2163 |
| 42 | 2026-02-15 | 58709.57 | 129540.17 | 78540.17 | 116120.17 | 129540.17 | 0 | event_2075, event_2101 |
| 43 | 2026-02-16 | -1358.99 | 128181.18 | 77181.18 | 114761.18 | 128181.18 | 0 | event_2137 |
| 44 | 2026-02-17 | 0 | 128181.18 | 77181.18 | 114761.18 | 128181.18 | 0 | (empty) |
| 45 | 2026-02-18 | 0 | 128181.18 | 77181.18 | 114761.18 | 128181.18 | 0 | (empty) |
| 46 | 2026-02-19 | 0 | 128181.18 | 77181.18 | 114761.18 | 128181.18 | 0 | (empty) |
| 47 | 2026-02-20 | 0 | 128181.18 | 77181.18 | 114761.18 | 128181.18 | 0 | (empty) |
| 48 | 2026-02-21 | -3213.03 | 124968.15 | 73968.15 | 111548.15 | 124968.15 | 0 | event_2137, event_2163 |
| 49 | 2026-02-22 | 0 | 124968.15 | 73968.15 | 111548.15 | 124968.15 | 0 | (empty) |
| 50 | 2026-02-23 | 0 | 124968.15 | 73968.15 | 111548.15 | 124968.15 | 0 | (empty) |
| 51 | 2026-02-24 | 0 | 124968.15 | 73968.15 | 111548.15 | 124968.15 | 0 | (empty) |
| 52 | 2026-02-25 | -2290.43 | 122677.72 | 71677.72 | 109257.72 | 122677.72 | 0 | event_2101 |
| 53 | 2026-02-26 | -1358.99 | 121318.73 | 70318.73 | 107898.73 | 121318.73 | 0 | event_2137 |
| 54 | 2026-02-27 | 0 | 121318.73 | 70318.73 | 107898.73 | 121318.73 | 0 | (empty) |
| 55 | 2026-02-28 | -1854.04 | 119464.69 | 68464.69 | 106044.69 | 119464.69 | 0 | event_2163 |
| 56 | 2026-03-01 | -18600 | 100864.69 | 49864.69 | 87444.69 | 100864.69 | 0 | event_2083 |
| 57 | 2026-03-02 | 0 | 100864.69 | 49864.69 | 87444.69 | 100864.69 | 0 | (empty) |
| 58 | 2026-03-03 | -1358.99 | 99505.7 | 48505.7 | 86085.7 | 99505.7 | 0 | event_2137 |
| 59 | 2026-03-04 | 0 | 99505.7 | 48505.7 | 86085.7 | 99505.7 | 0 | (empty) |
| 60 | 2026-03-05 | -3303.91 | 96201.79 | 45201.79 | 82781.79 | 96201.79 | 0 | event_2077 |
| 61 | 2026-03-06 | -2510 | 93691.79 | 42691.79 | 80271.79 | 93691.79 | 0 | event_2078 |
| 62 | 2026-03-07 | -4144.47 | 89547.32 | 38547.32 | 76127.32 | 89547.32 | 0 | event_2163, event_2101 |
| 63 | 2026-03-08 | -2558.99 | 86988.33 | 35988.33 | 73568.33 | 86988.33 | 0 | event_2080, event_2137 |
| 64 | 2026-03-09 | 0 | 86988.33 | 35988.33 | 73568.33 | 86988.33 | 0 | (empty) |
| 65 | 2026-03-10 | 0 | 86988.33 | 35988.33 | 73568.33 | 86988.33 | 0 | (empty) |
| 66 | 2026-03-11 | -2868.65 | 84119.68 | 33119.68 | 70699.68 | 84119.68 | 0 | event_2079, event_2081 |
| 67 | 2026-03-12 | 0 | 84119.68 | 33119.68 | 70699.68 | 84119.68 | 0 | (empty) |
| 68 | 2026-03-13 | -3289.69 | 80829.99 | 29829.99 | 67409.99 | 80829.99 | 0 | event_2137, event_2082 |
| 69 | 2026-03-14 | -1854.04 | 78975.95 | 27975.95 | 65555.95 | 78975.95 | 0 | event_2163 |
| 70 | 2026-03-15 | 61000 | 139975.95 | 88975.95 | 126555.95 | 139975.95 | 0 | event_2075 |
| 71 | 2026-03-16 | 0 | 139975.95 | 88975.95 | 126555.95 | 139975.95 | 0 | (empty) |
| 72 | 2026-03-17 | -2290.43 | 137685.52 | 86685.52 | 124265.52 | 137685.52 | 0 | event_2101 |
| 73 | 2026-03-18 | -1358.99 | 136326.53 | 85326.53 | 122906.53 | 136326.53 | 0 | event_2137 |
| 74 | 2026-03-19 | 0 | 136326.53 | 85326.53 | 122906.53 | 136326.53 | 0 | (empty) |
| 75 | 2026-03-20 | 0 | 136326.53 | 85326.53 | 122906.53 | 136326.53 | 0 | (empty) |
| 76 | 2026-03-21 | -1854.04 | 134472.49 | 83472.49 | 121052.49 | 134472.49 | 0 | event_2163 |
| 77 | 2026-03-22 | 0 | 134472.49 | 83472.49 | 121052.49 | 134472.49 | 0 | (empty) |
| 78 | 2026-03-23 | -1358.99 | 133113.5 | 82113.5 | 119693.5 | 133113.5 | 0 | event_2137 |
| 79 | 2026-03-24 | 0 | 133113.5 | 82113.5 | 119693.5 | 133113.5 | 0 | (empty) |
| 80 | 2026-03-25 | 0 | 133113.5 | 82113.5 | 119693.5 | 133113.5 | 0 | (empty) |
| 81 | 2026-03-26 | 0 | 133113.5 | 82113.5 | 119693.5 | 133113.5 | 0 | (empty) |
| 82 | 2026-03-27 | -2290.43 | 130823.07 | 79823.07 | 117403.07 | 130823.07 | 0 | event_2101 |
| 83 | 2026-03-28 | -3213.03 | 127610.04 | 76610.04 | 114190.04 | 127610.04 | 0 | event_2137, event_2163 |
| 84 | 2026-03-29 | 0 | 127610.04 | 76610.04 | 114190.04 | 127610.04 | 0 | (empty) |
| 85 | 2026-03-30 | 0 | 127610.04 | 76610.04 | 114190.04 | 127610.04 | 0 | (empty) |
| 86 | 2026-03-31 | 0 | 127610.04 | 76610.04 | 114190.04 | 127610.04 | 0 | (empty) |
| 87 | 2026-04-01 | -18600 | 109010.04 | 58010.04 | 95590.04 | 109010.04 | 0 | event_2083 |
| 88 | 2026-04-02 | -1358.99 | 107651.05 | 56651.05 | 94231.05 | 107651.05 | 0 | event_2137 |
| 89 | 2026-04-03 | 0 | 107651.05 | 56651.05 | 94231.05 | 107651.05 | 0 | (empty) |
| 90 | 2026-04-04 | -1854.04 | 105797.01 | 54797.01 | 92377.01 | 105797.01 | 0 | event_2163 |

## request_25 â€” user_25 (IDR)

Request: 60496000 on 2024-03-06; deadline 2024-04-17. Opening 32063050; minimum 23379100.

| Field | Expected | Actual | Match |
| --- | --- | --- | --- |
| amount_safe_to_pay | 1425000 | 2445438.17 | NO |
| affordability_status | not_affordable | not_affordable | yes |
| recommended_payment_method | not_recommended | not_recommended | yes |
| payment_plan | none | none | yes |
| earliest_date_for_full_payment | (empty) | (empty) | yes |
| spending_changes_needed | none | none | yes |

Baseline trough: day 8 (2024-03-14), balance 25824538.17, headroom 2445438.17.

Protected: rent|insurance|transport. Reduce: . Stop: .

Salary mode: historical. Evidence: none. Unparsed messages: none.


### Recurrence assumptions

| Event | Category / description | N / months | Mean | Median | Range | Reserve | Future dates |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_2203 | cloud_storage / Cloud storage plan | 5 / 5 | 126350 | 126350.00 | 126350â€“126350 | 126350 | 2024-03-12, 2024-04-12, 2024-05-12 |
| event_2206 | entertainment / Games and recreation | 5 / 5 | 459592.418 | 451681.59 | 415734.51â€“504697.37 | 459592.42 | 2024-03-14, 2024-04-14, 2024-05-14 |
| event_2225 | groceries / Fresh food shop | 18 / 6 | 1199174.795 | 1231722.845 | 864688.59â€“1510693.45 | 1199174.8 | 2024-03-09, 2024-03-19, 2024-03-29, 2024-04-08, 2024-04-18, 2024-04-28, 2024-05-08, 2024-05-18, 2024-05-28 |
| event_2202 | insurance / Insurance policy payment | 5 / 5 | 904400 | 904400.00 | 904400â€“904400 | 904400 | 2024-03-07, 2024-04-07, 2024-05-07 |
| event_2207 | rent / Monthly rent | 6 / 6 | 6954000 | 6954000.00 | 6954000â€“6954000 | 6954000 | 2024-04-02, 2024-05-02, 2024-06-02 |
| event_2205 | shopping / Monthly shopping spend | 5 / 5 | 1059028.742 | 1054608.50 | 966785.96â€“1170271.29 | 1059028.74 | 2024-03-12, 2024-04-12, 2024-05-12 |
| event_2204 | streaming / Video streaming plan | 5 / 5 | 573800 | 573800.00 | 573800â€“573800 | 573800 | 2024-03-09, 2024-04-09, 2024-05-09 |
| event_2261 | transport / Ride-hailing trip | 36 / 7 | 592511.1469444444444444444444 | 585491.54 | 445484.16â€“745983.26 | 592511.15 | 2024-03-10, 2024-03-15, 2024-03-20, 2024-03-25, 2024-03-30, 2024-04-04, 2024-04-09, 2024-04-14, 2024-04-19, 2024-04-24, 2024-04-29, 2024-05-04, 2024-05-09, 2024-05-14, 2024-05-19, 2024-05-24, 2024-05-29, 2024-06-03 |
| event_2201 | utilities / Household utility payment | 5 / 5 | 1323654.72 | 1338903.44 | 1201903.67â€“1401205.21 | 1323654.72 | 2024-03-06, 2024-04-06, 2024-05-06 |

### Full flow list from trace

| Date | Amount | Event | Category | Origin | Description |
| --- | --- | --- | --- | --- | --- |
| 2024-03-06 | -1323654.72 | event_2201 | utilities | recurring_expense | Household utility payment |
| 2024-03-07 | -904400 | event_2202 | insurance | recurring_expense | Insurance policy payment |
| 2024-03-09 | -573800 | event_2204 | streaming | recurring_expense | Video streaming plan |
| 2024-03-09 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-03-10 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-03-12 | -126350 | event_2203 | cloud_storage | recurring_expense | Cloud storage plan |
| 2024-03-12 | -1059028.74 | event_2205 | shopping | recurring_expense | Monthly shopping spend |
| 2024-03-14 | -459592.42 | event_2206 | entertainment | recurring_expense | Games and recreation |
| 2024-03-15 | 28499994 | event_2288 | salary | recurring_income | Next confirmed salary |
| 2024-03-15 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-03-19 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-03-20 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-03-25 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-03-29 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-03-30 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-02 | -6954000 | event_2207 | rent | recurring_expense | Monthly rent |
| 2024-04-04 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-06 | -1323654.72 | event_2201 | utilities | recurring_expense | Household utility payment |
| 2024-04-07 | -904400 | event_2202 | insurance | recurring_expense | Insurance policy payment |
| 2024-04-08 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-04-09 | -573800 | event_2204 | streaming | recurring_expense | Video streaming plan |
| 2024-04-09 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-12 | -126350 | event_2203 | cloud_storage | recurring_expense | Cloud storage plan |
| 2024-04-12 | -1059028.74 | event_2205 | shopping | recurring_expense | Monthly shopping spend |
| 2024-04-14 | -459592.42 | event_2206 | entertainment | recurring_expense | Games and recreation |
| 2024-04-14 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-15 | 28499994 | event_2288 | salary | recurring_income | Next confirmed salary |
| 2024-04-18 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-04-19 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-24 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-04-28 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-04-29 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-02 | -6954000 | event_2207 | rent | recurring_expense | Monthly rent |
| 2024-05-04 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-06 | -1323654.72 | event_2201 | utilities | recurring_expense | Household utility payment |
| 2024-05-07 | -904400 | event_2202 | insurance | recurring_expense | Insurance policy payment |
| 2024-05-08 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-05-09 | -573800 | event_2204 | streaming | recurring_expense | Video streaming plan |
| 2024-05-09 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-12 | -126350 | event_2203 | cloud_storage | recurring_expense | Cloud storage plan |
| 2024-05-12 | -1059028.74 | event_2205 | shopping | recurring_expense | Monthly shopping spend |
| 2024-05-14 | -459592.42 | event_2206 | entertainment | recurring_expense | Games and recreation |
| 2024-05-14 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-15 | 28499994 | event_2288 | salary | recurring_income | Next confirmed salary |
| 2024-05-18 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-05-19 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-24 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-05-28 | -1199174.8 | event_2225 | groceries | recurring_expense | Fresh food shop |
| 2024-05-29 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |
| 2024-06-02 | -6954000 | event_2207 | rent | recurring_expense | Monthly rent |
| 2024-06-03 | -592511.15 | event_2261 | transport | recurring_expense | Ride-hailing trip |

### Daily running balances

Expected-safe column subtracts the sample's safe amount today with no spending changes. Plan column replays the actual recommendation; for `none` it equals the baseline.

| Day | Date | Net flow | Baseline | Headroom | After expected safe | After plan | Plan payment | Events |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2024-03-06 | -1323654.72 | 30739395.28 | 7360295.28 | 29314395.28 | 30739395.28 | 0 | event_2201 |
| 1 | 2024-03-07 | -904400 | 29834995.28 | 6455895.28 | 28409995.28 | 29834995.28 | 0 | event_2202 |
| 2 | 2024-03-08 | 0 | 29834995.28 | 6455895.28 | 28409995.28 | 29834995.28 | 0 | (empty) |
| 3 | 2024-03-09 | -1772974.8 | 28062020.48 | 4682920.48 | 26637020.48 | 28062020.48 | 0 | event_2204, event_2225 |
| 4 | 2024-03-10 | -592511.15 | 27469509.33 | 4090409.33 | 26044509.33 | 27469509.33 | 0 | event_2261 |
| 5 | 2024-03-11 | 0 | 27469509.33 | 4090409.33 | 26044509.33 | 27469509.33 | 0 | (empty) |
| 6 | 2024-03-12 | -1185378.74 | 26284130.59 | 2905030.59 | 24859130.59 | 26284130.59 | 0 | event_2203, event_2205 |
| 7 | 2024-03-13 | 0 | 26284130.59 | 2905030.59 | 24859130.59 | 26284130.59 | 0 | (empty) |
| 8 | 2024-03-14 | -459592.42 | 25824538.17 | 2445438.17 | 24399538.17 | 25824538.17 | 0 | event_2206 |
| 9 | 2024-03-15 | 27907482.85 | 53732021.02 | 30352921.02 | 52307021.02 | 53732021.02 | 0 | event_2288, event_2261 |
| 10 | 2024-03-16 | 0 | 53732021.02 | 30352921.02 | 52307021.02 | 53732021.02 | 0 | (empty) |
| 11 | 2024-03-17 | 0 | 53732021.02 | 30352921.02 | 52307021.02 | 53732021.02 | 0 | (empty) |
| 12 | 2024-03-18 | 0 | 53732021.02 | 30352921.02 | 52307021.02 | 53732021.02 | 0 | (empty) |
| 13 | 2024-03-19 | -1199174.8 | 52532846.22 | 29153746.22 | 51107846.22 | 52532846.22 | 0 | event_2225 |
| 14 | 2024-03-20 | -592511.15 | 51940335.07 | 28561235.07 | 50515335.07 | 51940335.07 | 0 | event_2261 |
| 15 | 2024-03-21 | 0 | 51940335.07 | 28561235.07 | 50515335.07 | 51940335.07 | 0 | (empty) |
| 16 | 2024-03-22 | 0 | 51940335.07 | 28561235.07 | 50515335.07 | 51940335.07 | 0 | (empty) |
| 17 | 2024-03-23 | 0 | 51940335.07 | 28561235.07 | 50515335.07 | 51940335.07 | 0 | (empty) |
| 18 | 2024-03-24 | 0 | 51940335.07 | 28561235.07 | 50515335.07 | 51940335.07 | 0 | (empty) |
| 19 | 2024-03-25 | -592511.15 | 51347823.92 | 27968723.92 | 49922823.92 | 51347823.92 | 0 | event_2261 |
| 20 | 2024-03-26 | 0 | 51347823.92 | 27968723.92 | 49922823.92 | 51347823.92 | 0 | (empty) |
| 21 | 2024-03-27 | 0 | 51347823.92 | 27968723.92 | 49922823.92 | 51347823.92 | 0 | (empty) |
| 22 | 2024-03-28 | 0 | 51347823.92 | 27968723.92 | 49922823.92 | 51347823.92 | 0 | (empty) |
| 23 | 2024-03-29 | -1199174.8 | 50148649.12 | 26769549.12 | 48723649.12 | 50148649.12 | 0 | event_2225 |
| 24 | 2024-03-30 | -592511.15 | 49556137.97 | 26177037.97 | 48131137.97 | 49556137.97 | 0 | event_2261 |
| 25 | 2024-03-31 | 0 | 49556137.97 | 26177037.97 | 48131137.97 | 49556137.97 | 0 | (empty) |
| 26 | 2024-04-01 | 0 | 49556137.97 | 26177037.97 | 48131137.97 | 49556137.97 | 0 | (empty) |
| 27 | 2024-04-02 | -6954000 | 42602137.97 | 19223037.97 | 41177137.97 | 42602137.97 | 0 | event_2207 |
| 28 | 2024-04-03 | 0 | 42602137.97 | 19223037.97 | 41177137.97 | 42602137.97 | 0 | (empty) |
| 29 | 2024-04-04 | -592511.15 | 42009626.82 | 18630526.82 | 40584626.82 | 42009626.82 | 0 | event_2261 |
| 30 | 2024-04-05 | 0 | 42009626.82 | 18630526.82 | 40584626.82 | 42009626.82 | 0 | (empty) |
| 31 | 2024-04-06 | -1323654.72 | 40685972.1 | 17306872.1 | 39260972.1 | 40685972.1 | 0 | event_2201 |
| 32 | 2024-04-07 | -904400 | 39781572.1 | 16402472.1 | 38356572.1 | 39781572.1 | 0 | event_2202 |
| 33 | 2024-04-08 | -1199174.8 | 38582397.3 | 15203297.3 | 37157397.3 | 38582397.3 | 0 | event_2225 |
| 34 | 2024-04-09 | -1166311.15 | 37416086.15 | 14036986.15 | 35991086.15 | 37416086.15 | 0 | event_2204, event_2261 |
| 35 | 2024-04-10 | 0 | 37416086.15 | 14036986.15 | 35991086.15 | 37416086.15 | 0 | (empty) |
| 36 | 2024-04-11 | 0 | 37416086.15 | 14036986.15 | 35991086.15 | 37416086.15 | 0 | (empty) |
| 37 | 2024-04-12 | -1185378.74 | 36230707.41 | 12851607.41 | 34805707.41 | 36230707.41 | 0 | event_2203, event_2205 |
| 38 | 2024-04-13 | 0 | 36230707.41 | 12851607.41 | 34805707.41 | 36230707.41 | 0 | (empty) |
| 39 | 2024-04-14 | -1052103.57 | 35178603.84 | 11799503.84 | 33753603.84 | 35178603.84 | 0 | event_2206, event_2261 |
| 40 | 2024-04-15 | 28499994 | 63678597.84 | 40299497.84 | 62253597.84 | 63678597.84 | 0 | event_2288 |
| 41 | 2024-04-16 | 0 | 63678597.84 | 40299497.84 | 62253597.84 | 63678597.84 | 0 | (empty) |
| 42 | 2024-04-17 | 0 | 63678597.84 | 40299497.84 | 62253597.84 | 63678597.84 | 0 | (empty) |
| 43 | 2024-04-18 | -1199174.8 | 62479423.04 | 39100323.04 | 61054423.04 | 62479423.04 | 0 | event_2225 |
| 44 | 2024-04-19 | -592511.15 | 61886911.89 | 38507811.89 | 60461911.89 | 61886911.89 | 0 | event_2261 |
| 45 | 2024-04-20 | 0 | 61886911.89 | 38507811.89 | 60461911.89 | 61886911.89 | 0 | (empty) |
| 46 | 2024-04-21 | 0 | 61886911.89 | 38507811.89 | 60461911.89 | 61886911.89 | 0 | (empty) |
| 47 | 2024-04-22 | 0 | 61886911.89 | 38507811.89 | 60461911.89 | 61886911.89 | 0 | (empty) |
| 48 | 2024-04-23 | 0 | 61886911.89 | 38507811.89 | 60461911.89 | 61886911.89 | 0 | (empty) |
| 49 | 2024-04-24 | -592511.15 | 61294400.74 | 37915300.74 | 59869400.74 | 61294400.74 | 0 | event_2261 |
| 50 | 2024-04-25 | 0 | 61294400.74 | 37915300.74 | 59869400.74 | 61294400.74 | 0 | (empty) |
| 51 | 2024-04-26 | 0 | 61294400.74 | 37915300.74 | 59869400.74 | 61294400.74 | 0 | (empty) |
| 52 | 2024-04-27 | 0 | 61294400.74 | 37915300.74 | 59869400.74 | 61294400.74 | 0 | (empty) |
| 53 | 2024-04-28 | -1199174.8 | 60095225.94 | 36716125.94 | 58670225.94 | 60095225.94 | 0 | event_2225 |
| 54 | 2024-04-29 | -592511.15 | 59502714.79 | 36123614.79 | 58077714.79 | 59502714.79 | 0 | event_2261 |
| 55 | 2024-04-30 | 0 | 59502714.79 | 36123614.79 | 58077714.79 | 59502714.79 | 0 | (empty) |
| 56 | 2024-05-01 | 0 | 59502714.79 | 36123614.79 | 58077714.79 | 59502714.79 | 0 | (empty) |
| 57 | 2024-05-02 | -6954000 | 52548714.79 | 29169614.79 | 51123714.79 | 52548714.79 | 0 | event_2207 |
| 58 | 2024-05-03 | 0 | 52548714.79 | 29169614.79 | 51123714.79 | 52548714.79 | 0 | (empty) |
| 59 | 2024-05-04 | -592511.15 | 51956203.64 | 28577103.64 | 50531203.64 | 51956203.64 | 0 | event_2261 |
| 60 | 2024-05-05 | 0 | 51956203.64 | 28577103.64 | 50531203.64 | 51956203.64 | 0 | (empty) |
| 61 | 2024-05-06 | -1323654.72 | 50632548.92 | 27253448.92 | 49207548.92 | 50632548.92 | 0 | event_2201 |
| 62 | 2024-05-07 | -904400 | 49728148.92 | 26349048.92 | 48303148.92 | 49728148.92 | 0 | event_2202 |
| 63 | 2024-05-08 | -1199174.8 | 48528974.12 | 25149874.12 | 47103974.12 | 48528974.12 | 0 | event_2225 |
| 64 | 2024-05-09 | -1166311.15 | 47362662.97 | 23983562.97 | 45937662.97 | 47362662.97 | 0 | event_2204, event_2261 |
| 65 | 2024-05-10 | 0 | 47362662.97 | 23983562.97 | 45937662.97 | 47362662.97 | 0 | (empty) |
| 66 | 2024-05-11 | 0 | 47362662.97 | 23983562.97 | 45937662.97 | 47362662.97 | 0 | (empty) |
| 67 | 2024-05-12 | -1185378.74 | 46177284.23 | 22798184.23 | 44752284.23 | 46177284.23 | 0 | event_2203, event_2205 |
| 68 | 2024-05-13 | 0 | 46177284.23 | 22798184.23 | 44752284.23 | 46177284.23 | 0 | (empty) |
| 69 | 2024-05-14 | -1052103.57 | 45125180.66 | 21746080.66 | 43700180.66 | 45125180.66 | 0 | event_2206, event_2261 |
| 70 | 2024-05-15 | 28499994 | 73625174.66 | 50246074.66 | 72200174.66 | 73625174.66 | 0 | event_2288 |
| 71 | 2024-05-16 | 0 | 73625174.66 | 50246074.66 | 72200174.66 | 73625174.66 | 0 | (empty) |
| 72 | 2024-05-17 | 0 | 73625174.66 | 50246074.66 | 72200174.66 | 73625174.66 | 0 | (empty) |
| 73 | 2024-05-18 | -1199174.8 | 72425999.86 | 49046899.86 | 71000999.86 | 72425999.86 | 0 | event_2225 |
| 74 | 2024-05-19 | -592511.15 | 71833488.71 | 48454388.71 | 70408488.71 | 71833488.71 | 0 | event_2261 |
| 75 | 2024-05-20 | 0 | 71833488.71 | 48454388.71 | 70408488.71 | 71833488.71 | 0 | (empty) |
| 76 | 2024-05-21 | 0 | 71833488.71 | 48454388.71 | 70408488.71 | 71833488.71 | 0 | (empty) |
| 77 | 2024-05-22 | 0 | 71833488.71 | 48454388.71 | 70408488.71 | 71833488.71 | 0 | (empty) |
| 78 | 2024-05-23 | 0 | 71833488.71 | 48454388.71 | 70408488.71 | 71833488.71 | 0 | (empty) |
| 79 | 2024-05-24 | -592511.15 | 71240977.56 | 47861877.56 | 69815977.56 | 71240977.56 | 0 | event_2261 |
| 80 | 2024-05-25 | 0 | 71240977.56 | 47861877.56 | 69815977.56 | 71240977.56 | 0 | (empty) |
| 81 | 2024-05-26 | 0 | 71240977.56 | 47861877.56 | 69815977.56 | 71240977.56 | 0 | (empty) |
| 82 | 2024-05-27 | 0 | 71240977.56 | 47861877.56 | 69815977.56 | 71240977.56 | 0 | (empty) |
| 83 | 2024-05-28 | -1199174.8 | 70041802.76 | 46662702.76 | 68616802.76 | 70041802.76 | 0 | event_2225 |
| 84 | 2024-05-29 | -592511.15 | 69449291.61 | 46070191.61 | 68024291.61 | 69449291.61 | 0 | event_2261 |
| 85 | 2024-05-30 | 0 | 69449291.61 | 46070191.61 | 68024291.61 | 69449291.61 | 0 | (empty) |
| 86 | 2024-05-31 | 0 | 69449291.61 | 46070191.61 | 68024291.61 | 69449291.61 | 0 | (empty) |
| 87 | 2024-06-01 | 0 | 69449291.61 | 46070191.61 | 68024291.61 | 69449291.61 | 0 | (empty) |
| 88 | 2024-06-02 | -6954000 | 62495291.61 | 39116191.61 | 61070291.61 | 62495291.61 | 0 | event_2207 |
| 89 | 2024-06-03 | -592511.15 | 61902780.46 | 38523680.46 | 60477780.46 | 61902780.46 | 0 | event_2261 |
| 90 | 2024-06-04 | 0 | 61902780.46 | 38523680.46 | 60477780.46 | 61902780.46 | 0 | (empty) |
