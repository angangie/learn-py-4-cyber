"""
====================================================================
MODULE 1: VARIABLES & DATA TYPES - Your First Steps in Python! 🐍
====================================================================

Welcome to your first Python module! In this lesson, you'll learn about
variables and data types - the building blocks of all programming.

WHAT ARE VARIABLES?
Variables are like labeled containers that store information. Think of them
as boxes with names on them - you can put different things in each box
and access them later by their name.

PYTHON DATA TYPES WE'LL COVER:
- str (string): Text data like "Hello" or "192.168.1.1"
- int (integer): Whole numbers like 22, 80, 443
- float (decimal): Numbers with decimal points like 3.14, 99.9
- bool (boolean): True or False values
"""

# ============================================================================
# CONCEPT EXPLANATION: Variables and Data Types
# ============================================================================

# STRING EXAMPLES - Text data (always in quotes)
username = "admin"
ip_address = "192.168.1.100"
log_message = "Login successful"

# INTEGER EXAMPLES - Whole numbers (no quotes needed)
port_number = 443
failed_attempts = 5
max_connections = 100

# FLOAT EXAMPLES - Decimal numbers
cpu_usage = 87.5
network_latency = 0.025
security_score = 8.7

# BOOLEAN EXAMPLES - True or False values
firewall_enabled = True
intrusion_detected = False
admin_logged_in = True

# ============================================================================
# HOW THIS APPLIES TO CYBERSECURITY ADMINISTRATION:
# ============================================================================
"""
CYBERSECURITY APPLICATIONS OF VARIABLES:

1. STORING NETWORK INFORMATION:
   - IP addresses, port numbers, network ranges
   - Server names, domain names, MAC addresses

2. TRACKING SECURITY EVENTS:
   - Login attempts, failed passwords, access times
   - Alert levels, threat scores, vulnerability counts

3. CONFIGURATION MANAGEMENT:
   - Security settings, timeout values, thresholds
   - Enable/disable flags for security features

4. LOG ANALYSIS:
   - Error messages, event descriptions, timestamps
   - User actions, system responses, alert notifications

5. AUTOMATION SCRIPTS:
   - Status indicators, process counters, success flags
   - File paths, command parameters, script results

REAL-WORLD EXAMPLE:
A cybersecurity admin might use variables to store:
- current_threat_level = "HIGH"
- suspicious_ip = "203.0.113.42"
- ports_to_scan = [21, 22, 23, 25, 53, 80, 443]
- scan_complete = False
"""

# Network Security Variables
suspicious_ip = "203.0.113.42"
blocked_ports = 1337
threat_level = "MEDIUM"
firewall_active = True

# ============================================================================
# WARM-UP EXERCISES: Practice Creating Variables
# ============================================================================

# Exercise 1: Create a simple string variable
"""
PRACTICE: Basic String Variable

Create a variable named username1 that stores the text "admin".
"""
# TODO: Create username1 variable
username1= "admin"

# Exercise 2: Create a number variable  
"""
PRACTICE: Basic Number Variable

Create a variable named port that stores the number 443.
"""
# TODO: Create port variable
port = 443

# Exercise 3: Create a boolean variable
"""
PRACTICE: Basic Boolean Variable

Create a variable named is_secure that stores True.
"""
# TODO: Create is_secure variable
is_secure= True

# Exercise 4: Create multiple variables
"""
PRACTICE: Multiple Variables

Create these three variables:
- server_name with value "firewall"
- connections with value 25
- online with value True
"""
# TODO: Create the three variables
server_name= "firewall"
connections= 25
online= True

# ============================================================================
# YOUR MAIN EXERCISE: Create Cybersecurity Variables
# ============================================================================
"""
CYBERSECURITY MONITORING SYSTEM SETUP

You are a cybersecurity administrator setting up a new monitoring system for your organization. 
The system needs to track various pieces of critical infrastructure information.

Your task is to create a data storage system that can hold the following information:
- The username of the primary security administrator: "secladmin"
- The IP address of the main server: "10.0.0.50"
- The SSH port number used for secure connections: 22
- The number of failed login attempts currently recorded: 3
- The system uptime measured in hours: 72.5
- Whether a security patch is required: Yes
- Whether the backup process has completed: No

Create variables named admin_username, server_ip, ssh_port, login_attempts, 
uptime_hours, patch_required, and backup_completed to store this information.

After storing the data, display each piece of information with a descriptive 
label so other administrators can quickly review the system status.
"""

# YOUR CODE GOES HERE - Create the 7 variables described above
# ============================================================================

# TODO: Create your variables here
# Create admin_username variable here
admin_username  = "secladmin"

# Create server_ip variable here
server_ip = "10.0.0.50"

# Create ssh_port variable here
ssh_port =  22
# Create login_attempts variable here
login_attempts = 3
# Create uptime_hours variable here
uptime_hours = 72.5
# Create patch_required variable here
patch_required = True
# Create backup_completed variable here
backup_completed = False

# ============================================================================
# BUILT-IN TESTS - Check Your Work! 
# ============================================================================
"""
The tests below will check if you created your variables correctly.
If all tests pass, you'll see "All tests passed!" at the end.
If a test fails, you'll see an error message explaining what went wrong.
"""

print("\n" + "="*50)
print("RUNNING TESTS...")
print("="*50)

