"""
====================================================================
MODULE 4: LISTS - Managing Collections of Security Data 📋
====================================================================

Welcome to Module 4! You've been using lists in previous modules, but now
you'll master them completely. Lists are essential for cybersecurity work
because you're always dealing with collections: IP addresses, user accounts,
security alerts, port numbers, and more.

WHAT ARE LISTS?
Lists are ordered collections that can store multiple items. Think of them
as containers that hold related data together, like a list of authorized
users or a collection of suspicious IP addresses.

LIST OPERATIONS WE'LL COVER:
- Creating and accessing lists
- Adding and removing items
- Searching and sorting lists
- List slicing and manipulation
- Common list methods for security work
"""

import random # For conceptual example

# ============================================================================
# CONCEPT EXPLANATION: Creating and Accessing Lists
# ============================================================================

# Creating lists
authorized_users_conceptual = ["admin", "securityteam", "manager", "analyst"] # Renamed
open_ports_conceptual = [22, 80, 443, 8080] # Renamed
mixed_data_conceptual = ["server1", 192, True, "active"] # Renamed
empty_list_conceptual = [] # Renamed

print("List Examples:")
print(f"Authorized users (conceptual): {authorized_users_conceptual}")
print(f"Open ports (conceptual): {open_ports_conceptual}")
print(f"Mixed data (conceptual): {mixed_data_conceptual}")
print(f"Empty list (conceptual): {empty_list_conceptual}")

# Accessing list items (indexing starts at 0)
print("\nAccessing List Items:") # Added newline for clarity
print(f"First user: {authorized_users_conceptual[0]}")
print(f"Second user: {authorized_users_conceptual[1]}")
print(f"Last user: {authorized_users_conceptual[-1]}")
print(f"Second to last user: {authorized_users_conceptual[-2]}")

# List length
print(f"\nNumber of authorized users: {len(authorized_users_conceptual)}") # Added newline
print(f"Number of open ports: {len(open_ports_conceptual)}")

# ============================================================================
# CONCEPT EXPLANATION: Adding and Removing Items
# ============================================================================

# Starting with a list of blocked IPs
blocked_ips_conceptual = ["203.0.113.42", "198.51.100.1"] # Renamed
print(f"\nInitial blocked IPs (conceptual): {blocked_ips_conceptual}") # Added newline

# Adding items
blocked_ips_conceptual.append("192.0.2.146")
print(f"After append: {blocked_ips_conceptual}")
blocked_ips_conceptual.insert(1, "10.0.0.255")
print(f"After insert: {blocked_ips_conceptual}")

# Adding multiple items
new_threats_conceptual = ["172.16.0.100", "192.168.1.200"] # Renamed
blocked_ips_conceptual.extend(new_threats_conceptual)
print(f"After extend: {blocked_ips_conceptual}")

# Removing items
print("\nRemoving items (conceptual):") # Added newline
removed_ip_conceptual = blocked_ips_conceptual.pop() # Renamed
print(f"Removed last IP: {removed_ip_conceptual}")
print(f"List after pop: {blocked_ips_conceptual}")
blocked_ips_conceptual.remove("10.0.0.255")
print(f"After removing specific IP: {blocked_ips_conceptual}")
del blocked_ips_conceptual[0]
print(f"After deleting first item: {blocked_ips_conceptual}")

# ============================================================================
# CONCEPT EXPLANATION: Searching and Sorting
# ============================================================================

# Searching in lists
security_tools_conceptual = ["nmap", "wireshark", "metasploit", "burpsuite", "nessus"] # Renamed
print(f"\nSecurity tools (conceptual): {security_tools_conceptual}") # Added newline

tool_to_find_conceptual = "wireshark" # Renamed
if tool_to_find_conceptual in security_tools_conceptual:
    print(f"✅ {tool_to_find_conceptual} is available")
    position = security_tools_conceptual.index(tool_to_find_conceptual)
    print(f"Position of {tool_to_find_conceptual}: {position}")
else:
    print(f"❌ {tool_to_find_conceptual} not found")

# Counting occurrences
log_levels_conceptual = ["INFO", "WARNING", "ERROR", "INFO", "CRITICAL", "INFO", "ERROR"] # Renamed
print(f"\nLog levels (conceptual): {log_levels_conceptual}") # Added newline
print(f"INFO messages: {log_levels_conceptual.count('INFO')}")
print(f"ERROR messages: {log_levels_conceptual.count('ERROR')}")

