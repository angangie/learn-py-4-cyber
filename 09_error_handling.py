"""
====================================================================
MODULE 9: ERROR HANDLING - Building Robust Security Tools 🛡️
====================================================================

Welcome to the final module! You've learned all the core Python concepts.
Now you'll master error handling - the critical skill that makes your
cybersecurity tools robust, reliable, and ready for real-world deployment.

WHAT IS ERROR HANDLING?
Error handling lets your programs gracefully manage unexpected situations:
network failures, missing files, invalid data, or system errors. In
cybersecurity, robust error handling is essential because your tools must
work reliably even when systems are under attack or compromised.

ERROR HANDLING CONCEPTS WE'LL COVER:
- Understanding different types of errors
- try/except blocks for catching errors
- Multiple exception types and specific handling
- finally blocks for cleanup operations
- Custom exceptions for security scenarios
- Best practices for robust cybersecurity tools
"""
import datetime
import random # For network simulation
import os # For file operations in tests

# ============================================================================
# WARM-UP EXERCISES: Practice Error Handling
# ============================================================================

# Exercise 1: Basic try-except
"""
PRACTICE: Simple Try-Except

Write a function `safe_convert_to_int(value_str)` that attempts to convert
`value_str` to an integer.
If successful, return the integer.
If a ValueError occurs (e.g., `value_str` is "abc"), return the string "Invalid number".
"""
# TODO: Implement safe_convert_to_int
def safe_convert_to_int(value_str):
    pass


# Exercise 2: Handle file not found
"""
PRACTICE: File Error Handling

Write a function `read_config_file_warmup(filename)` that attempts to open
and read the content of `filename`.
If successful, return the content.
If a FileNotFoundError occurs, return the string "File not found".
"""
# TODO: Implement read_config_file_warmup
def read_config_file_warmup(filename):
    pass


# Exercise 3: Multiple exception types
"""
PRACTICE: Multiple Exception Handling

Write a function `safe_divide_warmup(a, b)` that attempts to return `a / b`.
Handle ZeroDivisionError by returning "Cannot divide by zero".
Handle TypeError (e.g., if a or b are not numbers) by returning "Invalid input types".
For any other exception, return "An unexpected error occurred".
"""
# TODO: Implement safe_divide_warmup
def safe_divide_warmup(a,b):
    pass


# Exercise 4: Try-except-finally
"""
PRACTICE: Finally Block

Write a function `process_file_with_cleanup_warmup(filename)` that attempts to open
`filename` for reading and returns its content.
Regardless of success or failure (FileNotFoundError or other exceptions),
the function should also create/overwrite a file named "cleanup_log.txt"
with the message "File operation completed for [filename]".
If reading is successful, return file content. If an error occurs during read, return None.
The cleanup action (writing to "cleanup_log.txt") must always be attempted.
"""
# TODO: Implement process_file_with_cleanup_warmup
def process_file_with_cleanup_warmup(filename):
    pass


