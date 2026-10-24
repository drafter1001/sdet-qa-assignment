
# Swag Labs - QA Test Plan

## 1. Scope
**In-Scope:**
* User Authentication (Login logic, error handling).
* Product Catalog (Image rendering, sorting).
* Shopping Cart (Adding/removing items).
* Checkout Workflow (Form validation).

## 2. Types of Testing
* **Functional Testing:** Verifying core user flows (login, checkout).
* **UI Testing:** Ensuring elements render correctly.
* **Negative Testing:** Invalid credentials or empty checkout fields.

## 3. Test Cases
1. **TC01:** Verify a standard user can successfully log in.
2. **TC02:** Verify a locked-out user receives the exact error message.
3. **TC03:** Verify a user can add an item to the cart and the badge updates.
4. **TC04:** Verify a user can successfully complete checkout.
5. **TC05:** Verify the sorting dropdown correctly sorts items.
