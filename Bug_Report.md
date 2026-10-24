
# Swag Labs - Bug Report

**Environment:** Google Chrome (Desktop)
**User Account Tested:** problem_user

### Bug 1: Product Images Fail to Load
* **Description:** All product images on the inventory page are incorrectly replaced by the identical image of a dog.
* **Steps to Reproduce:** Log in with `problem_user` -> Observe the inventory page.
* **Severity:** High.

### Bug 2: "Remove" Button Broken
* **Description:** The "Remove" button does not work for items on the inventory page after being added to the cart. 
* **Steps to Reproduce:** Log in as `problem_user` -> Click "Add to cart" -> Click "Remove". 
* **Severity:** Medium.

### Bug 3: Sorting Dropdown is Non-Functional
* **Description:** Selecting any option from the product sort dropdown does not reorder the products.
* **Severity:** Medium.

### Bug 4: Checkout Form "Last Name" Error
* **Description:** During checkout, typing into the "Last Name" field throws an immediate error.
* **Steps to Reproduce:** Add item to cart -> Go to Checkout -> Type into Last Name field.
* **Severity:** Critical. Blocker for checkout.