# ============================================================================
# YOUR MAIN EXERCISE: Build a Robust Security Monitoring System
# ============================================================================
"""
CUSTOM SECURITY EXCEPTION FRAMEWORK:
Define these custom exceptions, all inheriting from a base `SecurityException(Exception)`:
- `NetworkSecurityError(SecurityException)`
- `DataValidationError(SecurityException)`
- `ConfigurationError(SecurityException)`
- `SecurityPolicyError(SecurityException)`

SECURE FILE PROCESSING ENGINE:
`secure_file_processor(filename, operation_type)`:
  `operation_type` can be "read", "parse", "validate".
  - "read": Returns file content.
  - "parse": Assumes "key=value" lines. Returns list of {"key": k, "value": v} dicts.
             Raises `DataValidationError` if a line (not comment/empty) isn't "key=value".
  - "validate": Checks if content is empty or contains "CRITICAL".
                Returns True if valid (not empty, no "CRITICAL").
                Raises `DataValidationError` if empty or "CRITICAL" found.
  General Errors: Raise `FileNotFoundError`, `PermissionError` as appropriate.
                  Wrap other IOErrors in `ConfigurationError`.
  Logging: For each operation (start, success, failure), append to "security_operations.log":
           "[TIMESTAMP] [LEVEL] Operation: [op_type] on [filename] - Details: [success/error msg]"
           (LEVEL can be INFO or ERROR)
  Return: A dictionary `{"success": True/False, "data": ..., "error": "message if failed"}`.
          `data` is content for "read", list of dicts for "parse", boolean for "validate".

NETWORK SECURITY MONITORING SERVICE:
`monitor_network_security(ip_list, port_list)`:
  Inputs: list of IP strings, list of port integers.
  Simulate checks: For each IP/port:
    - If IP is "0.0.0.0", raise `NetworkSecurityError("Monitoring all interfaces is a risk")`.
    - If port is < 1 or > 65535, raise `DataValidationError("Invalid port number")`.
    - Randomly simulate "open", "closed", or "timeout".
    - If "timeout", raise `NetworkSecurityError("Connection timeout")`.
  Return: A list of dictionaries, one for each successful check:
          `{"ip": ..., "port": ..., "status": "open/closed"}`.
          If an error occurs for an IP/port, that check is skipped (not in returned list).
          The function itself should not crash but continue with other IPs/ports.

SECURITY CONFIGURATION VALIDATOR:
`validate_security_config(config_dict)`:
  Input: A dictionary representing a parsed configuration.
  Validations:
    - Required keys: "firewall_enabled", "max_login_attempts". If missing, raise `ConfigurationError`.
    - "firewall_enabled" must be True. If not, raise `SecurityPolicyError`.
    - "max_login_attempts" must be an int between 3 and 10 (inclusive). If not, raise `DataValidationError`.
  Return: True if all validations pass. Otherwise, the function will raise an exception.

INTEGRATED SECURITY DASHBOARD (Class):
`SecurityDashboard(name)`:
  - `__init__(self, name)`: Store `name`. Init `successful_ops = 0`, `failed_ops = 0`, `error_log = []` (list of error strings).
  - `_log_error(self, operation_name, error_instance)`: Appends f"{operation_name} failed: {type(error_instance).__name__} - {error_instance}" to `self.error_log`. Increments `failed_ops`.
  - `process_file_batch(self, filenames_ops_tuples)`: Takes list of `(filename, op_type)` tuples.
    Calls `secure_file_processor` for each. If `result["success"]` is True, increment `successful_ops`. Else, call `_log_error`.
    Return list of all results from `secure_file_processor`.
  - `run_network_checks(self, ips, ports)`: Calls `monitor_network_security`.
    If `monitor_network_security` raises any `SecurityException` (or its children) or `DataValidationError`,
    call `_log_error`. Otherwise (if no exception or other type of exception), increment `successful_ops`.
    Return results from `monitor_network_security` or None if a caught exception occurred.
  - `audit_configurations(self, config_dicts_map)`: Takes a dict `{"configname": config_dict}`.
    Calls `validate_security_config` for each. If True, increment `successful_ops`.
    If any of the defined custom exceptions (or `DataValidationError`) are raised, call `_log_error`.
    Return a dict `{"configname": True/False (validation_status)}`.
  - `get_dashboard_summary(self)`: Returns a string summarizing total ops, successful, failed, and lists errors from `error_log`.

COMPREHENSIVE SYSTEM TESTING (Function):
`run_security_monitoring_test()`:
  - Create sample files:
    - "valid_read.txt": "Secure data"
    - "valid_parse.ini": "key1=val1\nkey2=val2"
    - "invalid_parse.ini": "key1=val1\nbadline"
    - "critical_content.txt": "Contains CRITICAL keyword"
    - "empty_file.txt": ""
  - Instantiate `SecurityDashboard`.
  - Call its methods with a mix of valid and invalid inputs to trigger errors and successes.
    (e.g., process valid files, non-existent files, files causing parse/validation errors).
    (e.g., run network checks with valid IPs, "0.0.0.0", invalid ports).
    (e.g., audit valid configs, configs missing keys, configs violating policies).
  - Call `get_dashboard_summary()` and print it.
  - Ensure "security_operations.log" is created and has entries.
"""

# YOUR CODE GOES HERE
# ============================================================================


# PART 1: Create Custom Security Exceptions
# TODO: Define your 4 custom exception classes here
class SecurityException(Exception):
    pass

class NetworkSecurityError(SecurityException):
    pass

class DataValidationError(SecurityException):
    pass

class ConfigurationError(SecurityException):
    pass

class SecurityPolicyError(SecurityException):
    pass

# PART 2: Robust File Processing Function
# TODO: Implement secure_file_processor function
def secure_file_processor(filename, operation_type):
    pass

# PART 3: Network Security Monitor
# TODO: Implement monitor_network_security function
def monitor_network_security(ip_list, port_list):
    pass

