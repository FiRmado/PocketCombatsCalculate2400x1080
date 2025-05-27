import React, { useState } from 'react';
import { View, ScrollView, StyleSheet, ImageBackground } from 'react-native';
import { TextInput, Button, Text, RadioButton } from 'react-native-paper';
import { useFonts, Cinzel_700Bold } from '@expo-google-fonts/cinzel';
import { Merriweather_400Regular } from '@expo-google-fonts/merriweather';

export default function AttributesScreen() {
  const [fontsLoaded] = useFonts({
    'Cinzel-Bold': Cinzel_700Bold,
    'Merriweather': Merriweather_400Regular,
  });

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
    
    const manaCoef = (100 + wis) / 100;
    if (characterClass === 'mage') {
      mana = Math.floor((8 + lvl * (lvl <= 70 ? 5 : 7)) * manaCoef);
    } else if (characterClass === 'warrior') {
      mana = Math.floor((8 + lvl * (lvl <= 70 ? 2 : 3)) * manaCoef);
    }
    
    return { hp, mana };
  };

  if (!fontsLoaded) {
    return null;
  }

  const stats = calculateStats();

  return (
    <ImageBackground 
      source={{ uri: 'https://images.pexels.com/photos/3832623/pexels-photo-3832623.jpeg' }}
      style={styles.container}
    >
      <ScrollView style={styles.scrollView}>
        <View style={styles.content}>
          <Text style={styles.title}>Character Builder</Text>
          
          <View style={styles.card}>
            <TextInput
              label="Level"
              value={level}
              onChangeText={setLevel}
              keyboardType="numeric"
              style={styles.input}
              mode="outlined"
              theme={{ colors: { primary: '#d4af37' }}}
            />

            <Text style={styles.sectionTitle}>Class Selection</Text>
            <RadioButton.Group onValueChange={value => setCharacterClass(value)} value={characterClass}>
              <View style={styles.radioGroup}>
                <RadioButton.Item 
                  label="Mage" 
                  value="mage" 
                  labelStyle={styles.radioLabel}
                  color="#d4af37"
                />
                <RadioButton.Item 
                  label="Warrior" 
                  value="warrior" 
                  labelStyle={styles.radioLabel}
                  color="#d4af37"
                />
              </View>
            </RadioButton.Group>

            <View style={styles.statsContainer}>
              <Text style={styles.statsText}>Available Attributes: {calculateAttributes()}</Text>
              <Text style={styles.statsText}>HP: {stats.hp}</Text>
              <Text style={styles.statsText}>Mana: {stats.mana}</Text>
            </View>

            <Text style={styles.sectionTitle}>Attributes</Text>
            {Object.entries(attributes).map(([attr, value]) => (
              <TextInput
                key={attr}
                label={attr.charAt(0).toUpperCase() + attr.slice(1)}
                value={value}
                onChangeText={(text) => setAttributes(prev => ({ ...prev, [attr]: text }))}
                keyboardType="numeric"
                style={styles.input}
                mode="outlined"
                theme={{ colors: { primary: '#d4af37' }}}
              />
            ))}
          </View>
        </View>
      </ScrollView>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: 16,
  },
  title: {
    fontSize: 32,
    fontFamily: 'Cinzel-Bold',
    color: '#ffffff',
    textAlign: 'center',
    marginVertical: 24,
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: { width: 2, height: 2 },
    textShadowRadius: 4,
  },
  card: {
    backgroundColor: 'rgba(25, 25, 25, 0.9)',
    borderRadius: 12,
    padding: 20,
    marginBottom: 20,
  },
  input: {
    marginBottom: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    fontFamily: 'Merriweather',
  },
  radioGroup: {
    marginVertical: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 8,
  },
  radioLabel: {
    color: '#ffffff',
    fontFamily: 'Merriweather',
  },
  statsContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#d4af37',
  },
  statsText: {
    fontSize: 16,
    marginBottom: 8,
    color: '#ffffff',
    fontFamily: 'Merriweather',
  },
  sectionTitle: {
    fontSize: 20,
    color: '#d4af37',
    fontFamily: 'Cinzel-Bold',
    marginVertical: 16,
  },
});