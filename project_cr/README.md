# Simple Change Request Module

A simple Odoo module for managing change requests with a user-friendly web interface.

## Features

- **Comprehensive Change Request Form**: Complete form with all necessary fields
- **Status Workflow**: Draft → Submitted → Approved → Completed
- **Priority Levels**: Low, Medium, High, Urgent
- **Request Types**: System, Process, Policy, Other
- **User-Friendly Interface**: Clean, modern web form
- **Search & Filtering**: Advanced search capabilities
- **Automatic Numbering**: Auto-generated request numbers (CR-0001, CR-0002, etc.)

## Installation

1. Copy this module to your Odoo addons directory
2. Restart your Odoo server
3. Go to Apps menu in Odoo
4. Search for "Simple Change Request"
5. Click Install

## Usage

### Creating a Change Request

1. Navigate to **Change Requests** menu
2. Click **Create** button
3. Fill in the form with:
   - **Request Title**: Brief description of the change
   - **Requester**: Automatically filled with current user
   - **Department**: Your department
   - **Request Type**: Select appropriate type
   - **Priority**: Set priority level
   - **Expected Completion**: Target completion date
   - **Description**: Detailed description of the change
   - **Business Justification**: Why this change is needed
   - **Impact Analysis**: Potential impact of the change

### Workflow States

- **Draft**: Initial state when creating a request
- **Submitted**: Request has been submitted for review
- **Approved**: Request has been approved and can proceed
- **Rejected**: Request has been rejected
- **Completed**: Request has been completed

### Navigation

- **Change Requests**: View all change requests
- **My Requests**: View only your own requests

### Search & Filtering

Use the search bar and filters to find specific requests by:
- Title, description, or requester
- Status (Draft, Submitted, Approved, etc.)
- Priority level
- Request type
- Department

## File Structure

```
project_cr/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   └── simple_change_request.py
├── views/
│   └── simple_change_request_views.xml
├── data/
│   ├── demo_data.xml
│   └── sequence_data.xml
└── security/
    └── ir.model.access.csv
```

## Technical Details

- **Model**: `simple.change.request`
- **Dependencies**: base
- **Version**: 1.0
- **Author**: Your Name

## Customization

You can customize this module by:
- Adding more fields to the model
- Modifying the form layout
- Adding new workflow states
- Customizing the CSS styling
- Adding email notifications
- Integrating with other modules 