# PART 4: Configuration Validator
# TODO: Implement validate_security_config function
def validate_security_config(config_dict):
    pass

# PART 5: Comprehensive Security Dashboard
# TODO: Implement SecurityDashboard class
class SecurityDashboard:
    pass

# PART 6: Integration Test
# TODO: Implement run_security_monitoring_test function
def run_security_monitoring_test():
    pass


# ============================================================================
# BUILT-IN TESTS - Check Your Work!
# ============================================================================
# Ensure this log file is cleaned up if it's created by tests/warmups
LOG_FILE_WARMUP = "cleanup_log.txt"
LOG_FILE_MAIN = "security_operations.log"

def cleanup_test_env():
    test_files = [
        LOG_FILE_WARMUP, LOG_FILE_MAIN,
        "warmup_read_test.txt", "valid_read.txt", "valid_parse.ini",
        "invalid_parse.ini", "critical_content.txt", "empty_file.txt",
        "test_error_file.txt" # From original test_error_handling
    ]
    for f in test_files:
        if os.path.exists(f):
            try:
                os.remove(f)
            except Exception:
                pass # Best effort

def setup_warmup_files():
    cleanup_test_env() # Clean before setting up
    with open("warmup_read_test.txt", "w") as f:
        f.write("Test content for warmup.")

def test_warmup_error_handling():
    warmup_passed = 0
    total_warmup_tests = 4
    setup_warmup_files()

    # Test 1
    try:
        assert safe_convert_to_int("123") == 123
        assert safe_convert_to_int("abc") == "Invalid number"
        print("✅ Warm-up Exercise 1 PASSED")
        warmup_passed += 1
    except Exception as e: print(f"❌ Warm-up Exercise 1 FAILED: {e}")

    # Test 2
    try:
        assert read_config_file_warmup("warmup_read_test.txt") == "Test content for warmup."
        assert read_config_file_warmup("non_existent_warmup.txt") == "File not found"
        print("✅ Warm-up Exercise 2 PASSED")
        warmup_passed += 1
    except Exception as e: print(f"❌ Warm-up Exercise 2 FAILED: {e}")

    # Test 3
    try:
        assert safe_divide_warmup(10, 2) == 5.0
        assert safe_divide_warmup(10, 0) == "Cannot divide by zero"
        assert safe_divide_warmup(10, "a") == "Invalid input types"
        # Test for generic exception (e.g., by passing an object that can't be divided)
        class Unusable: pass
        # This check might be tricky if the generic Exception is too broad in implementation.
        # For now, we assume the specific ones are prioritized.
        # Consider adding a specific case that triggers the generic `except Exception`.
        print("✅ Warm-up Exercise 3 PASSED")
        warmup_passed += 1
    except Exception as e: print(f"❌ Warm-up Exercise 3 FAILED: {e}")

    # Test 4
    try:
        # Successful read
        assert process_file_with_cleanup_warmup("warmup_read_test.txt") == "Test content for warmup."
        assert os.path.exists(LOG_FILE_WARMUP)
        with open(LOG_FILE_WARMUP, "r") as f: assert "warmup_read_test.txt" in f.read()
        os.remove(LOG_FILE_WARMUP) # Clean for next sub-test

        # File not found
        assert process_file_with_cleanup_warmup("non_existent_cleanup.txt") is None
        assert os.path.exists(LOG_FILE_WARMUP)
        with open(LOG_FILE_WARMUP, "r") as f: assert "non_existent_cleanup.txt" in f.read()
        print("✅ Warm-up Exercise 4 PASSED")
        warmup_passed += 1
    except Exception as e: print(f"❌ Warm-up Exercise 4 FAILED: {e}")


    print(f"\nWarm-up Score: {warmup_passed}/{total_warmup_tests} exercises completed correctly.")
    return warmup_passed == total_warmup_tests

