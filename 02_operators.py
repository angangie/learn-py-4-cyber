"""
====================================================================
MODULE 2: OPERATORS - Making Comparisons and Decisions 🔍
====================================================================

Welcome to Module 2! Now that you know how to store data in variables,
you'll learn how to work with that data using operators.

WHAT ARE OPERATORS?
Operators are symbols that perform operations on variables and values.
Think of them as the "action words" of programming - they let you compare,
calculate, and make logical decisions.

TYPES OF OPERATORS WE'LL COVER:
- Arithmetic: +, -, *, / (math operations)
- Comparison: ==, !=, <, >, <=, >= (comparing values)
- Logical: and, or, not (combining conditions)
"""

# ============================================================================
# CONCEPT EXPLANATION: Arithmetic Operators
# ============================================================================

# Basic math operations
failed_attempts = 5
max_attempts = 10
remaining_attempts = max_attempts - failed_attempts

# More arithmetic examples
total_users = 100
admin_users = 5
regular_users = total_users - admin_users
admin_percentage = (admin_users / total_users) * 100

# ============================================================================
# CONCEPT EXPLANATION: Comparison Operators
# ============================================================================

# Comparison operators return True or False
current_cpu = 85
cpu_threshold = 80

print("Comparison Examples:")
print(f"CPU usage == threshold: {current_cpu == cpu_threshold}")
print(f"CPU usage != threshold: {current_cpu != cpu_threshold}")
print(f"CPU usage > threshold: {current_cpu > cpu_threshold}")
print(f"CPU usage < threshold: {current_cpu < cpu_threshold}")
print(f"CPU usage >= threshold: {current_cpu >= cpu_threshold}")
print(f"CPU usage <= threshold: {current_cpu <= cpu_threshold}")
print()

# ============================================================================
# CONCEPT EXPLANATION: Logical Operators
# ============================================================================

# Logical operators combine conditions
firewall_on = True
antivirus_on = True
updates_current = False

# Using 'and' - both conditions must be True
system_secure = firewall_on and antivirus_on

# Using 'or' - at least one condition must be True
some_protection = firewall_on or antivirus_on

# Using 'not' - reverses True/False
updates_needed = not updates_current

# Complex logical combinations
fully_secure = firewall_on and antivirus_on and updates_current

# ============================================================================
# HOW THIS APPLIES TO CYBERSECURITY ADMINISTRATION:
# ============================================================================
"""
CYBERSECURITY APPLICATIONS OF OPERATORS:

1. THRESHOLD MONITORING:
   - Check if CPU usage > 90% (performance monitoring)
   - Verify if failed logins >= 5 (brute force detection)
   - Monitor if network traffic != normal (anomaly detection)

2. SECURITY VALIDATION:
   - Password length >= 8 characters
   - Port number == 443 for secure connections
   - User role != "guest" for admin functions

3. LOGICAL SECURITY DECISIONS:
   - Allow access IF (user authenticated AND permissions granted)
   - Trigger alert IF (intrusion detected OR suspicious activity)
   - Block connection IF NOT (IP whitelisted)

4. SYSTEM STATUS CHECKS:
   - Services running AND patches updated AND firewall enabled
   - Backup completed OR manual backup scheduled
   - NOT vulnerable AND security score > 8.0

5. INCIDENT RESPONSE:
   - Severity == "HIGH" triggers immediate response
   - Multiple failed attempts AND from external IP
   - System compromised OR data breach detected
"""

# Security threshold checks
failed_logins = 7
max_failed_logins = 5
account_locked = failed_logins >= max_failed_logins

# Security status evaluation
patch_level = 95
min_patch_level = 90
firewall_active = True
antivirus_updated = True

patches_current = patch_level >= min_patch_level
security_good = patches_current and firewall_active and antivirus_updated

# ============================================================================
# WARM-UP EXERCISES: Practice Using Operators
# ============================================================================

# Exercise 1: Basic comparison
"""
PRACTICE: Simple Comparison

Create variables cpu_usage = 85 and cpu_limit = 90.
Check if cpu_usage is greater than cpu_limit and store the result in high_cpu.
"""
# TODO: Create variables and comparison
cpu_limit = 90
cpu_usage = 85
high_cpu = cpu_usage > cpu_limit


# Exercise 2: Basic math operations
"""
PRACTICE: Arithmetic Operations

Create variables users_online = 50 and new_users = 25.
Calculate total_users by adding them together.
"""
# TODO: Create variables and calculate total
users_online = 50 
new_users = 25
total_users = users_online + new_users


# Exercise 3: Boolean logic with AND
"""
PRACTICE: AND Logic

Create variables firewall_on = True and antivirus_on = True.
Check if BOTH are True and store in system_protected.
"""
# TODO: Create variables and use AND logic
firewall_active = True
antivirus_on = True
system_protected = firewall_active and antivirus_on
print(system_protected)