# Sorting lists
vulnerability_scores_conceptual = [7.5, 9.2, 4.1, 8.8, 6.3, 9.9, 2.1] # Renamed
print(f"\nOriginal vulnerability scores (conceptual): {vulnerability_scores_conceptual}") # Added newline
sorted_scores_conceptual = sorted(vulnerability_scores_conceptual)
print(f"Sorted scores (ascending): {sorted_scores_conceptual}")
sorted_scores_desc_conceptual = sorted(vulnerability_scores_conceptual, reverse=True)
print(f"Sorted scores (descending): {sorted_scores_desc_conceptual}")
vulnerability_scores_conceptual.sort(reverse=True)
print(f"Original list after in-place sort: {vulnerability_scores_conceptual}")

# ============================================================================
# CONCEPT EXPLANATION: List Slicing
# ============================================================================

network_devices_conceptual = ["router", "switch", "firewall", "server", "workstation", "printer", "camera"] # Renamed
print(f"\nAll devices (conceptual): {network_devices_conceptual}") # Added newline
print(f"First 3 devices: {network_devices_conceptual[:3]}")
print(f"Last 3 devices: {network_devices_conceptual[-3:]}")
print(f"Middle devices: {network_devices_conceptual[2:5]}")
print(f"Every other device: {network_devices_conceptual[::2]}")
print(f"Reversed list: {network_devices_conceptual[::-1]}")

# ============================================================================
# CONCEPT EXPLANATION: List Comprehensions (Advanced)
# ============================================================================

port_numbers_conceptual = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 993, 995] # Renamed
print(f"\nAll ports (conceptual): {port_numbers_conceptual}") # Added newline
high_ports_conceptual = [port for port in port_numbers_conceptual if port > 1000] # Renamed
print(f"High ports (>1000): {high_ports_conceptual}")
port_descriptions_conceptual = [f"Port {port}" for port in port_numbers_conceptual[:5]] # Renamed
print(f"Port descriptions: {port_descriptions_conceptual}")

# ============================================================================
# HOW THIS APPLIES TO CYBERSECURITY ADMINISTRATION:
# ============================================================================
"""
CYBERSECURITY APPLICATIONS OF LISTS:
1. IP ADDRESS MANAGEMENT: Whitelist, Blacklist, Subnet ranges, DHCP pools
2. USER AND ACCESS MANAGEMENT: User accounts, Role assignments, Access logs
3. SECURITY MONITORING: Alert types, Event logs, Threat indicators (IOCs)
4. NETWORK SECURITY: Open/Blocked ports, Protocol monitoring, Firewall rules
5. INCIDENT RESPONSE: Affected systems, Evidence collection, Response team
6. CONFIGURATION MANAGEMENT: Security tools, Policy settings, Patch levels
"""

# Security incident management
incident_priorities_conceptual = ["Low", "Medium", "High", "Critical"] # Renamed
active_incidents_conceptual = [ # Renamed
    "Phishing attempt from external email", "Suspicious login from foreign IP",
    "Malware detected on workstation-42", "Unauthorized access to admin panel"
]
print("\nCurrent Security Incidents (Conceptual):") # Added newline
for i, incident in enumerate(active_incidents_conceptual):
    priority = incident_priorities_conceptual[min(i, len(incident_priorities_conceptual)-1)]
    print(f"[{priority}] {incident}")

# Network asset management
critical_servers_conceptual = ["web-server", "database-server", "mail-server", "backup-server"] # Renamed
server_status_list_conceptual = [] # Renamed
print("\nServer Status Check (Conceptual):") # Added newline
for server in critical_servers_conceptual:
    status = "ONLINE" if random.choice([True, False]) else "OFFLINE"
    server_status_list_conceptual.append(status)
    print(f"{server}: {status}")
offline_servers_conceptual = [critical_servers_conceptual[i] for i, status in enumerate(server_status_list_conceptual) if status == "OFFLINE"] # Renamed
if offline_servers_conceptual:
    print(f"⚠️  Servers requiring attention: {offline_servers_conceptual}")
else:
    print("✅ All critical servers are online")

# ============================================================================
# WARM-UP EXERCISES: Practice Using Lists
# ============================================================================

# Initialize global variables for warmup outputs
warmup1_devices_list = []
warmup1_devices_length = 0
warmup2_users_list_modified = [] # This will hold the state of the list after modification
warmup3_services_list_modified = []
warmup4_port22_allowed = None
warmup4_port21_allowed = None


