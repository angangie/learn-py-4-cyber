"""
====================================================================
MODULE 3: CONDITIONAL STATEMENTS - Making Smart Decisions 🤔
====================================================================

Welcome to Module 3! Now that you can compare and evaluate data with operators,
you'll learn how to make your programs take different actions based on those
comparisons using conditional statements.

WHAT ARE CONDITIONAL STATEMENTS?
Conditional statements let your program make decisions. They work like this:
"IF this condition is true, THEN do this action, OTHERWISE do that action."

CONDITIONAL STATEMENTS WE'LL COVER:
- if: Execute code when a condition is True
- elif: Check additional conditions (else if)
- else: Execute code when all conditions are False
"""

# ============================================================================
# CONCEPT EXPLANATION: Basic IF Statements
# ============================================================================

# Simple if statement
failed_logins = 3
max_attempts = 5

print(f"Failed login attempts: {failed_logins}")
print(f"Maximum allowed attempts: {max_attempts}")

if failed_logins > max_attempts:
    print("🚨 ALERT: Account should be locked!")

# If statement that executes
failed_logins = 6  # Now it exceeds the limit

print(f"\nFailed login attempts: {failed_logins}") # Added newline for clarity
print(f"Maximum allowed attempts: {max_attempts}")

if failed_logins > max_attempts:
    print("🚨 ALERT: Account should be locked!")

# ============================================================================
# CONCEPT EXPLANATION: IF-ELSE Statements
# ============================================================================

# If-else provides an alternative action
firewall_status = True

print(f"\nFirewall enabled: {firewall_status}") # Added newline

if firewall_status:
    print("✅ Security status: Firewall protection active")
else:
    print("⚠️  Security status: Firewall protection disabled")

# Another if-else example
cpu_usage = 95
cpu_threshold = 90

print(f"\nCurrent CPU usage: {cpu_usage}%") # Added newline
print(f"CPU threshold: {cpu_threshold}%")

if cpu_usage > cpu_threshold:
    print("🔥 WARNING: High CPU usage detected!")
else:
    print("✅ CPU usage is within normal limits")

# ============================================================================
# CONCEPT EXPLANATION: IF-ELIF-ELSE Statements
# ============================================================================

# Multiple conditions with elif
threat_score = 7

print(f"\nCurrent threat score: {threat_score}/10") # Added newline

if threat_score >= 9:
    print("🚨 CRITICAL: Immediate action required!")
elif threat_score >= 7:
    print("⚠️  HIGH: Enhanced monitoring needed")
elif threat_score >= 5:
    print("🟡 MEDIUM: Standard monitoring")
elif threat_score >= 3:
    print("🟢 LOW: Minimal risk")
else:
    print("✅ SAFE: No significant threats")

# ============================================================================
# CONCEPT EXPLANATION: Complex Conditions
# ============================================================================

# Using logical operators in conditions
user_role = "admin"
authenticated = True
vpn_connected = False

print(f"\nUser role: {user_role}") # Added newline
print(f"Authenticated: {authenticated}")
print(f"VPN connected: {vpn_connected}")

if user_role == "admin" and authenticated:
    print("✅ Admin access granted")
    if not vpn_connected:
        print("⚠️  Warning: Admin not using VPN")
else:
    print("❌ Access denied")

# ============================================================================
# HOW THIS APPLIES TO CYBERSECURITY ADMINISTRATION:
# ============================================================================
"""
CYBERSECURITY APPLICATIONS OF CONDITIONAL STATEMENTS:

1. ACCESS CONTROL DECISIONS:
   - IF user is authenticated AND has proper role THEN grant access
   - IF login attempt from blacklisted IP THEN block immediately
   - IF password strength < minimum THEN require password change

2. INCIDENT RESPONSE AUTOMATION:
   - IF threat level == "CRITICAL" THEN trigger emergency response
   - IF malware detected THEN isolate system AND notify admin
   - IF unusual network activity THEN increase monitoring level

3. SYSTEM MONITORING:
   - IF CPU usage > 90% THEN send alert AND restart service
   - IF disk space < 10% THEN cleanup logs AND notify admin
   - IF service down THEN attempt restart ELSE escalate to admin

4. SECURITY POLICY ENFORCEMENT:
   - IF file extension in dangerous_list THEN quarantine file
   - IF user inactive > 30 days THEN disable account
   - IF unsuccessful logins > 5 THEN lock account for 30 minutes

5. VULNERABILITY MANAGEMENT:
   - IF patch level < required THEN schedule update
   - IF security scan finds high vulnerabilities THEN priority fix
   - IF system unpatched > 30 days THEN flag for immediate attention
"""

# Security access control example
user_ip = "203.0.113.42"
blacklisted_ips = ["203.0.113.42", "198.51.100.1"]
user_authenticated = True