# Exercise 4: Boolean logic with OR
"""
PRACTICE: OR Logic

Create variables critical_alert = False and warning_alert = True.
Check if EITHER is True and store in any_alert.
"""
# TODO: Create variables and use OR logic
critical_alert = False
warning_alert = True
any_alert = critical_alert or warning_alert
print(any_alert)

# ============================================================================
# YOUR MAIN EXERCISE: Create Security Monitoring Logic
# ============================================================================
"""
NETWORK SECURITY CONDITION ANALYZER

You are monitoring a corporate network and need to analyze current security conditions 
to determine if any alerts should be triggered.

Current network status:
- Active connections: 150
- Maximum allowed connections: 100
- Administrator is currently online: Yes
- System is in maintenance mode: No
- Current threat level: 7 (on a scale of 1-10)
- Safe threat threshold: 5

Your system needs to evaluate several security conditions:

1. Determine if the network is experiencing a connection overload
   (when current connections exceed the maximum allowed)

2. Assess if the threat level is high 
   (when threat level exceeds the safe threshold)

3. Check if the system is ready for normal operations
   (when administrator is online AND system is not in maintenance mode)

4. Determine if a security alert should be triggered
   (when there is either a connection overload OR high threat level)

5. Evaluate if it's safe to operate
   (when system is ready AND no security alert is active)

Store these evaluations in variables named connection_overload, threat_high, 
system_ready, security_alert, and safe_to_operate. Also create variables for 
the network status data using names current_connections, max_connections, 
admin_online, maintenance_mode, threat_level, and safe_threshold.
"""

# YOUR CODE GOES HERE
# ============================================================================

# PART 1: Create the required variables

# TODO: Create the 6 variables listed above
# Create current_connections variable here
current_connections = 150
# Create max_connections variable here
max_connections = 100
# Create admin_online variable here
admin_online = True
# Create maintenance_mode variable here
maintenance_mode = False
# Create threat_level variable here
threat_level = 7
# Create safe_threshold variable here
safe_threshold = 5

# PART 2: Calculate security conditions using operators
# TODO: Create the 5 calculated variables using operators
# Create connection_overload variable here
connection_overload = current_connections > max_connections
# Create threat_high variable here
threat_high = threat_level > safe_threshold
# Create system_ready variable here
system_ready = admin_online and not maintenance_mode
# Create security_alert variable here
security_alert = connection_overload or threat_high
# Create safe_to_operate variable here
safe_to_operate = system_ready and not security_alert


# ============================================================================
# BUILT-IN TESTS - Check Your Work!
# ============================================================================

print("\n" + "="*50)
print("RUNNING TESTS...")
print("="*50)

def test_warmup_exercises():
    """Test the warm-up exercises."""
    print("=== TESTING WARM-UP EXERCISES ===")
    warmup_passed = 0
    
    # Test Exercise 1: Simple comparison
    try:
        assert cpu_usage == 85, f"Variable 'cpu_usage' should be 85, got: {cpu_usage}"
        assert cpu_limit == 90, f"Variable 'cpu_limit' should be 90, got: {cpu_limit}"
        assert high_cpu == False, f"Variable 'high_cpu' should be False (85 > 90 is False), got: {high_cpu}"
        print("✅ Exercise 1 PASSED: comparison logic correct")
        warmup_passed += 1
    except NameError as e:
        print(f"❌ Exercise 1 FAILED: Missing variable - {e}")
        print("Create variables: cpu_usage=85, cpu_limit=90, high_cpu=(cpu_usage > cpu_limit)")
    except AssertionError as e:
        print(f"❌ Exercise 1 FAILED: {e}")
    
    # Test Exercise 2: Arithmetic operations
    try:
        assert users_online == 50, f"Variable 'users_online' should be 50, got: {users_online}"
        assert new_users == 25, f"Variable 'new_users' should be 25, got: {new_users}"
        assert total_users == 75, f"Variable 'total_users' should be 75 (50 + 25), got: {total_users}"
        print("✅ Exercise 2 PASSED: arithmetic calculation correct")
        warmup_passed += 1
    except NameError as e:
        print(f"❌ Exercise 2 FAILED: Missing variable - {e}")
        print("Create variables: users_online=50, new_users=25, total_users=(users_online + new_users)")
    except AssertionError as e:
        print(f"❌ Exercise 2 FAILED: {e}")
    
    # Test Exercise 3: AND logic
    try:
        assert firewall_on == True, f"Variable 'firewall_on' should be True, got: {firewall_on}"
        assert antivirus_on == True, f"Variable 'antivirus_on' should be True, got: {antivirus_on}"
        assert system_protected == True, f"Variable 'system_protected' should be True (True and True), got: {system_protected}"
        print("✅ Exercise 3 PASSED: AND logic correct")
        warmup_passed += 1
    except NameError as e:
        print(f"❌ Exercise 3 FAILED: Missing variable - {e}")
        print("Create variables: firewall_on=True, antivirus_on=True, system_protected=(firewall_on and antivirus_on)")
    except AssertionError as e:
        print(f"❌ Exercise 3 FAILED: {e}")
    
    # Test Exercise 4: OR logic
    try:
        assert critical_alert == False, f"Variable 'critical_alert' should be False, got: {critical_alert}"
        assert warning_alert == True, f"Variable 'warning_alert' should be True, got: {warning_alert}"
        assert any_alert == True, f"Variable 'any_alert' should be True (False or True), got: {any_alert}"
        print("✅ Exercise 4 PASSED: OR logic correct")
        warmup_passed += 1
    except NameError as e:
        print(f"❌ Exercise 4 FAILED: Missing variable - {e}")
        print("Create variables: critical_alert=False, warning_alert=True, any_alert=(critical_alert or warning_alert)")
    except AssertionError as e:
        print(f"❌ Exercise 4 FAILED: {e}")
    
    print(f"Warm-up Score: {warmup_passed}/4 exercises completed")
    return warmup_passed == 4