# Exercise 1: Create and print a simple list
"""
PRACTICE: Initial Device Inventory

Your organization is setting up its network. The first three core devices acquired are
a "firewall", then a "router", and finally a "switch".
You need to create a list representing this initial inventory in the order they were acquired.
Also, record the total number of devices in this initial list.

(Store the list itself in a global variable named warmup1_devices_list
count of devices in `warmup1_devices_length` for automated checking.)
"""
# TODO: Create a list with "firewall", "router", "switch".
# TODO: Assign this list to `warmup1_devices_list`.
# TODO: Calculate its length and assign to `warmup1_devices_length`.
warmup1_devices_list=["firewall", "router", "switch"]
warmup1_devices_length=len(warmup1_devices_list)


# Exercise 2: Add item to list
"""
PRACTICE: Expanding User Access

Initially, your system has two types of users: "admin" and "guest".
A new user role, "operator", needs to be added to this list of user types.
The new role should be added at the end of the existing list.

(Start with a list `users_warmup2` containing "admin" and "guest".
After adding "operator", store the final list in the global variable
`warmup2_users_list_modified`.)
"""
# TODO: Create `users_warmup2` with "admin", "guest".
# TODO: Append "operator" to this list.
# TODO: Assign the modified list to `warmup2_users_list_modified`.


# Exercise 3: Remove item from list
"""
PRACTICE: Decommissioning a Service

Your current list of active network services is "web", "mail", "test", and "dns".
The "test" service is being decommissioned and needs to be removed from this list.
Ensure your code can handle the case where "test" might already be missing,
though for this specific exercise, it will be present.

(Start with a list `services_warmup3` containing these four services.
After removing "test", store the updated list in the global variable
`warmup3_services_list_modified`.)
"""
# TODO: Create `services_warmup3` with "web", "mail", "test", "dns".
# TODO: Remove "test" from the list.
# TODO: Assign the modified list to `warmup3_services_list_modified`.


# Exercise 4: Check if item exists in list
"""
PRACTICE: Validating Allowed Ports

Your firewall has a list of currently allowed incoming ports: 22, 80, and 443.
You need to perform two checks:
1. Is port 22 currently allowed?
2. Is port 21 currently allowed?
Record the true/false results of these checks.

(Define the list of allowed ports as `allowed_ports_warmup4`.
Store the boolean result for port 22 in `warmup4_port22_allowed`.
Store the boolean result for port 21 in `warmup4_port21_allowed`.)
"""
# TODO: Create `allowed_ports_warmup4` with 22, 80, 443.
# TODO: Check if 22 is in the list and assign the result to `warmup4_port22_allowed`.
# TODO: Check if 21 is in the list and assign the result to `warmup4_port21_allowed`.