def test_warmup_exercises():
    """Test the warm-up exercises."""
    print("=== TESTING WARM-UP EXERCISES ===")
    warmup_passed = 0
    
    # Test Exercise 1: username variable
    try:
        assert username1 == "admin", f"Variable 'username1' should be 'admin', got: {username1}"
        print("✅ Exercise 1 PASSED: username1 variable created correctly")
        warmup_passed += 1
    except NameError:
        print("❌ Exercise 1 FAILED: Create variable named 'username1' with value 'admin'")
    except AssertionError as e:
        print(f"❌ Exercise 1 FAILED: {e}")
    
    # Test Exercise 2: port variable
    try:
        assert port == 443, f"Variable 'port' should be 443, got: {port}"
        print("✅ Exercise 2 PASSED: port variable created correctly")
        warmup_passed += 1
    except NameError:
        print("❌ Exercise 2 FAILED: Create variable named 'port' with value 443")
    except AssertionError as e:
        print(f"❌ Exercise 2 FAILED: {e}")
    
    # Test Exercise 3: is_secure variable
    try:
        assert is_secure == True, f"Variable 'is_secure' should be True, got: {is_secure}"
        print("✅ Exercise 3 PASSED: is_secure variable created correctly")
        warmup_passed += 1
    except NameError:
        print("❌ Exercise 3 FAILED: Create variable named 'is_secure' with value True")
    except AssertionError as e:
        print(f"❌ Exercise 3 FAILED: {e}")
    
    # Test Exercise 4: multiple variables
    try:
        assert server_name == "firewall", f"Variable 'server_name' should be 'firewall', got: {server_name}"
        assert connections == 25, f"Variable 'connections' should be 25, got: {connections}"
        assert online == True, f"Variable 'online' should be True, got: {online}"
        print("✅ Exercise 4 PASSED: All three variables created correctly")
        warmup_passed += 1
    except NameError as e:
        print(f"❌ Exercise 4 FAILED: Missing variable - {e}")
        print("Create variables: server_name='firewall', connections=25, online=True")
    except AssertionError as e:
        print(f"❌ Exercise 4 FAILED: {e}")
    
    print(f"Warm-up Score: {warmup_passed}/4 exercises completed")
    return warmup_passed == 4

def test_main_exercise():
    """Test the main exercise variables."""
    print("\n=== TESTING MAIN EXERCISE ===")
    
    try:
        # Test admin_username
        assert admin_username == "secladmin", f"Variable 'admin_username' should be 'secladmin', got: {admin_username}"
        print("✅ admin_username: Correct")
        
        # Test server_ip
        assert server_ip == "10.0.0.50", f"Variable 'server_ip' should be '10.0.0.50', got: {server_ip}"
        print("✅ server_ip: Correct")
        
        # Test ssh_port
        assert ssh_port == 22, f"Variable 'ssh_port' should be 22, got: {ssh_port}"
        print("✅ ssh_port: Correct")
        
        # Test login_attempts
        assert login_attempts == 3, f"Variable 'login_attempts' should be 3, got: {login_attempts}"
        print("✅ login_attempts: Correct")
        
        # Test uptime_hours
        assert uptime_hours == 72.5, f"Variable 'uptime_hours' should be 72.5, got: {uptime_hours}"
        print("✅ uptime_hours: Correct")
        
        # Test patch_required
        assert patch_required == True, f"Variable 'patch_required' should be True, got: {patch_required}"
        print("✅ patch_required: Correct")
        
        # Test backup_completed
        assert backup_completed == False, f"Variable 'backup_completed' should be False, got: {backup_completed}"
        print("✅ backup_completed: Correct")
        
        # Test data types
        assert isinstance(admin_username, str), "admin_username should be a string"
        assert isinstance(server_ip, str), "server_ip should be a string"
        assert isinstance(ssh_port, int), "ssh_port should be an integer"
        assert isinstance(login_attempts, int), "login_attempts should be an integer"
        assert isinstance(uptime_hours, float), "uptime_hours should be a float"
        assert isinstance(patch_required, bool), "patch_required should be a boolean"
        assert isinstance(backup_completed, bool), "backup_completed should be a boolean"
        print("✅ All data types are correct")
        
        print("\n✅ MAIN EXERCISE COMPLETED! All variables created correctly!")
        return True
        
    except NameError as e:
        print(f"❌ ERROR: Variable not found - {e}: Make sure you've created all required variables above the test section.")
        return False
    except AssertionError as e:
        print(f"❌ ERROR: {e}: Check the values you assigned to your variables.")
        return False
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        return False

def test_variables():
    """Run all tests for Module 1."""
    warmup_success = test_warmup_exercises()
    main_success = test_main_exercise()
    
    if warmup_success and main_success:
        print("\n✅ All tests passed! You've mastered Python variables and data types! Proceed to Module 2: Operators")
    else:
        resultsDisplay = "\n📚 Keep practicing! Complete all exercises to proceed."
        
        if not warmup_success:
            resultsDisplay+= " Finish the warm-up exercises first."
        if not main_success:
            resultsDisplay+= " Complete the main cybersecurity monitoring exercise."
        print(resultsDisplay)

# Run the tests
test_variables()

# ============================================================================
# WHAT'S NEXT?
# ============================================================================
"""
Great job completing Module 1! Here's what you learned:

✅ How to create variables in Python
✅ The four main data types: str, int, float, bool
✅ How variables apply to cybersecurity work
✅ Basic variable naming and assignment

CYBERSECURITY SKILLS GAINED:
- Store network configuration data
- Track security metrics and status
- Manage user and system information
- Create foundation for security automation

NEXT MODULE: 02_operators.py
In the next module, you'll learn about operators - the tools that let you
compare data, perform calculations, and make logical decisions in your
cybersecurity scripts.

Keep up the excellent work! 🚀
"""
