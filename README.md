# Moojo Lead Generation Crew

This project uses CrewAI to automate the process of finding and analyzing e-commerce companies using AI shopping assistants that need Moojo's privacy-preserving consumer identity solution.

## Overview

The crew consists of four specialized AI agents working together to:

1. Find companies using AI shopping assistants that need privacy-preserving identity solutions
2. Analyze their e-commerce privacy and compliance needs
3. Evaluate their shopping AI implementations
4. Create personalized retail outreach strategies

### Agents and Their Roles

1. **AI Commerce Researcher**

   - Identifies companies using AI shopping assistants
   - Focuses on e-commerce and retail sectors
   - Creates initial assessment of shopping experience needs

2. **Privacy and Compliance Analyst**

   - Evaluates e-commerce privacy implications
   - Analyzes retail regulations (GDPR, CCPA, PCI-DSS)
   - Identifies privacy risks in shopping flows

3. **AI Commerce Implementation Specialist**

   - Analyzes shopping AI architectures
   - Evaluates checkout and payment flows
   - Identifies integration opportunities in purchase processes

4. **E-commerce Business Development Strategist**
   - Creates retail-focused outreach strategies
   - Maps e-commerce decision-makers
   - Develops shopping-specific value propositions

### Workflow

The crew follows a sequential process:

1. **Research Phase**

   - Identifies 5-10 promising e-commerce companies
   - Gathers information about AI shopping implementations
   - Initial assessment of retail privacy needs

2. **Privacy Analysis**

   - Evaluates e-commerce privacy practices
   - Identifies retail compliance requirements
   - Assesses payment data protection needs

3. **Technical Analysis**

   - Reviews shopping AI implementations
   - Analyzes checkout verification methods
   - Evaluates personalization vs. privacy balance

4. **Final Report**

   - Synthesizes all retail analyses
   - Prioritizes e-commerce prospects
   - Creates detailed company profiles

5. **Outreach Strategy**
   - Develops retail-focused approach plans
   - Creates e-commerce stakeholder maps
   - Crafts shopping-specific messaging

### Outputs

The crew generates two main outputs:

1. `moojo_leads_report.md`: Comprehensive analysis of e-commerce prospects
2. `outreach_strategy.md`: Detailed retail outreach plans for each prospect

## Setup and Usage

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:

```
SERPER_API_KEY=your_key_here
```

3. Run the crew:

```bash
crewai run
```

## Example Output

See `moojo_leads_report.md` and `outreach_strategy.md` for the latest run outputs.

## Technical Details

- Built using CrewAI framework
- Uses Serper API for web research
- Configuration driven using YAML files
- Modular agent and task design

## Files Structure

```
src/edu/
├── config/
│   ├── agents.yaml    # Agent configurations
│   └── tasks.yaml     # Task definitions
├── crew.py           # Main crew implementation
└── main.py          # Entry point
```
