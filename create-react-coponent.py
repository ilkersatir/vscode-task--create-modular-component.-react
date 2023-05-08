import os

# Get user inputs
component_name = input("Enter component name: ")
dir_path = input("Enter the directory path where you want to create the component (default: src/components): ") or "src/components"
style_type = input("Enter the style type (tsx or scss): ") or "scss"

# Create the component directory
component_dir = os.path.join(dir_path, component_name)
os.makedirs(component_dir)

# Create the component files and write content 
with open(os.path.join(component_dir, "index.ts"), "w") as f:
    f.write(f"export * from './{component_name}'\n")

with open(os.path.join(component_dir, f"{component_name}.tsx"), "w") as f:
    
    if style_type == "tsx":
        f.write(f"import {{ {component_name}Styles }} from './{component_name}.styles';\n\n")
    else:
        f.write(f"import './{component_name}.styles.{style_type}'\n\n")      

    f.write(f"type {component_name}Props = {{\n")
    f.write(f"  // props\n")
    f.write(f"}}\n\n")
    f.write(f"export const {component_name} = () => {{\n")
    f.write(f"  return (\n")
    f.write(f"    <div className='{component_name}'>\n")
    f.write(f"      {component_name}\n")
    f.write(f"    </div>\n")
    f.write(f"  )\n")
    f.write(f"}}\n\n")
    f.write(f"export default {component_name};\n")

if style_type == "tsx":
    with open(os.path.join(component_dir, f"{component_name}.styles.tsx"), "w") as f:
        f.write(f"export const {component_name}Styles = [ /* Style */ ]\n")

else:
    with open(os.path.join(component_dir, f"{component_name}.styles.{style_type}"), "w") as f:
        f.write(f".{component_name} {{ /* Style */ }}\n")

with open(os.path.join(component_dir, f"{component_name}.test.tsx"), "w") as f:
    f.write(f"import {{ render, screen }} from '@testing-library/react';\n")
    f.write(f"import {component_name} from './{component_name}';\n\n")
    f.write(f"describe('{component_name}', () => {{\n")
    f.write(f"  test.skip('renders the {component_name} component', () => {{\n")
    f.write(f"    render(<{component_name} />);\n")
    f.write(f"    const component = screen.getByText('{component_name}');\n")
    f.write(f"    expect(component).toBeInTheDocument();\n")
    f.write(f"  }});\n")
    f.write(f"}});\n")

with open(os.path.join(component_dir, f"{component_name}.stories.tsx"), "w") as f:
    f.write(f"import {{ Story, Meta }} from '@storybook/react';\n")
    f.write(f"import {{ {component_name} }} from './{component_name}';\n\n")
    f.write(f"export default {{\n")
    f.write(f"  title: '{component_name}',\n")
    f.write(f"  component: {component_name},\n")
    f.write(f"}} as Meta;\n\n")
    f.write(f"const Template: Story = (args) => <{component_name} {{...args}} />;\n\n")
    f.write(f"export const Default = Template.bind({{}});\n") 
    f.write(f"Default.args = {{\n")
    f.write(f" // props \n")
    f.write(f"}};\n")


# Add export statement to the index.ts file
with open(os.path.join(dir_path, "index.ts"), "a") as f:
    f.write(f"export * from './{component_name}';\n")