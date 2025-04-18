# Creating a DeepSeek Automation in the Visual Editor

Here's a step-by-step guide for creating an automation that uses DeepSeek in Home Assistant's visual editor:

## Example: Ask DeepSeek for a Recipe Based on Ingredients

### Step 1: Create a New Automation
1. Go to **Settings** > **Automations & Scenes**
2. Click the **+ Create Automation** button
3. Select **Create new automation**
4. Give it a name like "Ask DeepSeek for Recipe Ideas"

### Step 2: Add a Trigger
1. Click **Add Trigger**
2. Select a trigger type (for example, "Time" if you want it to run daily, or "Device" if you want to trigger it from a button press)
3. Configure the trigger details

### Step 3: Call DeepSeek Service and Store Response
1. Click **Add Action**
2. Select **Call service**
3. In the service field, search for and select `deepseek.generate_text`
4. In the service data section, add:
   ```yaml
   prompt: "Please suggest a recipe using these ingredients: eggs, spinach, and cheese. Include easy instructions."
   ```
5. Under **Response Variable** enter `deepseek_response`
   - This is critical as it stores the AI's response for use in subsequent steps

### Step 4: Use the Response
1. Click **Add Action** again
2. Select an action type (e.g., "Call service")
3. Choose a service like `notify.mobile_app` or `persistent_notification.create`
4. For notification data, add:
   ```yaml
   title: "Recipe Suggestion"
   message: "{{ deepseek_response.response }}"
   ```
   - Note the `.response` - this is accessing the specific response field we return from our service

### Step 5: Save Your Automation
1. Click **Save** in the bottom right
2. Test the automation by clicking the **Run Actions** button

## Visual Editor Screenshot Description

In the visual editor, your automation would look like this:

1. **Trigger Section**:
   - A time or device trigger of your choice

2. **Actions Section**:
   - **Action 1**: Call service
     - Service: `deepseek.generate_text`
     - Service Data:
       ```yaml
       prompt: "Please suggest a recipe using these ingredients: eggs, spinach, and cheese. Include easy instructions."
       ```
     - Response Variable: `deepseek_response`

   - **Action 2**: Call service
     - Service: `notify.mobile_app` or similar
     - Service Data:
       ```yaml
       title: "Recipe Suggestion"
       message: "{{ deepseek_response.response }}"
       ```

## Important Notes

1. The `response_variable` field is crucial - it saves the response for use in later actions
2. When using the stored response, use `{{ variable_name.response }}` to access the content
3. You can use this pattern in any automation scenario where you want AI-generated content