def test_main_error_handling_system():
    main_passed = True
    # Setup files needed for main tests within run_security_monitoring_test or here
    # For simplicity, run_security_monitoring_test should handle its own file creation/cleanup
    # or we centralize it more carefully.

    # Test Part 1: Custom exceptions
    try:
        custom_exceptions = [NetworkSecurityError, DataValidationError, ConfigurationError, SecurityPolicyError, SecurityException]
        for exc in custom_exceptions:
            assert issubclass(exc, Exception), f"{exc.__name__} is not an Exception."
        assert issubclass(NetworkSecurityError, SecurityException), "NetworkSecurityError should inherit from SecurityException."
        print("✅ Main Test 1 PASSED: Custom exceptions defined correctly.")
    except Exception as e:
        print(f"❌ Main Test 1 FAILED: Custom exceptions - {e}")
        main_passed = False

    # Test Part 2: secure_file_processor
    # This requires file creation and careful checking of security_operations.log
    # Simplified check:
    if 'secure_file_processor' not in globals() or not callable(secure_file_processor):
        print("❌ Main Test 2 FAILED: secure_file_processor function not defined or not callable.")
        main_passed = False
    else:
        # Basic functionality test (more detailed tests would be in run_security_monitoring_test)
        with open("test_sfp.txt", "w") as f: f.write("key=value")
        res = secure_file_processor("test_sfp.txt", "read")
        if not (isinstance(res, dict) and res.get("success") == True and res.get("data") == "key=value"):
            print(f"❌ Main Test 2 FAILED: secure_file_processor 'read' basic test. Got {res}")
            main_passed = False
        else:
            print("✅ Main Test 2 PASSED: secure_file_processor basic 'read' check.")
        if os.path.exists("test_sfp.txt"): os.remove("test_sfp.txt")


    # Test Part 3: monitor_network_security
    if 'monitor_network_security' not in globals() or not callable(monitor_network_security):
        print("❌ Main Test 3 FAILED: monitor_network_security function not defined or not callable.")
        main_passed = False
    else:
        # Basic functionality test
        res = monitor_network_security(["1.1.1.1"], [80])
        if not isinstance(res, list): # Should return a list of dicts for successful checks
            print(f"❌ Main Test 3 FAILED: monitor_network_security did not return a list. Got {type(res)}")
            main_passed = False
        else:
             print("✅ Main Test 3 PASSED: monitor_network_security basic call check.")


    # Test Part 4: validate_security_config
    if 'validate_security_config' not in globals() or not callable(validate_security_config):
        print("❌ Main Test 4 FAILED: validate_security_config function not defined or not callable.")
        main_passed = False
    else:
        # Basic functionality test
        valid_conf = {"firewall_enabled": True, "max_login_attempts": 5}
        invalid_conf = {"firewall_enabled": False, "max_login_attempts": 5}
        try:
            assert validate_security_config(valid_conf) is True, "Valid config failed validation."
        except Exception: # Should not raise for valid
             print(f"❌ Main Test 4 FAILED: validate_security_config raised on valid config.")
             main_passed = False
        
        raised_expected = False
        try:
            validate_security_config(invalid_conf) # Should raise SecurityPolicyError
        except SecurityPolicyError:
            raised_expected = True
        except Exception as e:
            print(f"❌ Main Test 4 FAILED: validate_security_config raised wrong exception for invalid config: {type(e)}.")
            main_passed = False
        if not raised_expected and main_passed : # if it didn't fail for other reasons
            print(f"❌ Main Test 4 FAILED: validate_security_config did not raise SecurityPolicyError for invalid config.")
            main_passed = False
        elif raised_expected:
             print("✅ Main Test 4 PASSED: validate_security_config basic checks.")


    # Test Part 5: SecurityDashboard class
    if 'SecurityDashboard' not in globals() or not isinstance(SecurityDashboard, type):
         print("❌ Main Test 5 FAILED: SecurityDashboard class not defined.")
         main_passed = False
    else:
        try:
            dashboard = SecurityDashboard("TestDash")
            # Check for methods - more detailed tests are part of run_security_monitoring_test
            assert hasattr(dashboard, "process_file_batch")
            assert hasattr(dashboard, "run_network_checks")
            assert hasattr(dashboard, "audit_configurations")
            assert hasattr(dashboard, "get_dashboard_summary")
            print("✅ Main Test 5 PASSED: SecurityDashboard class basic structure.")
        except Exception as e:
            print(f"❌ Main Test 5 FAILED: SecurityDashboard instantiation or method check - {e}")
            main_passed = False

    # Test Part 6: run_security_monitoring_test
    if 'run_security_monitoring_test' not in globals() or not callable(run_security_monitoring_test):
        print("❌ Main Test 6 FAILED: run_security_monitoring_test function not defined or not callable.")
        main_passed = False
    else:
        # This is a complex test. We'll just call it and assume it prints its own pass/fail.
        # A more rigorous test would capture its output or check file states.
        print("Running run_security_monitoring_test (output will follow):")
        try:
            run_security_monitoring_test() # This function should create its own files and print summary
            # Check if security_operations.log was created as a side effect.
            assert os.path.exists(LOG_FILE_MAIN), f"{LOG_FILE_MAIN} was not created by run_security_monitoring_test."
            print(f"✅ Main Test 6 PASSED: run_security_monitoring_test executed and {LOG_FILE_MAIN} created.")
        except Exception as e:
            print(f"❌ Main Test 6 FAILED: run_security_monitoring_test execution error - {e}")
            main_passed = False


    if main_passed: print("\n🎉 SOME MAIN EXERCISE CHECKS PASSED (structural and basic calls)!")
    else: print("\n❌ SOME MAIN EXERCISE CHECKS FAILED.")
    return main_passed

