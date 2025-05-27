import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Provider as PaperProvider } from 'react-native-paper';
import { MaterialCommunityIcons } from '@expo/vector-icons';

import AttributesScreen from './src/screens/AttributesScreen';
import StatsScreen from './src/screens/StatsScreen';
import SkillsScreen from './src/screens/SkillsScreen';
import SettingsScreen from './src/screens/SettingsScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <PaperProvider>
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={{
            tabBarActiveTintColor: '#2196F3',
            tabBarInactiveTintColor: 'gray',
          }}
        >
          <Tab.Screen 
            name="Attributes" 
            component={AttributesScreen}
            options={{
              tabBarIcon: ({ color }) => (
                <MaterialCommunityIcons name="calculator" size={26} color={color} />
              ),
            }}
          />
          <Tab.Screen 
            name="Stats" 
            component={StatsScreen}
            options={{
              tabBarIcon: ({ color }) => (
                <MaterialCommunityIcons name="heart" size={26} color={color} />
              ),
            }}
          />
          <Tab.Screen 
            name="Skills" 
            component={SkillsScreen}
            options={{
              tabBarIcon: ({ color }) => (
                <MaterialCommunityIcons name="sword" size={26} color={color} />
              ),
            }}
          />
          <Tab.Screen 
            name="Settings" 
            component={SettingsScreen}
            options={{
              tabBarIcon: ({ color }) => (
                <MaterialCommunityIcons name="cog" size={26} color={color} />
              ),
            }}
          />
        </Tab.Navigator>
      </NavigationContainer>
    </PaperProvider>
  );
}