print(f"\nUser IP: {user_ip}") # Added newline
print(f"User authenticated: {user_authenticated}")

if user_ip in blacklisted_ips:
    print("🚨 BLOCKED: IP address is blacklisted")
elif not user_authenticated:
    print("❌ DENIED: User not authenticated")
else:
    print("✅ ACCESS GRANTED: User cleared for entry")

# System health monitoring example
memory_usage = 85
disk_usage = 45
network_errors = 12

print("\nSystem Health Check:") # Added newline
print(f"Memory usage: {memory_usage}%")
print(f"Disk usage: {disk_usage}%")
print(f"Network errors: {network_errors}")

if memory_usage > 90:
    print("🔴 CRITICAL: Memory usage too high")
elif memory_usage > 80:
    print("🟡 WARNING: Memory usage elevated")
else:
    print("🟢 OK: Memory usage normal")

if disk_usage > 90:
    print("🔴 CRITICAL: Disk space critically low")
elif disk_usage > 75:
    print("🟡 WARNING: Disk space running low")
else:
    print("🟢 OK: Disk space sufficient")

# ============================================================================
# WARM-UP EXERCISES: Practice Using Conditionals
# ============================================================================

# Exercise 1: Simple if statement
"""
PRACTICE: Threat Level Assessment

In your security monitoring system, you're tracking a numerical threat level.
For this exercise, assume the current threat level is 8.
Your task is to write code that checks this threat level. If it's above 5,
your system should note "High threat detected". Otherwise, it should note "Low or normal threat".

(Store the result of this assessment in a global variable named `warmup1_output` for checking.)
"""
# TODO: Define a variable for the threat level (set to 8).
# TODO: Write an if-else statement to determine the threat message.
# TODO: Assign the determined message to the global variable `warmup1_output`.
# warmup1_output = "" # Initialize for testing

current_score= 8
if current_score > 5:
    print("High threat detected")
else:
    print("Low or normal threat")
warmup1_output = "High threat detected" #what does initialized for testing mean? 

# Exercise 2: If-else statement
"""
PRACTICE: Port Connection Type

Your system needs to identify the type of connection based on a port number.
Consider port number 22. If the connection is on port 22, it's an "SSH connection".
Any other port should be identified as "Other connection".

(Store the connection type string in a global variable named `warmup2_output`.)
"""
# TODO: Define a variable for the port number (set to 22).
# TODO: Use an if-else statement to identify the connection type.
# TODO: Assign the connection type to the global variable `warmup2_output`.
# warmup2_output = "" # Initialize for testing
port_number = 22
if port_number == 22: #need explanation on == again 
    print("SSH connection")
else:
    print("Other connection")
warmup2_output = "SSH connection"

# Exercise 3: Multiple conditions with elif
"""
PRACTICE: Security Score Evaluation

A system's security posture is rated with a score. For this scenario, the score is 7.
Evaluate this score:
- A score of 9 or higher is "Excellent security".
- A score between 7 and 8 (inclusive) is "Good security".
- Any other score "Needs improvement".

(Assign the evaluation string to the global variable `warmup3_output`.)
"""
# TODO: Define a variable for the security score (set to 7).
# TODO: Implement an if-elif-else structure to evaluate the score.
# TODO: Assign the evaluation message to the global variable `warmup3_output`.
# warmup3_output = "" # Initialize for testing
security_code = 7
if security_code>=9 :
    print:"Excellent security"
elif security_code>=7:
    print:"Good security"
else:
    print:"Needs improvement"
warmup3_output="Good security"  #why is this "good security"
# Exercise 4: Combining conditions with AND
"""
PRACTICE: System Readiness Check

For a system to be ready for critical operations, two conditions must be met:
an administrator must be logged in, AND the overall system health must be good.
Assume for this check that an admin is indeed logged in, and the system is healthy.
Determine if the system is "System ready for operations" or "System not ready".

(Store the readiness status in the global variable `warmup4_output`.)
"""
# TODO: Define two boolean variables: one for admin login status (True),
#       and one for system health (True).
# TODO: Write a conditional statement using 'and' to check if both are true.
# TODO: Assign the appropriate readiness message to `warmup4_output`.
# warmup4_output = "" # Initialize for testing


