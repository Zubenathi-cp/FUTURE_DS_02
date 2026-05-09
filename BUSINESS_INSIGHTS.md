# Business Insights - Customer Retention & Churn Analysis

## Executive Summary

This analysis examined **7,032 customers** for a subscription-based business to identify why customers leave, which segments are most at risk, and what actions can improve retention.

**Key finding:** Month-to-month contracts churn at **42.7%** - 15 times higher than two-year contracts at **2.8%**.

---

## Top 3 Churn Drivers

### 1. Contract Type (Biggest Driver)
| Contract Type | Churn Rate | Risk Level |
|--------------|------------|------------|
| Month-to-month | 42.7% | 🔴 Critical |
| One year | 11.3% | 🟡 Medium |
| Two year | 2.8% | 🟢 Low |

**Insight:** Customers on month-to-month contracts are **15x more likely to leave** than two-year customers.

### 2. Payment Method
| Payment Method | Churn Rate |
|----------------|------------|
| Electronic check | 35.2% |
| Mailed check | 25.1% |
| Bank transfer | 18.3% |
| Credit card | 15.2% |

**Insight:** Electronic check users have the highest churn risk.

### 3. Customer Tenure
| Tenure Group | Churn Rate |
|--------------|------------|
| 0-6 months | 45% |
| 6-12 months | 28% |
| 12-24 months | 18% |
| 24+ months | 8% |

**Insight:** **60% of churn happens in the first 6 months** - the onboarding period is critical.

---

## Customer Lifetime Value Analysis

| Metric | Value |
|--------|-------|
| Retained customers tenure | 37.6 months |
| Churned customers tenure | 18.0 months |
| **Value Gap** | **19.6 months** |

**Insight:** Retained customers stay **20 months longer** than churned customers, representing significantly higher lifetime value.

### Tenure by Contract Type
| Contract Type | Average Tenure |
|---------------|----------------|
| Two year | 57.1 months |
| One year | 42.1 months |
| Month-to-month | 18.0 months |

**Insight:** Two-year contract customers stay **3x longer** than month-to-month customers.

---

## High Risk Segment

| Segment | % of Customers | Churn Rate |
|---------|---------------|------------|
| Month-to-month + tenure < 6 months | 23% | Very High |

**Insight:** Nearly **1 in 4 customers** are in the high-risk segment and need immediate attention.

---

## Actionable Recommendations

### Recommendation 1: Convert Month-to-Month to Annual
- **Action:** Offer "2 months free" for annual commitment
- **Target:** All month-to-month customers
- **Expected Impact:** Reduce churn by 15-20%

### Recommendation 2: Improve First 90-Day Experience
- **Action:** Automated onboarding emails + check-in calls
- **Schedule:** Days 1, 7, 30, 60, 90
- **Expected Impact:** Reduce early churn by 25%

### Recommendation 3: Incentivize Auto-Pay
- **Action:** $5/month discount for credit card/bank transfer
- **Target:** Electronic check users (35% churn rate)
- **Expected Impact:** Convert 30% of high-risk payment methods

### Recommendation 4: Early Warning System
- **Action:** Flag customers with tenure <6 months + monthly charges >$80
- **Trigger:** Automated retention offer - 20% discount for 3 months
- **Expected Impact:** Save 15-20% of at-risk customers

### Recommendation 5: Loyalty Rewards Program
- **Action:** Rewards at 12, 24, 36 month milestones
- **Benefits:** Free month, premium feature access, referral bonuses
- **Expected Impact:** Increase retention by 10% for long-term customers

---

## Expected Business Impact

| Recommendation | Expected Churn Reduction |
|----------------|-------------------------|
| Convert to annual contracts | 15-20% |
| Improve first 90 days | 25% |
| Auto-pay incentives | 30% conversion |
| Early warning system | 15-20% |
| Loyalty rewards | 10% |

**Combined Potential Impact:** **25-35% overall churn reduction**

---

## Conclusion

The data clearly shows that:
1. **Contract type** is the strongest predictor of churn
2. **First 6 months** are the most critical retention window
3. **Electronic check** users need immediate intervention
4. **Retained customers** have 2x higher lifetime value

Implementing these 5 recommendations could reduce churn by **25-35%** and increase customer lifetime value significantly.

---

**Report Date:** May 2026
**Analyst:** Zubenathi Mateza
**Task:** Future Interns - Data Science & Analytics Task 2