# ============================================================================
# YOUR MAIN EXERCISE: Build a Security Asset Management System
# ============================================================================
"""
CHALLENGE: SECURITY ASSET MANAGEMENT SYSTEM

You're building a system to manage various security assets within your organization.
This involves tracking network devices, user accounts, security alerts, and
vulnerability data. Each task below builds upon lists to manage this information.

TASK 1: NETWORK INFRASTRUCTURE TRACKING
   Your initial list of core network devices is: "firewall", "router", "switch", "server".
   Two updates are needed:
   1. An "intrusion_detection_system" has been added. Append it to your list.
   2. A "load_balancer" was installed earlier and should be inserted into the list
      right after the "router" (i.e., it will become the third item if "router" is second).
   (Start with `network_devices`. After these operations, make the final list available
   as `final_network_devices`, and store the total count of devices in `final_device_count`.)

TASK 2: USER ACCOUNT MANAGEMENT
   The current list of user account types is: "admin", "user1", "user2", "guest".
   Perform these changes:
   1. The "guest" account type is being removed.
   2. Two new account types, "analyst" and "manager", are being added to the list.
   After these changes, also verify if the "admin" account type is still present.
   (Start with `user_accounts`. The final list of account types should be stored in
   `final_user_accounts`. A boolean indicating if "admin" is in this final list
   should be stored in `is_admin_in_final_list`.)

TASK 3: SECURITY ALERT TRACKING
   You have received four security alerts as plain text messages:
     Alert 1: "Failed login attempt from IP address 203.0.113.42"
     Alert 2: "High CPU usage detected on server-01"
     Alert 3: "Suspicious file detected in downloads folder"
     Alert 4: "Firewall rule violation from internal network"
   Your tasks are:
   1. Collect these four alerts into a list called `security_alerts_log`.
   2. Create a new list, `formatted_initial_alerts`, where each alert message from
      `security_alerts_log` is prefixed by its 1-based index number (e.g., "1: Alert message...").
   3. The first alert in `security_alerts_log` has been resolved. Remove it from the list.
      Store the content of this removed alert in `removed_alert_content`.
   4. Create another list, `formatted_remaining_alerts`, from the updated `security_alerts_log`
      (after removal), again prefixing each alert with its new 1-based index.

TASK 4: VULNERABILITY ASSESSMENT
   You have a list of raw vulnerability scores from a recent scan: `[8.5, 6.2, 9.1, 4.3, 7.8]`.
   Process these scores:
   1. Sort these scores in descending order (highest to lowest). Store this sorted list
      in `sorted_vulnerability_scores`. The original list can be modified or you can create a new one.
   2. From the `sorted_vulnerability_scores`, create a new list called `high_severity_vulns_list`
      that includes only scores greater than 7.0.
   3. Calculate the average of the original `vulnerability_scores`. If the list of scores
      were empty, the average should be considered 0.0. Store this average in `average_vuln_score`.
   (Define the initial `vulnerability_scores` list yourself as part of your solution for this task.)

TASK 5: SECURITY DASHBOARD SUMMARY DATA
   To populate a security dashboard, you need to consolidate some key metrics from the
   previous tasks. Create the following global variables and assign them values based on
   the final state of your data from Tasks 1-4:
   - `dashboard_total_devices`: The total number of network devices (from `final_device_count`).
   - `dashboard_total_users`: The total number of user account types (from `final_user_accounts`).
   - `dashboard_active_alerts_count`: The number of alerts remaining in `security_alerts_log`.
   - `dashboard_highest_vulnerability`: The highest score from `sorted_vulnerability_scores`
     (if the list is empty, this should be 0.0).

Ensure all results are stored in the specified global variables for checking.
"""

# YOUR CODE GOES HERE
# ============================================================================

# Initialize global variables for Main Exercise results
final_network_devices = []
final_device_count = 0
final_user_accounts = []
is_admin_in_final_list = False
security_alerts_log = []
formatted_initial_alerts = []
removed_alert_content = ""
formatted_remaining_alerts = []
vulnerability_scores = [] # This will be initialized by user for TASK 4
sorted_vulnerability_scores = []
high_severity_vulns_list = []
average_vuln_score = 0.0
dashboard_total_devices = 0
dashboard_total_users = 0
dashboard_active_alerts_count = 0
dashboard_highest_vulnerability = 0.0

# PART 1: Network Infrastructure Tracking
# TODO: Define initial network_devices, perform operations, assign to final_network_devices and final_device_count


# PART 2: User Account Management
# TODO: Define initial user_accounts, perform operations, assign to final_user_accounts and is_admin_in_final_list


# PART 3: Security Alert Tracking
# TODO: Define initial alerts, populate security_alerts_log, create formatted_initial_alerts,
#       remove first alert into removed_alert_content, create formatted_remaining_alerts.


# PART 4: Vulnerability Assessment
# TODO: Define initial vulnerability_scores, then populate sorted_vulnerability_scores,
#       high_severity_vulns_list, and average_vuln_score.


# PART 5: Security Dashboard Summary Data
# TODO: Assign values to dashboard_total_devices, dashboard_total_users,
#       dashboard_active_alerts_count, and dashboard_highest_vulnerability.


# ============================================================================
# BUILT-IN TESTS - Check Your Work!
# ============================================================================

print("\n" + "="*50)
print("RUNNING TESTS...")
print("="*50)