# ============================================================================
# YOUR MAIN EXERCISE: Build a Security Assessment System
# ============================================================================
"""
CHALLENGE: AUTOMATED SECURITY ASSESSMENT TOOL

Imagine you're building a tool to quickly assess a computer's security settings.
This tool will check several aspects of the system and report on each.

First, establish the current state of the system by defining these characteristics:
- The password for the main user account is 6 characters long.
- The system was last updated 45 days ago.
- The firewall is currently enabled.
- Antivirus software is not active.
- The primary administrator account is active.
- There have been 8 failed login attempts recently.

Based on these characteristics, your tool needs to generate specific assessment messages
for different security areas. The rules for these messages are as follows:

1.  PASSWORD SECURITY ASSESSMENT:
    How strong is the password?
    - If the password length is 12 characters or more, it's a "Strong password".
    - If it's between 8 and 11 characters (inclusive), it's an "Adequate password".
    - If it's shorter than 8 characters, it's a "Weak password, requires immediate change".
    (Store this assessment in `password_assessment_msg`.)

2.  SYSTEM UPDATE STATUS:
    Is the system up-to-date?
    - If the last update was 7 days ago or less, "System updates are current".
    - If it was between 8 and 30 days ago (inclusive of 30), "System updates are acceptable".
    - If it was more than 30 days ago, "System is critically outdated".
    (Store this status in `update_status_msg`.)

3.  SECURITY SOFTWARE PROTECTION:
    How well is the system protected by security software?
    - If both the firewall is enabled AND antivirus is active, "System is fully protected".
    - If either the firewall is enabled OR antivirus is active (but not both), "System is partially protected".
    - If neither is active, "System is unprotected".
    (Store this protection status in `software_protection_msg`.)

4.  ACCOUNT SECURITY MONITORING:
    What's the status of account login activity? (Evaluate these conditions in order)
    - If the admin account is active AND there have been more than 5 failed login attempts, it's an "Admin account under attack".
    - Else, if there have been more than 10 failed login attempts, it's a "Possible brute force attack".
    - Else, if there have been more than 3 failed login attempts, it's a "Multiple failed attempts warning".
    - Otherwise, it's "Normal login activity".
    (Store this activity status in `account_security_msg`.)

OPTIONAL CHALLENGE: OVERALL SECURITY RECOMMENDATION
    Based on the individual assessment messages you've generated, try to determine an
    overall security recommendation. For example:
    - If multiple areas are weak or critical, the recommendation might be "Urgent action required across multiple areas."
    - If most areas are good, "System posture is fair, address noted issues."
    - If all areas are strong, "System security posture is strong."
    This is an open-ended part for you to define your own logic.
    (Store your overall recommendation in `overall_recommendation_msg`.)

Your goal is to implement the logic to define the initial characteristics and then
determine each of these messages, storing them in their respective global variables for automated checking.
"""

# YOUR CODE GOES HERE
# ============================================================================

# PART 1: Define the system characteristic variables
# TODO: Define the 6 initial system characteristic variables
# password_length = 6
# ... and so on

# PART 2: Determine assessment messages and assign to global variables
# TODO: Implement conditional logic for each assessment area and assign to the respective `_msg` variables

# password_assessment_msg = "" # Initialize for testing
# update_status_msg = ""       # Initialize for testing
# software_protection_msg = "" # Initialize for testing
# account_security_msg = ""    # Initialize for testing

# (Optional Challenge)
# overall_recommendation_msg = "" # Initialize for testing


# ============================================================================
# BUILT-IN TESTS - Check Your Work!
# ============================================================================

print("\n" + "="*50)
print("RUNNING TESTS...")
print("="*50)

def test_warmup_exercises():
    """Test the warm-up exercises."""
    print("--- Testing Warm-up Exercises ---")
    passed_count = 0

    # Test Exercise 1
    try:
        # User is expected to define threat_level_warmup1 and warmup1_output
        # Simulating user code for testing:
        # threat_level_warmup1 = 8
        # if threat_level_warmup1 > 5: warmup1_output = "High threat detected"
        # else: warmup1_output = "Low or normal threat"
        assert warmup1_output == "High threat detected", "Warmup 1: threat_level = 8"

        # Test the other case (conceptually, user would change threat_level_warmup1 and rerun)
        # For testing, we assume the logic handles both.
        # A real student environment might require them to set up both test cases or we test their logic more directly.
        # For now, we'll assume the primary case (threat_level=8) is what they implement for the variable.
        print("✅ Warm-up 1 PASSED")
        passed_count += 1
    except NameError:
        print("❌ Warm-up 1 FAILED: `threat_level_warmup1` or `warmup1_output` not defined.")
    except AssertionError as e:
        print(f"❌ Warm-up 1 FAILED: {e}")

    # Test Exercise 2
    try:
        # port_warmup2 = 22
        # if port_warmup2 == 22: warmup2_output = "SSH connection"
        # else: warmup2_output = "Other connection"
        assert warmup2_output == "SSH connection", "Warmup 2: port = 22"
        print("✅ Warm-up 2 PASSED")
        passed_count += 1
    except NameError:
        print("❌ Warm-up 2 FAILED: `port_warmup2` or `warmup2_output` not defined.")
    except AssertionError as e:
        print(f"❌ Warm-up 2 FAILED: {e}")

    # Test Exercise 3
    try:
        # security_score_warmup3 = 7
        # if security_score_warmup3 >= 9: warmup3_output = "Excellent security"
        # elif security_score_warmup3 >= 7: warmup3_output = "Good security"
        # else: warmup3_output = "Needs improvement"
        assert warmup3_output == "Good security", "Warmup 3: score = 7"
        print("✅ Warm-up 3 PASSED")
        passed_count += 1
    except NameError:
        print("❌ Warm-up 3 FAILED: `security_score_warmup3` or `warmup3_output` not defined.")
    except AssertionError as e:
        print(f"❌ Warm-up 3 FAILED: {e}")

    # Test Exercise 4
    try:
        # admin_logged_in_warmup4 = True
        # system_healthy_warmup4 = True
        # if admin_logged_in_warmup4 and system_healthy_warmup4: warmup4_output = "System ready for operations"
        # else: warmup4_output = "System not ready"
        assert warmup4_output == "System ready for operations", "Warmup 4: True, True"
        print("✅ Warm-up 4 PASSED")
        passed_count += 1
    except NameError:
        print("❌ Warm-up 4 FAILED: Variables for warmup 4 or `warmup4_output` not defined.")
    except AssertionError as e:
        print(f"❌ Warm-up 4 FAILED: {e}")

    print(f"Warm-up Score: {passed_count}/4 exercises completed.")
    return passed_count == 4