def test_main_exercise():
    """Test the main exercise calculations."""
    print("\n=== TESTING MAIN EXERCISE ===")
    
    try:
        # Test network status variables
        assert current_connections == 150, f"Variable 'current_connections' should be 150, got: {current_connections}"
        print("✅ current_connections: Correct")
        
        assert max_connections == 100, f"Variable 'max_connections' should be 100, got: {max_connections}"
        print("✅ max_connections: Correct")
        
        assert admin_online == True, f"Variable 'admin_online' should be True, got: {admin_online}"
        print("✅ admin_online: Correct")
        
        assert maintenance_mode == False, f"Variable 'maintenance_mode' should be False, got: {maintenance_mode}"
        print("✅ maintenance_mode: Correct")
        
        assert threat_level == 7, f"Variable 'threat_level' should be 7, got: {threat_level}"
        print("✅ threat_level: Correct")
        
        assert safe_threshold == 5, f"Variable 'safe_threshold' should be 5, got: {safe_threshold}"
        print("✅ safe_threshold: Correct")
        
        # Test calculated conditions
        assert connection_overload == True, f"Variable 'connection_overload' should be True (150 > 100), got: {connection_overload}"
        print("✅ connection_overload: Correct calculation")
        
        assert threat_high == True, f"Variable 'threat_high' should be True (7 > 5), got: {threat_high}"
        print("✅ threat_high: Correct calculation")
        
        assert system_ready == True, f"Variable 'system_ready' should be True (admin_online AND not maintenance_mode), got: {system_ready}"
        print("✅ system_ready: Correct calculation")
        
        assert security_alert == True, f"Variable 'security_alert' should be True (connection_overload OR threat_high), got: {security_alert}"
        print("✅ security_alert: Correct calculation")
        
        assert safe_to_operate == False, f"Variable 'safe_to_operate' should be False (system_ready AND not security_alert), got: {safe_to_operate}"
        print("✅ safe_to_operate: Correct calculation")
        
        print("\n✅ MAIN EXERCISE COMPLETED! All calculations correct!")
        return True
        
    except NameError as e:
        print(f"❌ ERROR: Variable not found - {e}")
        print("Make sure you've created all required variables above the test section.")
        return False
    except AssertionError as e:
        print(f"❌ ERROR: {e}")
        print("Check your calculations and try again.")
        return False
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        return False

def test_operators():
    """Run all tests for Module 2."""
    warmup_success = test_warmup_exercises()
    main_success = test_main_exercise()
    
    if warmup_success and main_success:
        print("\n✅ CONGRATULATIONS! All tests passed!")
        print("You've successfully mastered Python operators!")
        print("Ready for Module 3: Conditional Statements")
    else:
        print("\n📚 Keep practicing! Complete all exercises to proceed.")
        if not warmup_success:
            print("- Finish the warm-up exercises first")
        if not main_success:
            print("- Complete the main network security analysis exercise")

# Run the tests
test_operators()

# ============================================================================
# WHAT'S NEXT?
# ============================================================================
"""
Excellent work completing Module 2! Here's what you learned:

✅ Arithmetic operators for calculations (+, -, *, /)
✅ Comparison operators for evaluating conditions (==, !=, <, >, <=, >=)
✅ Logical operators for combining conditions (and, or, not)
✅ How to create complex security logic using operators

CYBERSECURITY SKILLS GAINED:
- Monitor system thresholds and limits
- Evaluate security conditions automatically
- Create logical decision-making in scripts
- Build foundation for automated security responses

NEXT MODULE: 03_conditionals.py
In the next module, you'll learn conditional statements (if, elif, else) -
the building blocks that let your programs make intelligent decisions based
on the conditions you've learned to evaluate!

Keep building your cybersecurity programming skills! 🔐
"""