def test_warmup_lists():
    """Tests for the warm-up list exercises."""
    print("--- Testing Warm-up Exercises ---")
    passed_count = 0
    # Test 1
    try:
        # User should have defined devices_warmup1 and assigned to globals
        assert warmup1_devices_list == ["firewall", "router", "switch"], "Warmup 1: Device list incorrect"
        assert warmup1_devices_length == 3, "Warmup 1: Device length incorrect"
        print("✅ Warm-up 1 PASSED")
        passed_count += 1
    except (NameError, AssertionError) as e: print(f"❌ Warm-up 1 FAILED: {e}")
    # Test 2
    try:
        # User should have created users_warmup2, modified it, and assigned to global
        assert warmup2_users_list_modified == ["admin", "guest", "operator"], "Warmup 2: Add operator failed"
        print("✅ Warm-up 2 PASSED")
        passed_count += 1
    except (NameError, AssertionError) as e: print(f"❌ Warm-up 2 FAILED: {e}")
    # Test 3
    try:
        # User should have created services_warmup3, modified it, and assigned to global
        assert warmup3_services_list_modified == ["web", "mail", "dns"], "Warmup 3: Remove 'test' failed"
        print("✅ Warm-up 3 PASSED")
        passed_count += 1
    except (NameError, AssertionError) as e: print(f"❌ Warm-up 3 FAILED: {e}")
    # Test 4
    try:
        assert warmup4_port22_allowed is True, "Warmup 4: Port 22 check failed"
        assert warmup4_port21_allowed is False, "Warmup 4: Port 21 check failed"
        print("✅ Warm-up 4 PASSED")
        passed_count += 1
    except (NameError, AssertionError) as e: print(f"❌ Warm-up 4 FAILED: {e}")

    print(f"Warm-up Score: {passed_count}/4 passed.")
    return passed_count == 4

def test_main_exercise_asset_management(): # Renamed for clarity
    """Test function to verify your main exercise list operations are correct."""
    print("\n--- Testing Main Exercise ---")
    main_passed = True

    # TASK 1 Tests
    try:
        expected_devices = ["firewall", "router", "load_balancer", "switch", "server", "intrusion_detection_system"]
        assert final_network_devices == expected_devices, f"TASK 1: final_network_devices incorrect. Expected {expected_devices}, got {final_network_devices}"
        assert final_device_count == len(expected_devices), f"TASK 1: final_device_count incorrect. Expected {len(expected_devices)}, got {final_device_count}"
        print("✅ TASK 1 (Network Devices): PASSED")
    except (NameError, AssertionError) as e:
        print(f"❌ TASK 1 (Network Devices): FAILED - {e}")
        main_passed = False

    # TASK 2 Tests
    try:
        expected_users = ["admin", "user1", "user2", "analyst", "manager"]
        assert sorted(final_user_accounts) == sorted(expected_users), f"TASK 2: final_user_accounts incorrect. Expected {expected_users} (sorted), got {sorted(final_user_accounts)}"
        assert is_admin_in_final_list is True, "TASK 2: is_admin_in_final_list should be True"
        assert "guest" not in final_user_accounts, "TASK 2: 'guest' should have been removed"
        print("✅ TASK 2 (User Accounts): PASSED")
    except (NameError, AssertionError) as e:
        print(f"❌ TASK 2 (User Accounts): FAILED - {e}")
        main_passed = False

    # TASK 3 Tests
    try:
        initial_alerts_content_for_test = [
            "Failed login attempt from IP address 203.0.113.42",
            "High CPU usage detected on server-01",
            "Suspicious file detected in downloads folder",
            "Firewall rule violation from internal network"
        ]
        expected_formatted_initial = [f"{i+1}: {alert}" for i, alert in enumerate(initial_alerts_content_for_test)]
        assert formatted_initial_alerts == expected_formatted_initial, "TASK 3: formatted_initial_alerts incorrect."
        assert removed_alert_content == initial_alerts_content_for_test[0], "TASK 3: removed_alert_content incorrect."
        assert len(security_alerts_log) == 3, f"TASK 3: security_alerts_log should have 3 items after pop, got {len(security_alerts_log)}"
        expected_formatted_remaining = [f"{i+1}: {alert}" for i, alert in enumerate(initial_alerts_content_for_test[1:])]
        assert formatted_remaining_alerts == expected_formatted_remaining, "TASK 3: formatted_remaining_alerts incorrect."
        print("✅ TASK 3 (Security Alerts): PASSED")
    except (NameError, AssertionError) as e:
        print(f"❌ TASK 3 (Security Alerts): FAILED - {e}")
        main_passed = False

    # TASK 4 Tests
    try:
        original_scores_for_test = [8.5, 6.2, 9.1, 4.3, 7.8]
        # User should have defined vulnerability_scores with these values
        assert vulnerability_scores == original_scores_for_test, "TASK 4: Initial vulnerability_scores list is incorrect or was modified before sorting for sorted_vulnerability_scores."

        expected_sorted_test = sorted(original_scores_for_test, reverse=True)
        assert sorted_vulnerability_scores == expected_sorted_test, f"TASK 4: sorted_vulnerability_scores incorrect. Expected {expected_sorted_test}, got {sorted_vulnerability_scores}"

        expected_high_sev_test = [9.1, 8.5, 7.8]
        assert high_severity_vulns_list == expected_high_sev_test, f"TASK 4: high_severity_vulns_list incorrect. Expected {expected_high_sev_test}, got {high_severity_vulns_list}"

        expected_avg_test = sum(original_scores_for_test) / len(original_scores_for_test) if original_scores_for_test else 0.0
        assert abs(average_vuln_score - expected_avg_test) < 0.001, f"TASK 4: average_vuln_score incorrect. Expected {expected_avg_test}, got {average_vuln_score}"
        print("✅ TASK 4 (Vulnerability Assessment): PASSED")
    except (NameError, AssertionError) as e:
        print(f"❌ TASK 4 (Vulnerability Assessment): FAILED - {e}")
        main_passed = False

    # TASK 5 Tests
    try:
        # These assume previous tasks successfully populated their respective global variables
        expected_dashboard_total_devices = final_device_count if 'final_device_count' in globals() else 0
        expected_dashboard_total_users = len(final_user_accounts) if 'final_user_accounts' in globals() else 0
        expected_dashboard_active_alerts = len(security_alerts_log) if 'security_alerts_log' in globals() else 0
        expected_dashboard_highest_vuln = sorted_vulnerability_scores[0] if 'sorted_vulnerability_scores' in globals() and sorted_vulnerability_scores else 0.0

        assert dashboard_total_devices == expected_dashboard_total_devices, f"TASK 5: dashboard_total_devices. Expected {expected_dashboard_total_devices}, Got {dashboard_total_devices}"
        assert dashboard_total_users == expected_dashboard_total_users, f"TASK 5: dashboard_total_users. Expected {expected_dashboard_total_users}, Got {dashboard_total_users}"
        assert dashboard_active_alerts_count == expected_dashboard_active_alerts, f"TASK 5: dashboard_active_alerts_count. Expected {expected_dashboard_active_alerts}, Got {dashboard_active_alerts_count}"
        assert abs(dashboard_highest_vulnerability - expected_dashboard_highest_vuln) < 0.001, f"TASK 5: dashboard_highest_vulnerability. Expected {expected_dashboard_highest_vuln}, Got {dashboard_highest_vulnerability}"
        print("✅ TASK 5 (Dashboard Summary): PASSED")
    except (NameError, AssertionError) as e:
        print(f"❌ TASK 5 (Dashboard Summary): FAILED - {e}")
        main_passed = False

    if main_passed:
        print("\n🎉 MAIN EXERCISE: All core logic tests passed!")
    else:
        print("\n❌ MAIN EXERCISE: Some core logic tests failed.")
    return main_passed