def run_all_tests():
    """Run all tests for Module 9."""
    # No global setup/cleanup here, as run_security_monitoring_test handles its own files
    # and warmup tests also manage their specific files.
    # The cleanup_test_env can be called at the very end.

    print("="*50)
    print("RUNNING WARM-UP TESTS...")
    print("="*50)
    warmup_success = test_warmup_error_handling()

    print("\n" + "="*50)
    print("RUNNING MAIN EXERCISE CHECKS...")
    print("="*50)
    main_exercise_success = test_main_error_handling_system()

    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    if warmup_success and main_exercise_success:
        print("\n✅ All warm-up and main exercise tests passed (basic checks for main)!")
        print("You've successfully mastered Python error handling!")
        print("🎓 You have completed the entire Python for Cybersecurity course!")
    else:
        print("\n📚 Keep practicing! Review the failed tests or checks above.")
        if not warmup_success: print("- Some warm-up exercises have issues.")
        if not main_exercise_success: print("- The main exercise has issues or missing components.")

    cleanup_test_env() # Final cleanup of all test files

if __name__ == "__main__":
    run_all_tests()

# ============================================================================
# COURSE COMPLETION CELEBRATION!
# ============================================================================
"""
🎉 CONGRATULATIONS! YOU'VE COMPLETED THE PYTHON FOR CYBERSECURITY COURSE! 🎉

Here's everything you've mastered in this comprehensive journey:

MODULE 1 - VARIABLES & DATA TYPES ✅
- Storing and managing cybersecurity data
- Working with different data types for security applications

MODULE 2 - OPERATORS ✅  
- Building logical security conditions
- Creating threshold monitoring and comparison logic

MODULE 3 - CONDITIONAL STATEMENTS ✅
- Implementing intelligent security decision-making
- Automated security policy enforcement

MODULE 4 - LOOPS ✅
- Automating repetitive security tasks
- Processing large datasets and log files

MODULE 5 - LISTS ✅
- Managing collections of security data
- Working with IP addresses, user accounts, and security alerts

MODULE 6 - DICTIONARIES ✅
- Organizing complex security information
- Building structured security databases and configurations

MODULE 7 - FUNCTIONS ✅
- Creating reusable security tools and modules
- Building organized, maintainable security code

MODULE 8 - FILE I/O ✅
- Processing security logs, configuration files, and reports
- Implementing data persistence and file management

MODULE 9 - ERROR HANDLING ✅
- Building robust, production-ready security tools
- Implementing comprehensive error resilience

CYBERSECURITY SKILLS YOU'VE GAINED:
🔐 Security monitoring and alerting systems
🔐 Automated threat detection and response
🔐 Log analysis and pattern recognition
🔐 Network scanning and vulnerability assessment
🔐 User management and access control
🔐 Configuration management and compliance
🔐 Incident response automation
🔐 Security reporting and metrics
🔐 Error handling and system resilience

WHAT'S NEXT?
You now have a solid foundation in Python for cybersecurity! Consider exploring:
- Advanced Python libraries (requests, pandas, matplotlib)
- Cybersecurity frameworks (NIST, MITRE ATT&CK)
- Security tools integration (APIs, automation platforms)
- Advanced topics (machine learning for security, threat hunting)

Keep building amazing cybersecurity tools! 🚀🛡️
"""

# Final decorative print is fine here.
# print("\n" + "🎓" * 20)
# print("PYTHON FOR CYBERSECURITY COURSE COMPLETED!")
# print("🎓" * 20)
# print("\nYou're now ready to build professional cybersecurity automation!")
# print("Keep coding, keep securing, and welcome to the world of cybersecurity programming! 🐍🔒")
