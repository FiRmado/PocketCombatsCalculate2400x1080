import React, { useState } from 'react';
import { View, ScrollView, StyleSheet } from 'react-native';
import { TextInput, Button, Text, RadioButton } from 'react-native-paper';

export default function AttributesScreen() {
  const [level, setLevel] = useState('1');
  const [characterClass, setCharacterClass] = useState('mage');
  const [attributes, setAttributes] = useState({
    strength: '1',
    dexterity: '1',
    intuition: '1',
    endurance: '1',
    wisdom: '1',
    luck: '1'
  });

  const calculateAttributes = () => {
    let total = 0;
    const lvl = parseInt(level);
    
    for (let i = 1; i < lvl; i++) {
      total += Math.floor(i / 5 + 3);
    }
    total += 31;
    
    return total;
  };

  const calculateStats = () => {
    const lvl = parseInt(level);
    const end = parseInt(attributes.endurance);
    const wis = parseInt(attributes.wisdom);
    
    let hp = 35 + lvl * 5;
    let mana = 0;
    
    // HP calculation based on class
    if (characterClass === 'mage') {
      for (let i = 2; i <= lvl; i++) {
        hp += Math.floor(i * 0.3);
      }
    } else if (characterClass === 'warrior') {
      for (let i = 2; i <= lvl; i++) {
        hp += Math.floor(i * 0.7);
      }
    }
    
    hp += Math.floor((hp * end) / 100);
    
    // Mana calculation
    const manaCoef = (100 + wis) / 100;
    if (characterClass === 'mage') {
      mana = Math.floor((8 + lvl * (lvl <= 70 ? 5 : 7)) * manaCoef);
    } else if (characterClass === 'warrior') {
      mana = Math.floor((8 + lvl * (lvl <= 70 ? 2 : 3)) * manaCoef);
    }
    
    return { hp, mana };
  };

  const stats = calculateStats();

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>PocketCombats Calculator</Text>
      
      <TextInput
        label="Level"
        value={level}
        onChangeText={setLevel}
        keyboardType="numeric"
        style={styles.input}
        mode="outlined"
      />

      <RadioButton.Group onValueChange={value => setCharacterClass(value)} value={characterClass}>
        <View style={styles.radioGroup}>
          <RadioButton.Item label="Mage" value="mage" />
          <RadioButton.Item label="Warrior" value="warrior" />
          <RadioButton.Item label="Hunter" value="hunter" />
          <RadioButton.Item label="Newbie" value="newbie" />
        </View>
      </RadioButton.Group>

      <View style={styles.statsContainer}>
        <Text style={styles.statsText}>Available Attributes: {calculateAttributes()}</Text>
        <Text style={styles.statsText}>HP: {stats.hp}</Text>
        <Text style={styles.statsText}>Mana: {stats.mana}</Text>
      </View>

      {Object.entries(attributes).map(([attr, value]) => (
        <TextInput
          key={attr}
          label={attr.charAt(0).toUpperCase() + attr.slice(1)}
          value={value}
          onChangeText={(text) => setAttributes(prev => ({ ...prev, [attr]: text }))}
          keyboardType="numeric"
          style={styles.input}
          mode="outlined"
        />
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 16,
  },
  input: {
    marginBottom: 12,
    backgroundColor: 'white',
  },
  radioGroup: {
    marginVertical: 12,
    backgroundColor: 'white',
    borderRadius: 8,
  },
  statsContainer: {
    backgroundColor: 'white',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
  },
  statsText: {
    fontSize: 16,
    marginBottom: 8,
  },
});