def run_all_tests(): # Renamed from test_lists
    warmup_ok = test_warmup_lists()
    main_ok = test_main_exercise_asset_management()

    if warmup_ok and main_ok:
        print("\n✅ CONGRATULATIONS! All tests passed!")
        print("You've successfully mastered Python lists!")
        print("Ready for Module 5: Dictionaries") # Updated to 5
    else:
        print("\n📚 Keep practicing! Review the failed tests or messages above.")

# Run the tests
run_all_tests() # Updated call

# ============================================================================
# WHAT'S NEXT?
# ============================================================================
"""
Outstanding work completing Module 5! Here's what you learned:

✅ Creating and accessing lists with indexing
✅ Adding and removing items with append, insert, remove, pop
✅ Searching lists with 'in' operator and index() method
✅ Sorting lists with sort() and sorted() functions
✅ List slicing for extracting portions of data
✅ List comprehensions for creating filtered lists
✅ How to manage cybersecurity data collections effectively

CYBERSECURITY SKILLS GAINED:
- IP address and network device management
- User account and access control lists
- Security alert and incident tracking
- Vulnerability assessment and scoring
- Asset inventory and configuration management
- Log analysis and event processing

NEXT MODULE: 05_dictionaries.py
In the next module, you'll learn about dictionaries - powerful data structures
that store key-value pairs, perfect for organizing complex security information
like user profiles, system configurations, and security policies!

You're building sophisticated data management skills! 📊🔐
"""