def test_main_exercise():
    """Test the main exercise conditional logic."""
    print("\n--- Testing Main Exercise ---")
    main_passed = True

    expected_initial_vars = {
        "password_length": 6, "last_update_days": 45, "firewall_enabled": True,
        "antivirus_active": False, "admin_account_active": True, "failed_login_attempts": 8
    }
    for var_name, expected_value in expected_initial_vars.items():
        try:
            actual_value = globals()[var_name] # Check if defined by user
            assert actual_value == expected_value, f"Initial variable '{var_name}' has wrong value. Expected {expected_value}, got {actual_value}"
        except NameError:
            print(f"❌ Main Exercise FAILED: Initial variable '{var_name}' not defined.")
            main_passed = False
        except AssertionError as e:
            print(f"❌ Main Exercise FAILED: {e}")
            main_passed = False

    if not main_passed: return False # Stop if initial vars are wrong

    expected_messages = {
        "password_assessment_msg": "Weak password, requires immediate change",
        "update_status_msg": "System is critically outdated",
        "software_protection_msg": "System is partially protected",
        "account_security_msg": "Admin account under attack"
    }
    for var_name, expected_msg in expected_messages.items():
        try:
            actual_msg = globals()[var_name] # Check if defined by user
            assert actual_msg == expected_msg, f"Assessment message variable '{var_name}' incorrect. Expected '{expected_msg}', got '{actual_msg}'"
        except NameError:
            print(f"❌ Main Exercise FAILED: Result variable '{var_name}' not defined. Make sure to implement the logic and assign to this variable.")
            main_passed = False
        except AssertionError as e:
            print(f"❌ Main Exercise FAILED: {e}")
            main_passed = False

    if main_passed:
        print("✅ Main Exercise: All required message variables correctly assigned!")
    else:
        print("❌ Main Exercise: Some message variables incorrect or not defined.")
    return main_passed

def run_all_tests(): # Renamed from test_conditionals
    """Run all tests for Module 3."""
    warmup_success = test_warmup_exercises()
    main_success = test_main_exercise()

    if warmup_success and main_success:
        print("\n✅ CONGRATULATIONS! All tests passed!")
        print("You've successfully mastered Python conditional statements!")
        print("Ready for Module 4: Lists") # Updated from Loops to Lists
    else:
        print("\n📚 Keep practicing! Complete all exercises to proceed.")
        if not warmup_success:
            print("- Review warm-up exercises.")
        if not main_success:
            print("- Review main security assessment exercise.")

# Run the tests
run_all_tests() # Updated call

# ============================================================================
# WHAT'S NEXT?
# ============================================================================
"""
Outstanding work completing Module 3! Here's what you learned:

✅ Basic if statements for simple decisions
✅ If-else statements for two-option decisions
✅ If-elif-else for multiple condition checking
✅ Complex conditions using logical operators
✅ How to build automated security assessment logic

CYBERSECURITY SKILLS GAINED:
- Automated security policy enforcement
- Intelligent threat response decisions
- System health monitoring with smart alerts
- Access control logic implementation
- Incident response automation basics

NEXT MODULE: 04_lists.py
In the next module, you'll dive deep into lists - the versatile containers
that allow you to manage collections of security data like IP addresses,
user accounts, security alerts, and much more!

You're building serious cybersecurity automation skills! 🛡️
"""
