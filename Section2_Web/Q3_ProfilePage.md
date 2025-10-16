# Question 3: Profile Page with API

## Approach

Created a simple profile page that:
1. **Fetches** user data from JSONPlaceholder API
2. **Displays** name and email (plus additional fields)
3. **Handles** loading and error states

## Implementation Details

### Fetching Data
```javascript
async function fetchUserData() {
    const response = await fetch(API_URL);
    const user = await response.json();
}
```

### Loading State
- Shows spinner animation
- Displays "Loading user data..." message

### Error Handling
- Catches fetch errors (network issues, 404, 500, etc.)
- Displays error message with "Try Again" button
- Checks `response.ok` for HTTP errors

### Success State
- Displays user name, email, and other details
- Styled card with gradient background

## Technologies Used
- **Plain JavaScript** (async/await)
- **Fetch API** for HTTP requests
- **CSS** for styling and animations

## Code
See `Q3_ProfilePage.html`
