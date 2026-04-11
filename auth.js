const CLIENT_ID    = "ebanh1c48g1u5bu68r7j3sk3q";
const DOMAIN       = "https://ap-south-1v3aek6txo.auth.ap-south-1.amazoncognito.com";
const REDIRECT_URI = "https://dwp4zgmgeaeup.cloudfront.net/callback.html";
const LOGOUT_URI   = "https://dwp4zgmgeaeup.cloudfront.net";

// Step 1: Redirect to Cognito login (Authorization Code Flow)
function login() {
    const loginUrl = `${DOMAIN}/login?client_id=${CLIENT_ID}&response_type=code&scope=email+openid+phone&redirect_uri=${encodeURIComponent(REDIRECT_URI)}`;
    window.location.href = loginUrl;
}

// Step 2: Get authorization code from URL
function getCodeFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get("code");
}

// Step 3: Exchange authorization code for ID token
async function exchangeCodeForToken(code) {
    const tokenUrl = `${DOMAIN}/oauth2/token`;

    const body = new URLSearchParams({
        grant_type:   "authorization_code",
        client_id:    CLIENT_ID,
        code:         code,
        redirect_uri: REDIRECT_URI
    });

    const res = await fetch(tokenUrl, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body
    });

    const data = await res.json();

    if (!data.id_token) throw new Error("No id_token in response");

    return data.id_token;
}

// Step 4: Store / retrieve token
function saveToken(token) {
    sessionStorage.setItem("auth_token", token);
}

function getToken() {
    return sessionStorage.getItem("auth_token");
}

function isLoggedIn() {
    return !!getToken();
}

// Step 5: Guard pages — redirect to login if not authenticated
function requireLogin() {
    if (!isLoggedIn()) {
        login();
    }
}

// Step 6: Handle OAuth callback
async function handleCallback() {
    const code = getCodeFromUrl();

    if (code) {
        try {
            const token = await exchangeCodeForToken(code);
            saveToken(token);
            window.history.replaceState({}, document.title, "/callback.html");
            window.location.href = "index.html";
        } catch (err) {
            console.error("Token exchange failed", err);
            window.location.href = "error.html";
        }
    } else {
        window.location.href = "error.html";
    }
}

// Logout: clear session and redirect to Cognito logout
function logout() {
    sessionStorage.removeItem("auth_token");
    const logoutUrl = `${DOMAIN}/logout?client_id=${CLIENT_ID}&logout_uri=${encodeURIComponent(LOGOUT_URI)}`;
    window.location.href = logoutUrl;
}

// Adds a logout button fixed to top-right corner of any page
function addLogoutButton() {
    const btn = document.createElement("button");
    btn.innerText = "Logout";
    btn.className = "action-btn";

    // Fixed position so it stays visible when scrolling (was: absolute)
    btn.style.position = "fixed";
    btn.style.top      = "20px";
    btn.style.right    = "20px";
    btn.style.zIndex   = "1000";

    btn.onclick = logout;
    document.body.appendChild(btn);
}